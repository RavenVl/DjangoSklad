from django.db import models

class Group(models.Model):


    name = models.CharField(max_length=100, verbose_name="Название группы")
    description = models.TextField(blank=True, verbose_name="Описание группы")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")

    class Meta:
        verbose_name = "Группа товаров"
        verbose_name_plural = "Группы товаров"
        ordering = ['name']

    def __str__(self):
        return self.name

class Prod(models.Model):
    name = models.CharField(max_length=200, verbose_name="Название")
    description = models.TextField(blank=True, verbose_name="Описание")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Цена")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Дата обновления")
    sku = models.CharField(max_length=50, unique=True, verbose_name="Артикул")
    group = models.ForeignKey(Group, on_delete=models.PROTECT, verbose_name="Группа товаров", related_name='products')

    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"
        ordering = ['-created_at']

    def __str__(self):
        return self.name

from django.db import models

class Supplier(models.Model):
    name = models.CharField(max_length=200, verbose_name="Название компании")
    contact_person = models.CharField(max_length=100, verbose_name="Контактное лицо")
    phone = models.CharField(max_length=20, verbose_name="Телефон")
    email = models.EmailField(verbose_name="Email")
    address = models.TextField(verbose_name="Адрес")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")

    class Meta:
        verbose_name = "Поставщик"
        verbose_name_plural = "Поставщики"
        ordering = ['name']

    def __str__(self):
        return self.name

class Customer(models.Model):
    name = models.CharField(max_length=200, verbose_name="Название компании")
    contact_person = models.CharField(max_length=100, verbose_name="Контактное лицо")
    phone = models.CharField(max_length=20, verbose_name="Телефон")
    email = models.EmailField(verbose_name="Email")
    address = models.TextField(verbose_name="Адрес")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")

    class Meta:
        verbose_name = "Покупатель"
        verbose_name_plural = "Покупатели"
        ordering = ['name']

    def __str__(self):
        return self.name

class OperationType(models.Model):
    name = models.CharField(max_length=100, verbose_name="Тип операции")
    description = models.TextField(blank=True, verbose_name="Описание")

    class Meta:
        verbose_name = "Тип операции"
        verbose_name_plural = "Типы операций"
        ordering = ['name']

    def __str__(self):
        return self.name

class Operation(models.Model):
    code = models.IntegerField(unique=True, verbose_name="Код операции")
    name = models.CharField(max_length=200, verbose_name="Наименование")
    operation_type = models.ForeignKey(OperationType, on_delete=models.PROTECT, verbose_name="Тип операции", related_name='operations')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")

    class Meta:
        verbose_name = "Операция"
        verbose_name_plural = "Операции"
        ordering = ['code']

    def __str__(self):
        return f"{self.code} - {self.name}"


class Warehouse(models.Model):
    number = models.IntegerField(unique=True, verbose_name="Номер склада")
    name = models.CharField(max_length=200, verbose_name="Название склада")

    class Meta:
        verbose_name = "Склад"
        verbose_name_plural = "Склады"
        ordering = ['number']

    def __str__(self):
        return f"{self.number} - {self.name}"


class Transaction(models.Model):
    date = models.DateTimeField(verbose_name="Дата операции")
    operation = models.ForeignKey(Operation, on_delete=models.PROTECT, verbose_name="Операция", related_name='transactions')
    warehouse = models.ForeignKey(Warehouse, on_delete=models.PROTECT, verbose_name="Склад", related_name='transactions')
    product = models.ForeignKey(Prod, on_delete=models.PROTECT, verbose_name="Товар", related_name='transactions')
    customer = models.ForeignKey(Customer, on_delete=models.PROTECT, verbose_name="Покупатель", related_name='transactions')
    quantity = models.IntegerField(verbose_name="Количество товара")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Цена товара")
    total_sum = models.DecimalField(max_digits=12, decimal_places=2, verbose_name="Итоговая сумма")

    class Meta:
        verbose_name = "Операция"
        verbose_name_plural = "Операции"
        ordering = ['-date']

    def __str__(self):
        return f"Операция {self.operation} от {self.date}"

    def save(self, *args, **kwargs):
        self.total_sum = self.quantity * self.price
        super().save(*args, **kwargs)

