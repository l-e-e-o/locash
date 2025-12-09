from django.contrib import admin
from .models import User, Product, Transaction

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'display_name', 'id12', 'balance')
    search_fields = ('username', 'display_name', 'id12')

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'id12', 'price')
    search_fields = ('name', 'id12')

@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    list_display = ('tx_type', 'amount', 'user', 'to_user', 'product', 'timestamp')
    list_filter = ('tx_type',)
    search_fields = ('user__username', 'to_user__username', 'product__name')
