from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from products.models import Product


@receiver(post_save, sender=Product)
def product_create_signal(sender, instance, **kwargs):
    print("product created", instance)