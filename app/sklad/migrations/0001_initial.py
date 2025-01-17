# Generated by Django 4.2.7 on 2025-01-13 10:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Название компании')),
                ('contact_person', models.CharField(max_length=100, verbose_name='Контактное лицо')),
                ('phone', models.CharField(max_length=20, verbose_name='Телефон')),
                ('email', models.EmailField(max_length=254, verbose_name='Email')),
                ('address', models.TextField(verbose_name='Адрес')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
            ],
            options={
                'verbose_name': 'Покупатель',
                'verbose_name_plural': 'Покупатели',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Название группы')),
                ('description', models.TextField(blank=True, verbose_name='Описание группы')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
            ],
            options={
                'verbose_name': 'Группа товаров',
                'verbose_name_plural': 'Группы товаров',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Operation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.IntegerField(unique=True, verbose_name='Код операции')),
                ('name', models.CharField(max_length=200, verbose_name='Наименование')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
            ],
            options={
                'verbose_name': 'Операция',
                'verbose_name_plural': 'Операции',
                'ordering': ['code'],
            },
        ),
        migrations.CreateModel(
            name='OperationType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Тип операции')),
                ('description', models.TextField(blank=True, verbose_name='Описание')),
            ],
            options={
                'verbose_name': 'Тип операции',
                'verbose_name_plural': 'Типы операций',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Prod',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Название')),
                ('description', models.TextField(blank=True, verbose_name='Описание')),
                ('price', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Цена')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Дата обновления')),
                ('sku', models.CharField(max_length=50, unique=True, verbose_name='Артикул')),
                ('group', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='sklad.group', verbose_name='Группа товаров')),
            ],
            options={
                'verbose_name': 'Продукт',
                'verbose_name_plural': 'Продукты',
                'ordering': ['-created_at'],
            },
        ),
        migrations.CreateModel(
            name='Supplier',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Название компании')),
                ('contact_person', models.CharField(max_length=100, verbose_name='Контактное лицо')),
                ('phone', models.CharField(max_length=20, verbose_name='Телефон')),
                ('email', models.EmailField(max_length=254, verbose_name='Email')),
                ('address', models.TextField(verbose_name='Адрес')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
            ],
            options={
                'verbose_name': 'Поставщик',
                'verbose_name_plural': 'Поставщики',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Warehouse',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.IntegerField(unique=True, verbose_name='Номер склада')),
                ('name', models.CharField(max_length=200, verbose_name='Название склада')),
            ],
            options={
                'verbose_name': 'Склад',
                'verbose_name_plural': 'Склады',
                'ordering': ['number'],
            },
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(verbose_name='Дата операции')),
                ('quantity', models.IntegerField(verbose_name='Количество товара')),
                ('price', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Цена товара')),
                ('total_sum', models.DecimalField(decimal_places=2, max_digits=12, verbose_name='Итоговая сумма')),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='sklad.customer', verbose_name='Покупатель')),
                ('operation', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='sklad.operation', verbose_name='Операция')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='sklad.prod', verbose_name='Товар')),
                ('warehouse', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='sklad.warehouse', verbose_name='Склад')),
            ],
            options={
                'verbose_name': 'Операция',
                'verbose_name_plural': 'Операции',
                'ordering': ['-date'],
            },
        ),
        migrations.AddField(
            model_name='operation',
            name='operation_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='sklad.operationtype', verbose_name='Тип операции'),
        ),
    ]
