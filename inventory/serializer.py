from rest_framework import serializers
from .models import *

class Products_Serializer(serializers.ModelSerializer):

    class Meta:

        model = Products
        fields = '__all__'


class Products_Serializer2(serializers.ModelSerializer):

    class Meta:

        model = Products
        fields = ['product_name']


class Category_Serializer(serializers.ModelSerializer):
    class Meta:

        model = Category
        fields = '__all__'