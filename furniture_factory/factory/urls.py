from django.urls import path
from . import views

urlpatterns = [
    path('', views.order_list, name='order_list'),
    path('orders/create/', views.order_create, name='order_create'),
    path('orders/<int:order_id>/', views.order_detail, name='order_detail'),
    path('workshops/', views.workshop_list, name='workshop_list'),
]