from django.urls import path
from app_api import views

urlpatterns = [
    path('hello/', views.HelloApiView.as_view())
]
