from django.test import TestCase
from django.test import Client
from django.contrib.auth.models import User
from subscription.models import Order
from .models import UserProfile

# Create your tests here.


class ProfileURLTestCaseNonLoggedInUser(TestCase):
    """
    Test urls are returning appropriate responses,
    non-logged in users get redirected and if order is not theirs
    """
    def setUp(self):
        self.c = Client()
        self.my_user = User.objects.create_user('my_user', 'my_user@my_user.com', "my_userpass")
        self.user_profile = UserProfile.objects.all().first()
        self.order = Order.objects.create(user_profile=self.user_profile)

    def test_url_profile(self):
        response = self.c.get('/profile')
        self.assertEqual(response.status_code, 301)

    def test_url_profile_created_orderer_is_self(self):
        response = self.c.get(f'/profile/{self.order.order_number}')
        self.assertEqual(response.status_code, 302)

class ProfileURLTestCaseLoggedInUser(TestCase):
    """
    Test urls are returning appropriate responses,
    logged in users arent redirected unless order is not theirs
    """
    def setUp(self):
        self.c = Client()
        self.my_user = User.objects.create_user('my_user', 'my_user@my_user.com', "my_userpass")
        self.user_profile = UserProfile.objects.all().first()
        self.order = Order.objects.create(user_profile=self.user_profile)
        self.user_profile.default_address_one = "Test Address Line 1"
        self.user_profile.default_address_two = "Test Address Line 2"
        self.user_profile.default_town_city = "Test City"
        self.user_profile.default_postcode = "AA99 9AA"
        self.user_profile.default_phone_number = "07123123123"
        self.user_profile.default_county = "Test County"
        self.user_profile.default_country = "UK"
        self.user_profile.save()
        self.c.login(username=self.my_user.username, password="my_userpass")

    def test_url_profile(self):
        response = self.c.get('/profile/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Your Profile")
        self.assertContains(response, "Edit your delivery details")

    def test_url_profile_address_info_renders(self):
        user_profile = UserProfile.objects.all().first()
        response = self.c.get('/profile/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, user_profile.default_address_one)
        self.assertContains(response, user_profile.default_address_two)
        self.assertContains(response, user_profile.default_phone_number)

    def test_url_profile_order_orderer_is_self(self):
        response = self.c.get(f'/profile/{self.order.order_number}')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Order Number")
        self.assertContains(response, "Return to Profile")

    def test_url_profile_order_orderer_non_self(self):
        self.client.logout()
        new_user = User.objects.create_user('new_user', 'new_user@new_user.com', "new_userpass")
        self.c.login(username=new_user.username, password="new_userpass")
        response = self.c.get(f'/profile/{self.order.order_number}')
        self.assertEqual(response.status_code, 302)

    def test_url_profile_post_method_update_user_info(self):
        response = self.c.post('/profile/', {
            "default_address_one": "THIS IS A NEW ADDRESS LINE ONE",
            "default_postcode": "BB11 1BB",
            "default_town_city": "LIVERPOOL"
        })
        self.assertEqual(response.status_code, 200)
        response = self.c.get('/profile/')
        self.assertContains(response, "THIS IS A NEW ADDRESS LINE ONE")
        self.assertContains(response, "BB11 1BB")
        self.assertContains(response, "LIVERPOOL")