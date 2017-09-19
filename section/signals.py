from django.db.models.signals import post_save
from django.dispatch import receiver
from django.dispatch import Signal

# @receiver(post_save, sender=StudentPaymentDetail)
# def send_notification(sender,instance, **kwargs):
#     if kwargs.get('created', False):
#         notification = SendNotification.objects.create(student=instance,
#                                                       is_payment_pending=True)



# # In signals.py

update_count = Signal(providing_args=["name","standard","section"])
#
#
