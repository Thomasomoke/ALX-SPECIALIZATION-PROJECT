from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.registerpage, name="register"),
    path('login/', views.loginpage, name="login"),
    path('logout/', views.logoutUser, name="logout"),
    path('', views.dashBoard, name="dashboard"),
    path('products/', views.products, name="products"),
    path('customer/<str:pk>/', views.customer, name="customer"),
    path('create_booking/', views.create_booking, name='create_booking'),
    path('create_event/', views.create_event, name='create_event'),
    path('events/', views.event_list, name='event_list'),
    path('events/<int:pk>/', views.event_detail, name='event_detail'),  # Detail view for an event
    path('bookings/', views.booking_list, name='booking_list'),
    path('bookings/<int:event_pk>/', views.booking_list, name='booking_list_by_event'),
    path('bookings/delete/', views.delete_booking, name='delete_booking'),
    path('create_ticket_category/', views.create_ticket_category, name='create_ticket_category'),

    #------------ (CREATE URLS) ------------
    path('create_order/', views.createOrder, name="create_order"),
   
    #------------ (UPDATE URLS) ------------
    path('update_order/<str:pk>/', views.updateOrder, name="update_order"),


    #------------ (UPDATE URLS) ------------
    path('delete_order/<str:pk>/', views.deleteOrder, name="delete_order"),

]