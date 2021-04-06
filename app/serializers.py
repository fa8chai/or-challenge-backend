from rest_framework import serializers
from .models import *

class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):    
    images = ImageSerializer(many=True, read_only=True)
    class Meta:
        model = Product
        fields = '__all__'
        
class CategorySerializer(serializers.ModelSerializer):
    products = ProductSerializer(many=True, read_only=True)

    class Meta:
        model = Category
        fields = '__all__'


class OrderUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderUser
        fields = '__all__'

class OrderSerializer(serializers.ModelSerializer):
    product = ProductSerializer()
    order_user = OrderUserSerializer()
    class Meta:
        model = Order
        fields = '__all__'
    def create(self, validated_data):
        product_data = validated_data.pop('product')
        order_user_data = validated_data.pop('order_user')
        product = Product.objects.get(**product_data)
        order_user = OrderUser.objects.get_or_create(**order_user_data)
        order = Order.objects.create(product=product, order_user=order_user, **validated_data)
        return order