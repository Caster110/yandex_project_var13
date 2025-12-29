from django import forms
from .models import Order, Workshop

class OrderForm(forms.ModelForm):
    workshops = forms.ModelMultipleChoiceField(
        queryset=Workshop.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        label="Цеха, участвующие в выполнении заказа"
    )

    class Meta:
        model = Order
        fields = ['description', 'order_type']