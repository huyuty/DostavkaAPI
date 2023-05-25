from django.db import models


class Rest(models.Model):
    rest_name = models.CharField(verbose_name='Наименование ресторана', max_length=50)
    address = models.CharField(verbose_name='Адрес', max_length=100)
    description = models.CharField(verbose_name='Описание', max_length=200)

    class Meta:
        verbose_name_plural = 'restaurant'

    def __str__(self):
        return f'{self.rest_name} {self.address} {self.description}'


class DishMenu(models.Model):
    rest = models.ForeignKey(Rest, verbose_name='Ресторан', on_delete=models.CASCADE)
    dish_name = models.CharField(verbose_name='Наименование блюда', max_length=70)
    ingredients = models.CharField(verbose_name='Ингридиенты', max_length=120)
    price = models.DecimalField(verbose_name='Цена', decimal_places=2, max_digits=6)

    class Meta:
        verbose_name_plural = 'Menu'

    def __str__(self):
        return f'{self.dish_name} {self.price}'


class User(models.Model):
    user_address = models.CharField(verbose_name='Адрес пользователя', max_length=50)
    phone_user = models.CharField(verbose_name='Номер пользователя', max_length=30)

    class Meta:
        verbose_name_plural = 'User'

    def __str__(self):
        return f'{self.user_address} {self.phone_user}'


class Order(models.Model):
    user = models.ForeignKey(User, verbose_name='Пользователь', on_delete=models.CASCADE)
    total_cost = models.DecimalField(verbose_name='Итоговая стоимость', decimal_places=2, max_digits=7)

    def __str__(self):
        return f'{self.total_cost} {self.user.phone_user}'


class ProductOrder(models.Model):
    dish = models.ForeignKey(DishMenu, verbose_name='Блюда', on_delete=models.CASCADE)
    count = models.IntegerField(verbose_name='Количество')
    # price_order = models.DecimalField(verbose_name='Цена', decimal_places=2, max_digits=7)
    order = models.ForeignKey(Order, verbose_name='Заказ', on_delete=models.CASCADE)

    def __str__(self):
        return f' {self.count} {DishMenu.price_order}'


class Courier(models.Model):
    order = models.ForeignKey(Order, verbose_name='Заказ', on_delete=models.CASCADE)
    name = models.CharField(verbose_name='Имя', max_length=20)
    transport = models.CharField(verbose_name='Транспорт', max_length=20)

    def __str__(self):
        return f'{self.order} {self.name} {self.transport}'