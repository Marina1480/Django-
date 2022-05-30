from django.shortcuts import render, redirect

from phones.models import Phone


def index(request):
    return redirect('catalog')


def show_catalog(request):
    s = {'name': 'name',
    'min_price': 'price',
    'max_price': '-price',
    }
    template = 'catalog.html'
    sort = request.GET.get('sort', None)
    if sort == None:
        context = {
            'phones': Phone.objects.all(),
        }
    else:
        context = {
            'phones': Phone.objects.order_by(s[sort])
        }
    return render(request, template, context)


def show_product(request, slug):
    template = 'product.html'
    phone = Phone.objects.get(slug=slug)
    context = {
        'phone': phone,

    }
    return render(request, template, context)
