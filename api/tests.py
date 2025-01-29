from django.test import TestCase
from api.models import Restaurant, Menu, Vote, Employee
from django.utils.timezone import now


class VotingTestCase(TestCase):
    def setUp(self):
        self.user = Employee.objects.create_user(username="testuser", password="password")
        self.restaurant = Restaurant.objects.create(name="Test Restaurant")
        self.menu = Menu.objects.create(restaurant=self.restaurant, date=now().date(), items={"Pizza": "Cheese Pizza"})

    def test_vote_creation(self):
        vote = Vote.objects.create(employee=self.user, menu=self.menu)
        self.assertEqual(vote.menu, self.menu)
