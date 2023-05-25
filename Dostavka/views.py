from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticatedOrReadOnly, AllowAny
from .models import *
from .seriliazators import *

class ProductOrderViewSet(ModelViewSet):
    serializer_class = ProductOrderSerializer
    permission_classes = [AllowAny]
    queryset= ProductOrder.objects.all()

    # @action(methods=['get'], detail=False, url_path='filter-order')
    # def filter_order(self, request):
    #     ord = request.query_params.get('order')
    #     queryset = self.queryset.order_by(order=ord)
    #     data = self.serializer_class(queryset, many=True).data
    #     return Response(data)

    @action(methods=['get'], detail=False, url_path='filter-dish')
    def filter_dish(self, request):
        dish = request.query_params.get('dish_id')
        queryset = self.get_queryset().filter(dish=dish)
        data = self.serializer_class(queryset, many=True).data
        return Response(data)

class UserViewSet(ModelViewSet):
    serializer_class = UserSerializer
    queryset= User.objects.all()

class DishMenuViewSet(ModelViewSet):
    serializer_class = DishMenuSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = DishMenu.objects.all()

    @action(methods=['get'], detail=False, url_path='top-5-dishes')
    def get_five_dishes(self, request):
        queryset = self.queryset.order_by('?')[:5]
        data = self.serializer_class(queryset, many=True).data
        return Response(data)

    @action(methods=['get'], detail=False, url_path='filter-price')
    def filter_price(self, request):
        category = request.query_params.get('price')
        queryset = self.queryset.order_by('price')
        data = self.serializer_class(queryset, many=True).data
        return Response(data)

class CourierViewSet(ModelViewSet):
    serializer_class = CourierSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = Courier.objects.all()

class OrderViewSet(ModelViewSet):
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = Order.objects.all()

class RestViewSet(ModelViewSet):
    serializer_class = RestSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = Rest.objects.all()

    @action(methods=['get'], detail=False, url_path='filter-rest-name')
    def filter_rest_name(self, request):
        rest_name = request.query_params.get('rest_name')
        queryset = self.get_queryset().filter(rest_name=rest_name)
        data = self.serializer_class(queryset, many=True).data
        return Response(data)

    # @action(methods=['get'], detail=False, url_path='top-5-dishes')
    # def get_five_dishes(self, request):
    #     queryset = self.queryset.order_by('dish')[:5]
    #     data = self.serializer_class(queryset, many=True).data
    #     return Response(data)

    # @action(methods=['get'], detail=False, url_path='filter-category')
    # def filter_category(self, request):
    #     category = request.query_params.get('category_id')
    #     queryset = self.get_queryset().filter(category_name=category)
    #     data = self.serializer_class(queryset, many=True).data
    #     return Response(data)

