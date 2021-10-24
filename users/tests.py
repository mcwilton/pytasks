from django.test import TestCase
from django.contrib.auth.models import User

class Profile(TestCase):

	def test_profile(self):
		user = User(
			email = "user@email.com",
			username = "user",
			password = "123456?",
			
		)
		user.save()

		self.assertFalse(
			hasattr(user, 'profile')
			)
