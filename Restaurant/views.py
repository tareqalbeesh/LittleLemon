from django.shortcuts import render
from django.http import HttpRequest
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .serializers import MenuItemsSerializer, UserSerializer, BookingSerializer
from .models import Menu, Booking
from django.contrib.auth.models import User
from rest_framework.viewsets import ModelViewSet
# Create your views here.


def restaurant_view(request: HttpRequest):
    return render(request, 'index.html', {})


class MenuItemView(ListCreateAPIView):
    serializer_class = MenuItemsSerializer
    queryset = Menu.objects.all()


class SingleMenuItemView(RetrieveUpdateDestroyAPIView):
    serializer_class = MenuItemsSerializer
    queryset = Menu.objects.all()


class BookingViewSet(ModelViewSet):
    serializer_class = BookingSerializer
    queryset = Booking.objects.all()
