from django.test import TestCase
from .models import CustomUser
# Create your tests here.

class UserTestCase(TestCase):
    """Testing the user model to ensure we are returning all necessary values"""

    def setUp(self):
        self.custom_user_name = "Ryan"
        self.custom_user = CustomUser(name=self.user_name)

    def test_model_can_create_user(self):
        """Test if the user model can creat a new user."""
        old_count = User.objects.count()
        self.user.save()
        new_count = User.objects.count()
        self.assertNotEqual(old_count, new_count)


