from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view, name='home'),
    path('post/<int:pk>/', views.tpost_detail, name='tpost')
]