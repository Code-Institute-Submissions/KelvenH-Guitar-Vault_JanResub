from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_guitars, name='guitars'),
    path('<int:guitar_id>/', views.guitar_detail, name='guitar_detail'),
]
