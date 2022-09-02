from django.shortcuts import render, redirect
from .models import Shop
from .forms import ShopForm
from django.views.generic import DetailView, UpdateView, DeleteView


def shop_home(request):
    shop = Shop.objects.order_by('title')
    return render(request, 'shop/shop_home.html', {'shop': shop})


class ShopDetailView(DetailView):
    model = Shop
    template_name = 'shop/detail_view.html'
    context_object_name = 'shopPost'


def create(request):
    error = ''
    if request.method == 'POST':
        form = ShopForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            error = 'Форма была неверной'

    form = ShopForm()
    data = {
        'form': form,
        'error': error
    }
    return render(request, 'shop/create.html', data)


class ShopUpdateView(UpdateView):
    model = Shop
    template_name = 'shop/create.html'
    form_class = ShopForm


class ShopDeleteView(DeleteView):
    model = Shop
    success_url = '/shop/'
    template_name = 'shop/shop_delete.html'
