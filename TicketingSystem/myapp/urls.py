from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('register/', views.registerpage, name="register"),
    path('login/', views.loginpage, name="login"),
    path('logout/', views.logoutUser, name="logout"),
    path('', views.loginpage, name="login"),
    path('dashboard/', views.dashBoard, name="dashboard"),

    
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
    path('password_reset/', auth_views.PasswordResetView.as_view(template_name='accounts/password_reset.html'), name='password_reset'),
    path('password_reset_done/', auth_views.PasswordResetDoneView.as_view(template_name='accounts/password_reset_done.html'), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='accounts/password_reset_confirm.html'), name='password_reset_confirm'),
    path('reset_done/', auth_views.PasswordResetCompleteView.as_view(template_name='accounts/password_reset_complete.html'), name='password_reset_complete'),

    #------------ (CREATE URLS) ------------
    path('create_order/', views.createOrder, name="create_order"),
   
    #------------ (UPDATE URLS) ------------
    path('update_order/<str:pk>/', views.updateOrder, name="update_order"),


    #------------ (UPDATE URLS) ------------
    path('delete_order/<str:pk>/', views.deleteOrder, name="delete_order"),

]