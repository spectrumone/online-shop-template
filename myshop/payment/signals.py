from io import BytesIO
import weasyprint

from django.conf import settings
from django.core.mail import EmailMessage
from django.shortcuts import get_object_or_404
from django.template.loader import render_to_string

from paypal.standard.models import ST_PP_COMPLETED
from paypal.standard.ipn.signals import valid_ipn_received, invalid_ipn_received

from orders.models import Order  


def payment_notification(sender, **kwargs):
    ipn_obj = sender
    if ipn_obj.payment_status == ST_PP_COMPLETED:
        order = get_object_or_404(Order, id=ipn_obj.invoice)
        order.paid = True
        order.save()

        #create invoice e-mail
        subject = 'My Shop - Invoice no. {}'.format(order.id)
        message = 'Please see attached for the invoice for your recent\
purchase'
        email = EmailMessage(subject,
                             message,
                             'admin@myshop.com',
                             [order.email])

        #generate PDF
        html = render_to_string('orders/order/pdf.html', {'order': order})
        out = BytesIO()
        stylesheets = [weasyprint.CSS(settings.STATIC_ROOT + 'css/pdf.css')]
        weasyprint.HTML(string=html).write_pdf(out,
                                               stylesheets=stylesheets)
        #attach PDF file
        email.attach('order_{}.pdf'.format(order_id),
                     out.getvalue(),
                     'application/pdf')

        #send e-mail
        email.send()

valid_ipn_received.connect(payment_notification)
