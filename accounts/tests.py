from django.test import TestCase
from .models import User, Role


class RoleModelTest(TestCase):
    def setUp(self):
        self.role = Role(
            role = "USER"
            )
        
    def test_model_can_create_user(self):
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
