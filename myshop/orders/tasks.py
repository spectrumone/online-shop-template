from celery import task
from django.core.mail import send_mail
from .models import Order

@task
def order_created(order_id):
    """
    Task to send an e-mail notificaton when an order is
    successfully created.
    """
    order = Order.objects.get(id=order_id)
    subject = 'Order nr. {0}'.format(order_id)
    message = 'Dear {0}, \n\nYou have successfully placed an order.\
                Your order id is {1}.'.format(order.first_name, order.id)

    mail_sent = send_mail(subject,
                          message,
                          'admin@myshop.com',
                          [order.email])

    return mail_sent