from django.shortcuts import render
from rest_framework.decorators import detail_route, list_route
from rest_framework.generics import ListAPIView, CreateAPIView, UpdateAPIView, DestroyAPIView, RetrieveAPIView

from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from . import serializers
from . import models


class ProductViewSet(ModelViewSet):
    """Info!"""
    serializer_class = serializers.ProductSerializer
    queryset = models.Product.objects.all()


class CategoryViewSet(ModelViewSet):
    """Info2!"""
    serializer_class = serializers.CategorySerializer
    queryset = models.Category.objects.all()


class ProductCreateAPIView(CreateAPIView, ListAPIView):
    permission_classes = (IsAuthenticatedOrReadOnly,)
    serializer_class = serializers.ProductSerializer
    model = models.Product
    queryset = models.Product.objects.all()

    def get_queryset(self, *args, **kwargs):
        return models.Product.objects.all()


class ProductUpdateAPIView(UpdateAPIView, DestroyAPIView, RetrieveAPIView):
    serializer_class = serializers.ProductSerializer
    model = models.Product
    queryset = models.Product.objects.all()


class CategoryCreateAPIView(ListAPIView, CreateAPIView):

    serializer_class = serializers.CategorySerializer
    model = models.Category
    queryset = models.Category.objects.all()


class CategoryUpdateAPIView(UpdateAPIView, DestroyAPIView, RetrieveAPIView):
    serializer_class = serializers.CategorySerializer
    model = models.Category
    queryset = models.Category.objects.all()
