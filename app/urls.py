from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView

from . import views


urlpatterns = [
    path('', views.LandingPageView.as_view(), name='landing'),
    path('login/', LoginView.as_view(template_name='app/login.html', redirect_authenticated_user=True), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('dashboard/', views.DashboardView.as_view(), name='dashboard'),
    path('dashboard/<str:month>/', views.get_month_dashboard, name='dashboard-month'),

    path('accounts/', views.AccountListView.as_view(), name='account-list'),
    path('accounts/create/', views.AccountCreateUpdateView.as_view(), name='account-create'),
    path('accounts/<int:pk>/update/', views.AccountCreateUpdateView.as_view(), name='account-update'),
    path('accounts/<int:pk>/delete/', views.AccountDeleteView.as_view(), name='account-delete'),

    path('transactions/', views.TransactionListView.as_view(), name='transaction-list'),
    path('transactions/create/', views.TransactionCreateUpdateView.as_view(), name='transaction-create'),
    path('transactions/<int:pk>/update/', views.TransactionCreateUpdateView.as_view(), name='transaction-update'),
    path('transactions/<int:pk>/delete/', views.TransactionDeleteView.as_view(), name='transaction-delete'),

    path('entities/', views.EntityListView.as_view(), name='entity-list'),
    path('entities/create/', views.EntityCreateUpdateView.as_view(), name='entity-create'),
    path('entities/<int:pk>/update/', views.EntityCreateUpdateView.as_view(), name='entity-update'),
    path('entities/<int:pk>/delete/', views.EntityDeleteView.as_view(), name='entity-delete'),

    path('categories/', views.CategoryListView.as_view(), name='category-list'),
    path('categories/create/', views.CategoryCreateUpdateView.as_view(), name='category-create'),
    path('categories/<int:pk>/update/', views.CategoryCreateUpdateView.as_view(), name='category-update'),
    path('categories/<int:pk>/delete/', views.CategoryDeleteView.as_view(), name='category-delete'),
]
