from django.urls import URLPattern, path
from . import views

urlpatterns = [
    path('dashboard/', views.index, name='dashboard-index'),
    path('staff/', views.staff, name='dashboard-staff'),
    path('products/', views.products, name='dashboard-products'),
    path('order/', views.order, name='dashboard-order'),
]
