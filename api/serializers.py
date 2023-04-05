from rest_framework import serializers
from .models import Customer,Product

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model=Customer
        fields='__all__'


class ProductSerializer(serializers.ModelSerializer):

    product_image=serializers.ImageField(required=False)
    class Meta:
        model=Product
        fields='__all__'

    

    