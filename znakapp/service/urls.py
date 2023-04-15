from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='homepage'),
    path('how-it-work/', views.how_it_work, name='how-it-work'),
    path('price-list/', views.price_list, name='price-list'),
    path('contacts/', views.contacts, name='contacts'),
    path('login/cabinet/<str:user_id>', views.cabinet, name='cabinet'),
    path('login/', views.user_login, name='login'),
    path('register/', views.register_request, name='register'),
    path('logout/', views.user_logout, name='logout'),
]