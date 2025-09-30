from rest_framework.generics import RetrieveAPIView, ListCreateAPIView
from .models import Furniture, Order
from .serializers import FurnitureSerializer, OrderSerializer


class FurnitureListView(ListCreateAPIView):
    """
    Представление для создания нового предмета мебели и получения списка мебели с возможностью фильтрации по категории (?category=название_категории).
    """
    queryset = Furniture.objects.all()
    serializer_class = FurnitureSerializer

    def get_queryset(self):
        queryset = super().get_queryset()
        category = self.request.query_params.get('category')
        if category:
            queryset = queryset.filter(category__name=category)
        return queryset


class FurnitureDetailView(RetrieveAPIView):
    """
    Представление для получения деталей конкретного предмета мебели по его ID.
    """
    queryset = Furniture.objects.all()
    serializer_class = FurnitureSerializer


class OrderListView(ListCreateAPIView):
    """
    Представление для создания нового заказа и получения списка заказов с возможностью фильтрации по email клиента (?email=почта_клиента).
    """
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    def get_queryset(self):
        queryset = super().get_queryset()
        email = self.request.query_params.get('email')
        if email:
            queryset = queryset.filter(customer_email=email)
        return queryset

