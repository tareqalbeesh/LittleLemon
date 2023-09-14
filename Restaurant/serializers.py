from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Menu


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'groups', 'email']


class MenuItemsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Menu
        fields = '__all__'
