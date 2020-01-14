from django.contrib.auth.models import User
from django.test import TestCase
from users.models import UserInfo

class TestUserInfoModel(TestCase):
    def setUp(self):
        self.user = User.objects.create(
            first_name="John", last_name="Doe", password="password123"
        )
        self.UserInfo = UserInfo.objects.create(
            user=self.user, age=15, have_siblings="No", known_env_exposures="Blah", known_genetic_mutations="Blah Blah"
        )

    def test_model_field_types(self):
        """
        test that the model has recieved the right data types
        """
        self.assertTrue(isinstance(self.UserInfo.have_siblings, str))
        self.assertTrue(isinstance(self.UserInfo.known_env_exposures, str))
        self.assertTrue(isinstance(self.UserInfo.known_genetic_mutations, str))
        self.assertTrue(isinstance(self.UserInfo.age, int))
