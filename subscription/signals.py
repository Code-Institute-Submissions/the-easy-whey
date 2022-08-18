from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

from .models import SubscriptionLineItem

@receiver(post_save, sender=SubscriptionLineItem)
def update_on_save(sender, instance, created, **kwargs):
    instance.subscription.update_total()


# @receiver(post_delete, sender=SubscriptionLineItem)
# def update_on_delete(sender, instance, **kwargs):
#     instance.subscription.update_total()