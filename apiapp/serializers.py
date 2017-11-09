from rest_framework.serializers import ModelSerializer
from . import models


class ProductSerializer(ModelSerializer):
    class Meta:
        model = models.Product
        fields = '__all__'


class CategorySerializer(ModelSerializer):
    #products = ProductSerializer(many=True)
    class Meta:
        model = models.Category
        fields = ('id', 'name', 'products')
