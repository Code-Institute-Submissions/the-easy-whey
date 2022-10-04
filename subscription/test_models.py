from django.contrib.auth.models import User
from django.test import TestCase
from profiles.models import UserProfile
from .models import Order, OrderLineItem
import datetime

# Create your tests here.


class OrderModelTestCase(TestCase):
    """
    Test order model object creation
    """
    def setUp(self):
        self.user = User.objects.create(username="TestUser", password="12345")
        self.user_profile = UserProfile.objects.get(id=self.user.id)
        self.order = Order.objects.create(
            order_number="1234567890",
            user_profile=self.user_profile,
            full_name="Test Name",
            email="test@test.com",
            phone_number="07123123123",
            address_one="Address Line 1",
            address_two="Address Line 1",
            postcode="NP11 1AA",
            town_city="TestCity",
            county="TestCounty",
            country="TestCountry",
            date=datetime.datetime.now(),
            total_cost=0,
        )

        # for button to save info in order page
        # self.user_profile.default_address_one="Test Address Line 1"
        # self.user_profile.default_address_two="Test Address Line 2"
        # self.user_profile.default_town_city="Test City"
        # self.user_profile.default_postcode="AA99 9AA"
        # self.user_profile.default_phone_number="07123123123"
        # self.user_profile.default_county="Test County"
        # self.user_profile.default_country="UK"
        # self.user_profile.save()


    def test_order_exists(self):
        order_count = Order.objects.all().count()
        self.assertEqual(order_count, 1)

    def test_order_info_full_name(self):
        self.assertEqual(self.order.full_name, "Test Name")

    def test_order_info_phone_number(self):
        self.assertEqual(self.order.phone_number, "07123123123")

    def test_order_info_address_line_one(self):
        self.assertEqual(self.order.address_one, "Address Line 1")

    def test_order_info_town_city(self):
        self.assertEqual(self.order.total_cost, 0)

    def test_order_is_paid_is_false_by_default(self):
        self.assertEqual(self.order.is_paid, False)

    def test_order_model_string_name(self):
        self.assertEqual(str(self.order), "1234567890")


# class OrderLineItemModelTestCase(TestCase):
#     """
#     Test order line item model object creation
#     """
#     def test_userprofile_is_zero(self):
#         user_count = User.objects.all().count()
#         user_profile_count = UserProfile.objects.all().count()
#         self.assertEqual(user_count, 0)
#         self.assertEqual(user_profile_count, 0)

#     def test_one_user_created_and_user_profile_created(self):
#         user = User.objects.create(username="TestUser", password="12345")
#         user_count = User.objects.all().count()
#         self.assertEqual(user.username, "TestUser")
#         self.assertEqual(user_count, 1)
#         user_profile_count = UserProfile.objects.all().count()
#         self.assertEqual(user_profile_count, 1)
