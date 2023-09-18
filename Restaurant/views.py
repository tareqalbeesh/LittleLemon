from django.shortcuts import render
from django.http import HttpRequest
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .serializers import MenuItemsSerializer, UserSerializer, BookingSerializer
from .models import Menu, Booking
from django.contrib.auth.models import User
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
# Create your views here.


def restaurant_view(request: HttpRequest):
    return render(request, 'index.html', {})


class MenuItemView(ListCreateAPIView):
    serializer_class = MenuItemsSerializer
    queryset = Menu.objects.all()
    permission_classes = [IsAuthenticated]


class SingleMenuItemView(RetrieveUpdateDestroyAPIView):
    serializer_class = MenuItemsSerializer
    queryset = Menu.objects.all()
    permission_classes = [IsAuthenticated]


class BookingViewSet(ModelViewSet):
    serializer_class = BookingSerializer
    queryset = Booking.objects.all()
    permission_classes = [IsAuthenticated]


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def secret_view(request):
    return Response({'Response': 'this is a protected view'})
