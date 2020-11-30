from django.urls import path

from .views import FoodApiView

urlpatterns = [
    path('foods/', FoodApiView.as_view())
]