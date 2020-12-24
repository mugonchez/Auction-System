import pytz
from datetime import datetime, timedelta, date
from django.shortcuts import render, get_object_or_404, redirect
from .models import Product, Category, Review,  BidItems, Bidders
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from .forms import ReviewForm, FeedbackForm, BiddersForm
from django.contrib import messages
from cart.forms import CartAddProductForm
from django.contrib.auth.decorators import login_required
from django.db.models import Max


def product_list(request, category_slug=None):
    category = None
    bidders = Bidders.objects.all()
    checker = False
    today = date.today().strftime("%A")
    utc = pytz.UTC
    bidItems = BidItems.objects.filter(available=True)
    for bidd  in bidItems:
        now = datetime.now()
        end = bidd.end_date + timedelta(hours=3)
        now = now.replace(tzinfo=utc)
        if now > end:
            bidd.available = False
            bidd.save()
            for bi in bidders:
                bi.active = False
                bi.save()
            checker = True
            bidd.time = True
            bidder = Bidders.objects.filter(active=False).aggregate(Max('amount'))
            print (bidder.get('amount__max'))
            for bid in bidders:
                if bid.amount == bidder.get('amount__max'):
                    bid.won = True
                    bid.save()
    men = Category.objects.get(name='Men')
    women = Category.objects.get(name='Women')
    shoes = Category.objects.get(name='Shoes')
    jewelry = Category.objects.get(name='Jewelry')
    phones = Category.objects.get(name='Phones')
    laptops = Category.objects.get(name='Laptops')
    home_appliances = Category.objects.get(name='Home Appliances')
    play_station = Category.objects.get(name='Play Station')
    others = Category.objects.get(name='Others')
    furniture = Category.objects.get(name='Furniture')
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)
    paginator = Paginator(products, 12)
    page = request.GET.get('page')
    print (checker)

    try:
        products = paginator.page(page)
    except PageNotAnInteger:
        products = paginator.page(1)
    except EmptyPage:
        products = paginator.page(paginator.num_pages)
    return render(request, 'catalog/list.html', {'category': category,
                                                 'categories': categories,
                                                 'page': page,
                                                 'checker': checker,
                                                 'bidItems': bidItems,
                                                 'products': products,
                                                 'men': men,
                                                 'women': women,
                                                 'shoes': shoes,
                                                 'jewelry': jewelry,
                                                 'phones': phones,
                                                 'laptops': laptops,
                                                 'home_appliances': home_appliances,
                                                 'play_station': play_station,
                                                 'furniture': furniture,
                                                 'others': others,
                                                 'today': today
                                                 })


def product_detail(request, id, slug):
    product = get_object_or_404(Product, id=id, slug=slug, available=True)
    reviews = product.reviews.filter(active=True)

    review_count = product.reviews.count()

    paginator = Paginator(reviews, 3)
    page = request.GET.get('page')
    try:
        reviews = paginator.page(page)
    except PageNotAnInteger:
        reviews = paginator.page(1)
    except EmptyPage:
        reviews = paginator.page(paginator.num_pages)

    cart_product_form = CartAddProductForm()
    return render(request,
                  'catalog/detail.html',
                  {'product': product,
                   'reviews': reviews,
                   'review_count': review_count,
                   'cart_product_form': cart_product_form})

@login_required
def bid_detail(request, id):
    bidItem = get_object_or_404(BidItems, id=id,available=True)
    bids = bidItem.biditems.filter(active=True)
    if request.method == 'POST':
        bid_form = BiddersForm(data=request.POST)

        if bid_form.is_valid():
            if bid_form.cleaned_data['amount'] < bidItem.minimum_price:
                messages.error(request, 'Your amount is less than the minimum bid amount required')
                return redirect('catalog:bid_detail', bidItem.id)
            new_bid_form = bid_form.save(commit=False)
            new_bid_form.bidItem = bidItem
            new_bid_form.user = request.user
            new_bid_form.save()
            if bid_form.cleaned_data['amount'] > bidItem.minimum_price:
                bidItem.minimum_price = bid_form.cleaned_data['amount']
                bidItem.save()
            return redirect('catalog:bid_detail', bidItem.id)
    else:
        bid_form = BiddersForm()
    bid_count = bidItem.biditems.count()
    return render(request,
                  'catalog/bid.html',
                  {'bidItem': bidItem,
                   'bid_count': bid_count,
                   'bids': bids,
                   'bid_form': bid_form})



@login_required
def product_review(request, id):
    product = get_object_or_404(Product, id=id, available=True)
    reviews = product.reviews.filter(active=True)

    if request.method == 'POST':
        review_form = ReviewForm(data=request.POST)

        if review_form.is_valid():
            new_review_form = review_form.save(commit=False)
            new_review_form.product = product
            new_review_form.user = request.user
            new_review_form.save()
            messages.success(request, 'Your review has successfully been submitted')
    else:
        review_form = ReviewForm()

    review_count = product.reviews.count()

    cart_product_form = CartAddProductForm()

    return render(request,
                  'catalog/review.html',
                  {'product': product,
                   'reviews': reviews,
                   'review_form': review_form,
                   'review_count': review_count,
                   'cart_product_form': cart_product_form})


def help_center(request):
    return render(request, 'catalog/help.html')


def returns_policy(request):
    return render(request, 'catalog/returns.html')


def secure_payment(request):
    return render(request, 'catalog/payment.html')


def responsibility(request):
    return render(request, 'catalog/responsibility.html')


def privacy(request):
    return render(request, 'catalog/privacy.html')


def delivery(request):
    return render(request, 'catalog/delivery.html')


def careers(request):
    return render(request, 'catalog/career.html')


def conditions(request):
    return render(request, 'catalog/conditions.html')


def contact(request):
    return render(request, 'catalog/contact.html')


def feedback(request):
    if request.method == 'POST':
        feedback_form = FeedbackForm(request.POST, instance=request.user.feedback)
        if feedback_form.is_valid():
            feedback_form.save()
            messages.success(request, 'Thank you! Your feedback has successfully been received')
    else:
        feedback_form = FeedbackForm(instance=request.user.feedback)
    return render(request, 'catalog/feedback.html', {'feedback_form': feedback_form})





