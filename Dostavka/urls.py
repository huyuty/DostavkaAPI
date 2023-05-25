from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *

router = DefaultRouter()
router.register('Продукты в заказе',ProductOrderViewSet)
router.register('Основной заказ',OrderViewSet)
router.register('Меню',DishMenuViewSet)
router.register('Курьер',CourierViewSet)
router.register('Пользователи',UserViewSet)
router.register('Рестораны',RestViewSet)
urlpatterns = [
    path('api/v1/', include(router.urls)),
]