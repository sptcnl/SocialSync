from django.test import TestCase
from .models import User, Role, UserRole

from rest_framework.test import APIClient
from rest_framework import status

class ModelTest(TestCase):
    class RoleModelTest(TestCase):
        def setUp(self):
            self.role = Role(
                role = "USER"
                )

        def test_model_can_create_role(self):
            old_count = Role.objects.count()
            self.role.save()
            new_count = Role.objects.count()
            self.assertNotEqual(old_count, new_count)


    class UserModelTest(TestCase):
        def setUp(self):
            self.user_username = "test"
            self.user_password = "testpw123"
            self.user_nickname = "test"
            self.user = User(
                username = self.user_username,
                password = self.user_password,
                nickname = self.user_nickname,
                )

        def test_model_can_create_user(self):
            old_count = User.objects.count()
            self.user.save()
            new_count = User.objects.count()
            self.assertNotEqual(old_count, new_count)

    
    class UserRoleTest(TestCase):
        def setUp(self):
            user_role, created = Role.objects.get_or_create(role='USER')
            self.user_role = UserRole(
                user = User.objects.filter(username="test"),
                role = user_role
                )

        def test_model_can_create_user_role(self):
            old_count = UserRole.objects.count()
            self.user_role.save()
            new_count = UserRole.objects.count()
            self.assertNotEqual(old_count, new_count)

class ViewTest(TestCase):
    class SignupViewTest(TestCase):
        def setUp(self):
            self.client = APIClient()
            self.user_data = {
                "username" : "test",
                "password" : "testpw123",
                "nickname" : "test",
            }
            self.response = self.client.post('/accounts/signup/',
                                            self.user_data,
                                            format="json")

        def test_api_can_create_user(self):
            self.assertEqual(self.response.status_code, status.HTTP_201_CREATED)


    class LoginViewTest(TestCase):
        def setUp(self):
            self.client = APIClient()
            self.user_data = {
                "username" : "test",
                "password" : "testpw123",
            }
            self.response = self.client.post('/accounts/login/',
                                            self.user_data,
                                            format="json")

        def test_api_can_login(self):
            self.assertEqual(self.response.status_code, status.HTTP_200_OK)