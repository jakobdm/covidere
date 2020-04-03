from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import (CreateView, DetailView, ListView,
                                  UpdateView)

from order.models import Order
from product.models import Product
from shop.models import Shop


class ShopUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    """
    Shop Update View, handle view and update shop objects. Will only allow update of users own shop for now
    """
    model = Shop
    fields = ['name', 'address', 'zipcode', 'city', 'email', 'homepage', 'phone', 'mobilepay', 'contact']
    template_name = 'shop/update.html'
    success_url = reverse_lazy('shop_update')
    success_message = "Information updated!"

    def get_object(self, queryset=None):
        return self.request.user.shop


class ShopProductListView(LoginRequiredMixin, ListView):
    """
    Shop Product List View. Will list all products related to a single shop. Based on current user.
    """
    model = Product
    template_name = 'shop/product_list.html'

    def get_queryset(self):
        queryset = Product.objects.filter(shop=self.request.user.shop)
        return queryset


class ShopOrderListView(LoginRequiredMixin, ListView):
    """
    Shop Order List View. Will list all orders related to a shop. 
    For now based on current user. 
    Orders can contains products from other shops.
    """
    model = Order
    template_name = 'shop/order_list.html'

    def get_queryset(self):
        queryset = Order.objects.filter(items__product__shop=self.request.user.shop).distinct()
        return queryset

class ShopOrderDetailView(LoginRequiredMixin, DetailView):
    model = Order
    template_name = 'shop/order_detail.html'


class ShopOverviewView(LoginRequiredMixin, View):
    def get(self, request):
        return render(request, 'shop/overview.html')


class ShopProductUpdateView(LoginRequiredMixin, UpdateView):
    model = Product
    fields = ['name', 'description', 'price', 'on_sale', 'color', 'size', 'active', 'delivery_days', 'start_datetime', 'end_datetime']
    template_name = 'product/update.html'
    success_url = reverse_lazy('shop_products')

    def get_queryset(self):
        queryset = Product.objects.filter(shop=self.request.user.shop)
        return queryset


class ShopProductCreateView(LoginRequiredMixin, CreateView):
    model = Product
    fields = ['name', 'description','price', 'on_sale', 'color', 'size', 'active', 'delivery_days', 'start_datetime', 'end_datetime']
    template_name = 'product/create.html'
    success_url = reverse_lazy('shop_products')

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.shop = self.request.user.shop
        return super(ShopProductCreateView, self).form_valid(form)