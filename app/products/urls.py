from django.urls import path
from .views.read_view import ReadAPIView


urlpatterns = [
    path('v1/products/all/', ReadAPIView.as_view(), name='all-products'),
]