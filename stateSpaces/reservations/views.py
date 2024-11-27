from django.shortcuts import render

# Create your views here.
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse
from django.shortcuts import redirect

from .models import Product, Transaction
from .forms import MerchForm, TransactionForm
from user_management.models import Profile


class MerchListView(LoginRequiredMixin, ListView):
    model = Product
    template_name = 'merchstore_list.html'
    context_object_name = 'items'

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        user_profile = Profile.objects.get(user=self.request.user)
        owner_products = Product.objects.filter(owner=user_profile)
        other_products = Product.objects.exclude(owner=user_profile)

        product_types = {}
        for product in other_products:
            product_type = product.product_type
            if product_type.name not in product_types:
                product_types[product_type.name] = []
            product_types[product_type.name].append(product)
        
        ctx['owner_products'] = owner_products
        ctx['product_types'] = product_types
        
        return ctx


class MerchDetailView(DetailView):
    model = Product
    template_name = 'merchstore_detail.html'
    context_object_name = 'item'

    def get_current_user(self):
        return Profile.objects.get(user=self.request.user)

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        product = self.get_object()

        if self.request.user.is_authenticated:
            buyer = self.get_current_user()
            transaction_form = TransactionForm(initial={'product': product, 'buyer': buyer})
            ctx['buyer'] = buyer
        else:
            transaction_form = TransactionForm(initial={'product': product})
        ctx['transaction_form'] = transaction_form
        return ctx

    def post(self, request, *args, **kwargs):
        product = self.get_object()
        transaction_form = TransactionForm(request.POST)
        if transaction_form.is_valid():
            transaction = transaction_form.save(commit=False)
            transaction.product = product
            product.stock -= transaction.amount
            if request.user.is_authenticated:
                buyer = self.get_current_user()
                transaction.buyer = buyer
                transaction.save()
                product.save()
                return redirect('merchstore:cart')
            else:
                return redirect('merchstore:items')

        ctx = self.get_context_data(object=product, transaction_form=transaction_form)
        return self.render_to_response(ctx)


class MerchCreateView(LoginRequiredMixin, CreateView):
    model = Product
    form_class = MerchForm
    template_name = 'merchstore_create.html'

    def get_form(self, form_class=None):
        form = super().get_form(form_class=form_class)
        form.fields['owner'].initial = Profile.objects.get(user=self.request.user)
        form.fields['owner'].disabled = True
        return form

    def get_success_url(self):
        return reverse('merchstore:item', kwargs={'pk': self.object.pk})


class MerchUpdateView(LoginRequiredMixin, UpdateView):
    model = Product
    form_class = MerchForm
    template_name = 'merchstore_update.html'

    def get_form(self, form_class=None):
        form = super().get_form(form_class=form_class)
        form.fields['owner'].initial = Profile.objects.get(user=self.request.user)
        form.fields['owner'].disabled = True
        return form

    def get_success_url(self):
        return reverse('merchstore:item', kwargs={'pk': self.object.pk})


class MerchTransactionView(LoginRequiredMixin, ListView):
    model = Transaction
    template_name = 'merchstore_transactions.html'

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        user = Profile.objects.get(user=self.request.user)
        owner_products = Product.objects.filter(owner=user)
        owner_transactions = Transaction.objects.filter(product__in=owner_products)
        ctx['owner_transactions'] = owner_transactions
        ctx['buyers_list'] = Profile.objects.all()
        return ctx


class MerchCartView(LoginRequiredMixin, ListView):
    model = Transaction
    template_name = 'merchstore_cart.html'

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        user = Profile.objects.get(user=self.request.user)
        ctx['buyer_transactions'] = Transaction.objects.filter(buyer=user)
        ctx['sellers_list'] = Profile.objects.all()
        return ctx