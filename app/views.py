from django.urls import reverse_lazy
from django.http import JsonResponse
from django.shortcuts import redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, DeleteView, TemplateView

from .models import Account, Transaction, Entity, Category
from .mixins import SetUserMixin, AdminOnlyMixin, CreateUpdateView
from .forms import AccountForm, TransactionForm, EntityForm, CategoryForm


class LandingPageView(TemplateView):
    template_name = 'app/landing.html'

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('dashboard')
        return super().dispatch(request, *args, **kwargs)


class DashboardView(LoginRequiredMixin, TemplateView):
    template_name = 'app/dashboard.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        categories_info = {
            c.name: str(c.total_amount(user=self.request.user))
            for c in Category.objects.all()
            if c.total_amount(user=self.request.user)
        }
        context['categories_info'] = dict(sorted(
            categories_info.items(), key=lambda x: x[1], reverse=True
        ))
        return context


class AccountListView(LoginRequiredMixin, ListView):
    model = Account
    template_name = 'app/accounts.html'
    context_object_name = 'accounts'

    def get_queryset(self):
        return Account.objects.filter(user=self.request.user)


class AccountCreateUpdateView(SetUserMixin, CreateUpdateView):
    model = Account
    form_class = AccountForm
    template_name = 'app/form.html'
    success_url = reverse_lazy('account-list')


class AccountDeleteView(LoginRequiredMixin, DeleteView):
    model = Account
    template_name = 'app/accounts/confirm_delete.html'
    success_url = reverse_lazy('account-list')


class TransactionListView(LoginRequiredMixin, ListView):
    model = Transaction
    template_name = 'app/transactions.html'
    context_object_name = 'transactions'

    def get_queryset(self):
        return Transaction.objects.filter(account__user=self.request.user)


class TransactionCreateUpdateView(LoginRequiredMixin, CreateUpdateView):
    model = Transaction
    form_class = TransactionForm
    template_name = 'app/form.html'
    success_url = reverse_lazy('transaction-list')


class TransactionDeleteView(LoginRequiredMixin, DeleteView):
    model = Transaction
    success_url = reverse_lazy('transaction-list')


class EntityListView(LoginRequiredMixin, ListView):
    model = Entity
    template_name = 'app/entities.html'
    context_object_name = 'entities'

    def get_queryset(self):
        return Entity.objects.filter(user=self.request.user)


class EntityCreateUpdateView(SetUserMixin, CreateUpdateView):
    model = Entity
    form_class = EntityForm
    template_name = 'app/form.html'
    success_url = reverse_lazy('entity-list')


class EntityDeleteView(LoginRequiredMixin, DeleteView):
    model = Entity
    template_name = 'app/entities/confirm_delete.html'
    success_url = reverse_lazy('entity-list')


class CategoryListView(LoginRequiredMixin, ListView):
    model = Category
    template_name = 'app/categories.html'
    context_object_name = 'categories'


class CategoryCreateUpdateView(AdminOnlyMixin, LoginRequiredMixin, CreateUpdateView):
    model = Category
    form_class = CategoryForm
    template_name = 'app/form.html'
    success_url = reverse_lazy('category-list')


class CategoryDeleteView(AdminOnlyMixin, LoginRequiredMixin, DeleteView):
    model = Category
    template_name = 'app/categories/confirm_delete.html'
    success_url = reverse_lazy('category-list')


@login_required(login_url='/login/')
def get_month_dashboard(request, month):
    return JsonResponse({'success': True})
