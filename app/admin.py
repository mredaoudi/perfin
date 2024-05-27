from django.contrib import admin
from .models import Account, Transaction, Entity, Category


@admin.register(Account)
class AccountAdmin(admin.ModelAdmin):
    list_display = ('name', 'is_saving', 'initial_amount', 'current_amount', 'start_date')
    search_fields = ('name',)
    list_filter = ('is_saving',)


@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    list_display = ('account', 'amount', 'entity', 'transaction_date')
    search_fields = ('account_id__name', 'entity__name')
    list_filter = ('transaction_date',)


@admin.register(Entity)
class EntityAdmin(admin.ModelAdmin):
    list_display = ('name', 'category')
    search_fields = ('name',)
    list_filter = ('category',)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)
