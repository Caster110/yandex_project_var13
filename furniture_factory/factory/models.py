from django.db import models


class Workshop(models.Model):
    name = models.CharField(max_length=100, verbose_name="Название цеха")
    supervisor = models.CharField(max_length=100, verbose_name="Начальник цеха")

    def __str__(self):
        return f"{self.name} ({self.supervisor})"


class Worker(models.Model):
    full_name = models.CharField(max_length=100, verbose_name="ФИО рабочего")
    workshop = models.ForeignKey(Workshop, on_delete=models.CASCADE, verbose_name="Цех")

    def __str__(self):
        return self.full_name


class Order(models.Model):
    ORDER_TYPES = [
        ('corpus', 'Корпусная мебель'),
        ('upholstered', 'Мягкая мебель'),
    ]
    description = models.TextField(verbose_name="Описание заказа")
    order_type = models.CharField(max_length=20, choices=ORDER_TYPES, verbose_name="Тип мебели")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")

    def __str__(self):
        return f"Заказ #{self.id} ({self.get_order_type_display()})"


class OrderWorkshop(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    workshop = models.ForeignKey(Workshop, on_delete=models.CASCADE)


    class Meta:
        unique_together = ('order', 'workshop')
        verbose_name = "Цех в заказе"
        verbose_name_plural = "Цеха в заказах"