from django.contrib import admin
from .models import Workshop, Worker, Order, OrderWorkshop

@admin.register(Workshop)
class WorkshopAdmin(admin.ModelAdmin):
    list_display = ['name', 'supervisor']

@admin.register(Worker)
class WorkerAdmin(admin.ModelAdmin):
    list_display = ['full_name', 'workshop']

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'order_type', 'created_at']
    list_filter = ['order_type']

@admin.register(OrderWorkshop)
class OrderWorkshopAdmin(admin.ModelAdmin):
    list_display = ['order', 'workshop']