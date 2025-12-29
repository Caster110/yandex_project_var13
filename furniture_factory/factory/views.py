from django.shortcuts import render, redirect, get_object_or_404
from .models import Order, Workshop, OrderWorkshop
from .forms import OrderForm

def order_list(request):
    orders = Order.objects.all().order_by('-created_at')
    return render(request, 'factory/order_list.html', {'orders': orders})

def order_detail(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    workshops = [ow.workshop for ow in OrderWorkshop.objects.filter(order=order)]
    return render(request, 'factory/order_detail.html', {
        'order': order,
        'workshops': workshops
    })

def order_create(request):
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            order = form.save()
            for workshop in form.cleaned_data['workshops']:
                OrderWorkshop.objects.create(order=order, workshop=workshop)
            return redirect('order_list')
    else:
        form = OrderForm()
    return render(request, 'factory/order_form.html', {'form': form})

def workshop_list(request):
    workshops = Workshop.objects.prefetch_related('worker_set')
    return render(request, 'factory/workshop_list.html', {'workshops': workshops})