from rest_framework.serializers import ModelSerializer
from Dostavka.models import *


class DishMenuSerializer(ModelSerializer):
    class Meta:
        model = DishMenu
        fields = ('dish_name', 'price')


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ('phone_user',)


class ProductOrderSerializer(ModelSerializer):
    class Meta:
        model = ProductOrder
        fields = ('dish', 'count', 'order')


class OrderSerializer(ModelSerializer):
    class Meta:
        model = Order
        fields = ('user', 'total_cost')


class CourierSerializer(ModelSerializer):
    class Meta:
        model = Courier
        fields = ('order', 'name')

class RestSerializer(ModelSerializer):
    class Meta:
        model = Rest
        fields = ('rest_name', 'address', 'description')


