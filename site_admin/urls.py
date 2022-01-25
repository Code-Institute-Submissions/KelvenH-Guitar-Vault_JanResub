from django.urls import path
from . import views

urlpatterns = [
    path('', views.site_admin, name='site_admin'),
    path('listguitars/', views.GuitarList.as_view(), name='guitarlist'),
    path('addguitars/', views.add_guitar, name='add_guitar'),
    path('editguitars/<int:guitar_id>/', views.edit_guitar, name='edit_guitar'),
    path('deleteguitars/<int:guitar_id>/', views.delete_guitar, name='delete_guitar'),
    path('listorders/', views.OrderList.as_view(), name='orderlist'),
    path('addorders/', views.add_order, name='add_order'),
    path('editorders/<int:order_id>/', views.edit_order, name='edit_order'),
    path('deleteorders/<int:order_id>/', views.delete_order, name='delete_order'),
]
