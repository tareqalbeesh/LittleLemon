from django.urls import path
from .views import restaurant_view, SingleMenuItemView, MenuItemView, secret_view
from rest_framework.authtoken.views import obtain_auth_token
urlpatterns = [
    path('', restaurant_view),
    path('menu/', MenuItemView.as_view()),
    path('menu/<int:pk>', SingleMenuItemView.as_view()),
    path('secret/', secret_view),
    path('api-token-auth', obtain_auth_token),
]
