from django.urls import path
from . import views

urlpatterns = [
    path('', views.checkout, name='cart'),
    path('<int:cart_id>', views.CreateCheckoutSessionView.as_view(), name='cart_page'),
]