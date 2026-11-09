from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('tickets/create/', views.ticket_create, name='ticket_create'),
    path('tickets/list/', views.ticket_list, name='ticket_list'),
    path('tickets/<int:id>/', views.ticket_detail, name='ticket_detail'),
]