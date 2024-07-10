from django.db.models.signals import post_save, pre_save
from django.db.models.signals import post_delete
from django.dispatch import receiver
from products.models import Product, Category


@receiver(post_save, sender=Product)
def product_create_signal(sender, instance, **kwargs):
    print("product created", instance)
    


@receiver(post_delete, sender=Product)
def product_create_signal(sender, instance, **kwargs):
    print("product deleted", instance)

@receiver(post_delete, sender=Category)
def product_create_signal(sender, instance, **kwargs):
    print("category deleted", instance)