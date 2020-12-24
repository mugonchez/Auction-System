from django.core.mail import send_mail
from .models import OrderDetails


def sending_email(request, order_id):
    use = request.user
    order = OrderDetails.objects.get(id=order_id)
    subject = 'Order no. {}'.format(order.id)
    message = 'Hi {}, your order id {} has successfully been received'.format(use.username, order.id)
    sender = 'moses@admin.com'
    receiver = use.email
    mail_sent = send_mail(subject, message, sender, [receiver], fail_silently=False, )
    return mail_sent
