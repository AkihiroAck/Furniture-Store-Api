from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import send_mail
from .models import Order
import os


EMAIL_HOST_USER = os.getenv('EMAIL_HOST_USER')


@receiver(post_save, sender=Order)
def send_order_confirmation_email(sender, instance, created, **kwargs):
    """
    Отправляет информационное письмо клиенту после создания заказа.
    """
    if created:  # Проверяем, что объект создан, а не обновлен
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
        