from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Prod, Group, Supplier, Customer, Operation, OperationType, Warehouse, Transaction

@admin.register(Prod)
class ProdAdmin(admin.ModelAdmin):
    list_display = ('name', 'sku', 'price',  'group')
    search_fields = ('name', 'sku')
    list_filter = ('group',)

@admin.register(Group)
class GroupAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_at')
    search_fields = ('name',)

@admin.register(Supplier)
class SupplierAdmin(admin.ModelAdmin):
    list_display = ('name', 'contact_person', 'phone', 'email')
    search_fields = ('name', 'contact_person')

@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('name', 'contact_person', 'phone', 'email')
    search_fields = ('name', 'contact_person')

@admin.register(Operation)
class OperationAdmin(admin.ModelAdmin):
    list_display = ('code', 'name', 'operation_type')
    search_fields = ('name', 'code')
    list_filter = ('operation_type',)

@admin.register(OperationType)
class OperationTypeAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

@admin.register(Warehouse)
class WarehouseAdmin(admin.ModelAdmin):
    list_display = ('number', 'name')
    search_fields = ('name',)

@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    list_display = ('date', 'operation', 'warehouse', 'product', 'customer', 'quantity', 'total_sum')
    list_filter = ('operation', 'warehouse', 'customer')
    search_fields = ('product__name', 'customer__name')
