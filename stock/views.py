from django.shortcuts import render
from .models import StockList
from django.db.models.functions import Lower


def index(request):
    if request.GET.get('sort') == 'desc':
        stock_list = StockList.objects.all().order_by(Lower('company_name').desc())
    else:
        stock_list = StockList.objects.all().order_by(Lower('company_name').asc())

    context = {
        'stock_list': stock_list
    }

    return render(request, 'index.html', context)
