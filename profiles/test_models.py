from django.contrib.auth.models import User
from django.test import TestCase
from .models import UserProfile

# Create your tests here.


class ProfileModelTestCase(TestCase):
    """
    Test profile model object creation
    """

    def setUp(self):
        self.user = User.objects.create(username="TestUser", password="12345")
        self.user_profile = UserProfile.objects.get(id=self.user.id)
        self.user_profile.default_address_one = "Test Address Line 1"
        self.user_profile.default_address_two = "Test Address Line 2"
        self.user_profile.default_town_city = "Test City"
        self.user_profile.default_postcode = "AA99 9AA"
        self.user_profile.default_phone_number = "07123123123"
        self.user_profile.default_county = "Test County"
        self.user_profile.default_country = "UK"
        self.user_profile.save()

    def test_userprofile_exists(self):
        users_count = UserProfile.objects.all().count()
        self.assertEqual(users_count, 1)

    def test_userprofile_username_correct(self):
        self.assertEqual(self.user_profile.user.username, "TestUser")

    def test_userprofile_password_correct(self):
        self.assertEqual(self.user_profile.user.password, "12345")

    def test_userprofile_address_line_one_correct(self):
        self.assertEqual(self.user_profile.default_address_one,
                         "Test Address Line 1")

    def test_userprofile_address_line_two_correct(self):
        self.assertEqual(self.user_profile.default_address_two,
                         "Test Address Line 2")

    def test_userprofile_town_city_correct(self):
        self.assertEqual(self.user_profile.default_town_city, "Test City")

    def test_userprofile_model_string_name(self):
        self.assertEqual(str(self.user_profile), "TestUser - TestUser")


class ProfileModelMethodTestCase(TestCase):
    """
    Test profile model method
    """

    def test_userprofile_is_zero(self):
        user_count = User.objects.all().count()
        user_profile_count = UserProfile.objects.all().count()
        self.assertEqual(user_count, 0)
        self.assertEqual(user_profile_count, 0)

    def test_one_user_created_and_user_profile_created(self):
        user = User.objects.create(username="TestUser", password="12345")
        user_count = User.objects.all().count()
        self.assertEqual(user.username, "TestUser")
        self.assertEqual(user_count, 1)
        user_profile_count = UserProfile.objects.all().count()
        self.assertEqual(user_profile_count, 1)
