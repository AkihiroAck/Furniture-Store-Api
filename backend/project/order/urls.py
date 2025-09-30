from django.urls import path
from . import views


urlpatterns = [
    path('furniture/', views.FurnitureListView.as_view(), name='furniture-list'),
    path('furniture/<int:pk>/', views.FurnitureDetailView.as_view(), name='furniture-detail'),
    path('orders/', views.OrderListView.as_view(), name='order-list'),
]
