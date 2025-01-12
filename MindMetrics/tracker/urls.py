from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view, name='home'), 
    path('login/', views.login_view, name='login'),
    path('register/', views.register_view, name='register'),
    path('logout/', views.logout_view, name='logout'),
    path('quesstionaire/', views.quesstionaire_view, name='quesstionaire'),
    path('quesstionaire_submit/', views.quesstionaire_submit, name='quesstionaire_submit'),
    path('data_visulize/', views.visulize_view, name='data_visulize'),
]