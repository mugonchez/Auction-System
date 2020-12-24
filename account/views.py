from builtins import str, round

from django.contrib.auth.models import User
import json
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import UserRegistrationForm, UserEditForm, ProfileEditForm, TermsForm, PayForm
from .models import Profile
from orders.models import Order, OrderNotification, OrderDetails
from payment.models import Balance
from catalog.models import Feedback, Bidders
import requests




def register(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        terms_form = TermsForm(request.POST)
        if user_form.is_valid() and terms_form.is_valid():
            # Create a new user object but avoid saving it yet
            new_user = user_form.save(commit=False)
            # Set the chosen password
            new_user.set_password(user_form.cleaned_data['password'])
            # Save the User object
            new_user.save()
            terms_form.save()
            # Create the user profile
            profile = Profile.objects.create(user=new_user)
            feedback = Feedback.objects.create(user=new_user)
            return render(request,
                          'account/register_done.html',
                          {'new_user': new_user})
    else:
        user_form = UserRegistrationForm()
        terms_form = TermsForm()
    return render(request, 'account/register.html', {'user_form': user_form, 'terms_form': terms_form})


@login_required
def edit(request):
    if request.method == 'POST':
        user_form = UserEditForm(instance=request.user,
                                     data=request.POST)
        profile_form = ProfileEditForm(instance=request.user.profile,
                                       data=request.POST,
                                       files=request.FILES)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, 'Profile updated successfully')
        else:
            messages.error(request, 'Error updating your profile')
    else:
        user_form = UserEditForm(instance=request.user)
        profile_form = ProfileEditForm(instance=request.user.profile)
    return render(request, 'account/edit.html', {'user_form': user_form,
                                                 'profile_form': profile_form})


@login_required
def dashboard(request):
    orders = Order.objects.filter(user=request.user).order_by('order')
    recent_order = OrderDetails.objects.filter(details__user=request.user, active=True).distinct()
    total_amount = ""
    user_number = ""
    order_notifications = OrderNotification.objects.filter(user=request.user, active=True, read=False)
    read_notifications = OrderNotification.objects.filter(user=request.user, active=True)
    notification_count = order_notifications.count()
    balances = Balance.objects.filter(user=request.user)
    bidder = Bidders.objects.filter(user=request.user, won=True)
    number = ""
    amount = ""
    # if request.method == 'POST':
    #     pay_form = PayForm(data=request.POST)
    #     if pay_form.is_valid():
    #
    # else:
    #     pay_form = PayForm()
    if request.method == 'POST':
        for recent in recent_order:
            total_amount = recent.get_total_cost()
            total_amount = round(total_amount)
            user_number = recent.phone_number
            user_number = user_number.replace('+', '')
        number = request.POST.get('number')
        amount = request.POST.get('amount')
        print (total_amount)
        access_token = "1FO8GvQ2MCBHwYBI713q4CPfK2qq"
        api_url = "https://sandbox.safaricom.co.ke/mpesa/stkpush/v1/processrequest"
        headers = {"Authorization": "Bearer %s" % access_token}
        Shortcode = "174379"
        Passkey = "bfb279f9aa9bdbcf158e97dd71a467cd2e0c893059b10f78e6b72ada1ed2c919"
        Timestamp = "20190509201552"
        requesting = {
            "BusinessShortCode": "174379",
            "Password": "MTc0Mzc5YmZiMjc5ZjlhYTliZGJjZjE1OGU5N2RkNzFhNDY3Y2QyZTBjODkzMDU5YjEwZjc4ZTZiNzJhZGExZWQyYzkxOTIwMTkwNTA5MjAxNTUy",
            "Timestamp": "20190509201552",
            "TransactionType": "CustomerPayBillOnline",
            "Amount": total_amount,
            "PartyA": user_number,
            "PartyB": "174379",
            "PhoneNumber": user_number,
            "CallBackURL": "https://732d91c8.ngrok.io",
            "AccountReference": "Scarlet",
            "TransactionDesc": "work"
        }
        result = requests.post(api_url, json=requesting, headers=headers)
        print (result.text)
        return render(request, 'payment/payment_done.html')


    return render(request, 'account/dashboard.html', {'orders': orders,
                                                      'order_notifications': order_notifications,
                                                      'notification_count': notification_count,
                                                      'read_notifications': read_notifications,
                                                      'recent_order': recent_order,
                                                      'balances': balances,
                                                      'bidder': bidder})



def pay_bid(request, id):
    bid = get_object_or_404(Bidders, id=id)
    amount = bid.amount
    amount = round(amount)
    phone_number = bid.phone_number
    phone_number = phone_number.replace('+', '')
    access_token = "1FO8GvQ2MCBHwYBI713q4CPfK2qq"
    api_url = "https://sandbox.safaricom.co.ke/mpesa/stkpush/v1/processrequest"
    headers = {"Authorization": "Bearer %s" % access_token}
    Shortcode = "174379"
    Passkey = "bfb279f9aa9bdbcf158e97dd71a467cd2e0c893059b10f78e6b72ada1ed2c919"
    Timestamp = "20190509201552"
    requesting = {
        "BusinessShortCode": "174379",
        "Password": "MTc0Mzc5YmZiMjc5ZjlhYTliZGJjZjE1OGU5N2RkNzFhNDY3Y2QyZTBjODkzMDU5YjEwZjc4ZTZiNzJhZGExZWQyYzkxOTIwMTkwNTA5MjAxNTUy",
        "Timestamp": "20190509201552",
        "TransactionType": "CustomerPayBillOnline",
        "Amount": amount,
        "PartyA": phone_number,
        "PartyB": "174379",
        "PhoneNumber": phone_number,
        "CallBackURL": "https://732d91c8.ngrok.io",
        "AccountReference": "Scarlet",
        "TransactionDesc": "work"
    }
    result = requests.post(api_url, json=requesting, headers=headers)
    print (result.text)
    return render(request, 'payment/payment_done.html')





@login_required
def cancel_order(request, order_id):
    current_order = get_object_or_404(OrderDetails, id=order_id)
    current_order.active = False
    current_order.save()
    return render(request, 'account/cancel_done.html')


@login_required
def clear_order(request, order_id):
    current_order = get_object_or_404(OrderDetails, id=order_id)
    current_order.active = False
    current_order.save()
    return redirect('account:dashboard')




