from django.shortcuts import render
from django.http import HttpRequest
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .serializers import MenuItemsSerializer, UserSerializer
from .models import Menu
from django.contrib.auth.models import User
# Create your views here.


def restaurant_view(request: HttpRequest):
    return render(request, 'index.html', {})


class MenuItemView(ListCreateAPIView):
    serializer_class = MenuItemsSerializer
    queryset = Menu.objects.all()


class SingleMenuItemView(RetrieveUpdateDestroyAPIView):
    serializer_class = MenuItemsSerializer
    queryset = Menu.objects.all()
