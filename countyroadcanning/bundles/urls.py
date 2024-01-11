from django.urls import path
from . import views

urlpatterns = [
    path('', views.bundles, name='bundles'),
    path('<int:bundle_id>', views.bundle_page, name='bundle_page'),
]