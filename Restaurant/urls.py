from django.urls import path
from .views import restaurant_view, SingleMenuItemView, MenuItemView
urlpatterns = [
    path('', restaurant_view),
    path('menu/', MenuItemView.as_view()),
    path('menu/<int:pk>', SingleMenuItemView.as_view()),
]
