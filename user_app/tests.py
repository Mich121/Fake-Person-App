from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.test import APITestCase
from django.urls import reverse

# Create your tests here.
class RegisterTestAPI(APITestCase):

    def test_register(self):
        data = {
            "username": "testcase",
            "email": "testcase@gm.com",
            "password": "testcase88",
            "password2": "testcase88"
        }
        response = self.client.post(reverse('register1'), data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

class LogTestAPI(APITestCase):

    def setUp(self):
        self.user = User.objects.create(username='testcase', password='testcase88')

    def test_login(self):
        data = {
            "username": self.user.username,
            "password": self.user.password
        }
        response = self.client.post(reverse('login'), data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_logout(self):
        self.token = Token.objects.get(user__username=self.user.username)
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)
        response = self.client.post(reverse('logout'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)


