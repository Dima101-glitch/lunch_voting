from rest_framework import generics, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from api.models import Restaurant, Menu, Vote, Employee
from api.serializers import RestaurantSerializer, MenuSerializer, EmployeeSerializer, VoteSerializer
from django.utils.timezone import now
from django.db import models


class RegisterEmployeeView(generics.CreateAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    permission_classes = [permissions.AllowAny]


class RestaurantCreateView(generics.CreateAPIView):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer
    permission_classes = [permissions.IsAuthenticated]


class MenuCreateView(generics.CreateAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer
    permission_classes = [permissions.IsAuthenticated]


class CurrentDayMenuView(APIView):
    def get(self, request):
        today = now().date()
        menus = Menu.objects.filter(date=today)
        serializer = MenuSerializer(menus, many=True)
        return Response(serializer.data)


class VoteCreateView(generics.CreateAPIView):
    queryset = Vote.objects.all()
    serializer_class = VoteSerializer
    permission_classes = [permissions.IsAuthenticated]


class VoteResultsView(APIView):
    def get(self, request):
        today = now().date()
        results = (
            Vote.objects.filter(menu__date=today)
            .values('menu__items')
            .annotate(votes=models.Count('id'))
            .order_by('-votes')
        )
        return Response(results)
