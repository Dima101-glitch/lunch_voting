from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from api.views import (
    RegisterEmployeeView, RestaurantCreateView, MenuCreateView,
    CurrentDayMenuView, VoteCreateView, VoteResultsView
)

urlpatterns = [
    path('register/', RegisterEmployeeView.as_view(), name='register'),
    path('restaurants/', RestaurantCreateView.as_view(), name='create-restaurant'),
    path('menus/', MenuCreateView.as_view(), name='create-menu'),
    path('menus/today/', CurrentDayMenuView.as_view(), name='current-day-menu'),
    path('votes/', VoteCreateView.as_view(), name='create-vote'),
    path('votes/results/', VoteResultsView.as_view(), name='vote-results'),
    path('token/', TokenObtainPairView.as_view(), name='token'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token-refresh'),
]
