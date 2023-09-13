from rest_framework import serializers

from account_module.models import User
from .models import Product, ProductComment


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id','name', 'price', 'count', 'description', 'is_active']

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'first_name', 'last_name', 'total_buy']

class CommentSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    product = ProductSerializer(read_only=True)
    class Meta:
        model = ProductComment
        fields = '__all__'
