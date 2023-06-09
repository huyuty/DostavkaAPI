# Generated by Django 4.1.7 on 2023-05-04 03:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DishMenu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dish_name', models.CharField(max_length=70, verbose_name='Наименование блюда')),
                ('ingredients', models.CharField(max_length=120, verbose_name='Ингридиенты')),
                ('price', models.DecimalField(decimal_places=2, max_digits=6, verbose_name='Цена')),
            ],
            options={
                'verbose_name_plural': 'Menu',
            },
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total_cost', models.DecimalField(decimal_places=2, max_digits=7, verbose_name='Итоговая стоимость')),
            ],
        ),
        migrations.CreateModel(
            name='Rest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rest_name', models.CharField(max_length=50, verbose_name='Наименование ресторана')),
                ('address', models.CharField(max_length=100, verbose_name='Адрес')),
                ('description', models.CharField(max_length=200, verbose_name='Описание')),
            ],
            options={
                'verbose_name_plural': 'restaurant',
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_address', models.CharField(max_length=50, verbose_name='Адрес пользователя')),
                ('phone_user', models.CharField(max_length=30, verbose_name='Номер пользователя')),
            ],
            options={
                'verbose_name_plural': 'User',
            },
        ),
        migrations.CreateModel(
            name='ProductOrder',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dish_name_order', models.CharField(max_length=70, verbose_name='Наименование блюда')),
                ('count', models.IntegerField(max_length=20, verbose_name='Количество')),
                ('price_order', models.DecimalField(decimal_places=2, max_digits=7, verbose_name='Цена')),
                ('dish', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Dostavka.dishmenu', verbose_name='Блюда')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Dostavka.order', verbose_name='Заказ')),
            ],
        ),
        migrations.AddField(
            model_name='order',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Dostavka.user', verbose_name='Пользователь'),
        ),
        migrations.AddField(
            model_name='dishmenu',
            name='rest',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Dostavka.rest', verbose_name='Ресторан'),
        ),
        migrations.CreateModel(
            name='Courier',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='Имя')),
                ('transport', models.CharField(max_length=20, verbose_name='Транспорт')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Dostavka.order', verbose_name='Заказ')),
            ],
        ),
    ]
