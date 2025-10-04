from django.db.models.signals import m2m_changed
from django.dispatch import receiver
from django.core.mail import send_mail
from .models import Order
import os


EMAIL_HOST_USER = os.getenv('EMAIL_HOST_USER')


@receiver(m2m_changed, sender=Order.furnitures.through)
def send_order_confirmation_email(sender, instance, action, **kwargs):
    """
    Отправляет информационное письмо клиенту после добавления мебелей в заказ.
    """
    if action == "post_add":
        furniture_list = "\n".join([f"{furniture.name} - {furniture.price}" for furniture in instance.furnitures.all()])
        
        message = f"""
Спасибо за ваш заказ!

Детали заказа:
{furniture_list}

Общая стоимость: {instance.total_price}
        """

        send_mail(
            subject="Ваш заказ подтвержден",
            message=message,
            from_email=EMAIL_HOST_USER,
            recipient_list=[instance.customer_email],
            fail_silently=False,
        )
        