from rest_framework.serializers import ModelSerializer, StringRelatedField
from .models import Furniture, Order, Category


class FurnitureSerializer(ModelSerializer):
    """
    Сериализатор для модели мебели.
    """
    class Meta:
        model = Furniture
        fields = '__all__'
        

class OrderSerializer(ModelSerializer):
    """
    Сериализатор для модели заказа.
    """
    class Meta:
        model = Order
        fields = '__all__'
        read_only_fields = ['total_price', 'created_at']

    def create(self, validated_data):
        # Для расчета total_price при создании заказа
        furnitures = validated_data.pop("furnitures", [])
        order = Order.objects.create(**validated_data)
        order.furnitures.set(furnitures)
        order.total_price = sum(f.price for f in furnitures)
        order.save()
        return order
