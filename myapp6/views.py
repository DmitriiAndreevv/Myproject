from django.shortcuts import render
from django.db.models import Sum

from myapp5.models import Product


# Create your views here.

def total_in_db(request):
    total = Product.objects.aggregate(Sum('quantity'))
    context =  {
        'title': 'Общие кол-во посчитано в базе данных',
        'total': total,

    }
    return render(request, 'myapp6/total_count.html', context)

def total_in_view(request):
    products = Product.objects.all()
    total = sum(product.quantity for product in products)
    context =  {
        'title': 'Общие кол-во посчитано в представлении',
        'total': total,

    }
    return render(request, 'myapp6/total_count.html', context)


def total_in_template(request):
    context = {
        'title': 'Общие кол-во посчитано в шаблоне',
        'total': Product,
    }
    return render(request, 'myapp6/total_count.html', context)