from django.urls import path
from interface import views


app_name = 'interface'
urlpatterns = [
    path('', views.menus, name='menus'),
    path('make/vote/<int:menu_id>/', views.make_vote, name='make_vote'),
    path('messages/info/', views.messages_info, name='messages_info'),
    path('profile/', views.profile, name='profile'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('register/', views.register, name='register'),
]
