from django.test import TestCase
from django.test import Client
from django.contrib.auth.models import User
from products.models import Product
from subscription.models import Order, OrderLineItem
from .models import UserProfile
import datetime


# Create your tests here.


class OrderURLTestCaseNonLoggedInUser(TestCase):
    """
    Test urls are returning appropriate responses,
    non-logged in users get redirected if needed
    """
    def setUp(self):
        self.c = Client()

    def test_url_order(self):
        response = self.c.get('/order/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Why Order?")
        self.assertContains(response, "Tasty and Easy Whey to help you reach and maintain your goals!")

    def test_url_order_details(self):
        my_user = User.objects.create_user('my_user', 'my_user@my_user.com', "my_userpass")
        user_profile = UserProfile.objects.all().first()
        response = self.c.get('/order/details/')
        self.assertEqual(response.status_code, 302)

    def test_url_order_items(self):
        response = self.c.get('/order/items/')
        self.assertEqual(response.status_code, 302)

    def test_url_order_payment(self):
        my_user = User.objects.create_user('my_user', 'my_user@my_user.com', "my_userpass")
        user_profile = UserProfile.objects.all().first()
        order = Order.objects.create(
            user_profile=user_profile,
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
        order_number = Order.objects.first().order_number
        # session = self.c.session
        # session["order_number"] = order_number
        # session.save()
        response = self.c.get('/order/payment/')
        self.assertEqual(response.status_code, 302)

    def test_url_order_stripe_success(self):
        session = self.c.session
        session["checkout_key"] = False
        session.save()
        response = self.c.get('/stripe-success', follow=True)
        self.assertEqual(response.redirect_chain[0][1], 302)
        self.assertEqual(response.redirect_chain[0][0], "/order/")
        self.assertContains(response, "Why Order?")
        self.assertContains(response, "Tasty and Easy Whey to help you reach and maintain your goals!")

    def test_url_order_stripe_cancel(self):
        session = self.c.session
        session["checkout_key"] = False
        session.save()
        response = self.c.get('/stripe-cancel', follow=True)
        self.assertEqual(response.redirect_chain[0][1], 302)
        self.assertEqual(response.redirect_chain[0][0], "/order/")
        self.assertContains(response, "Why Order?")
        self.assertContains(response, "Tasty and Easy Whey to help you reach and maintain your goals!")

    def test_url_order_try_again(self):
        my_user = User.objects.create_user('my_user', 'my_user@my_user.com', "my_userpass")
        user_profile = UserProfile.objects.all().first()
        order = Order.objects.create(
            user_profile=user_profile,
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
        session = self.c.session
        session["order_number"] = order.order_number
        session.save()
        pre_order_count = Order.objects.all().count()
        response = self.c.get('/try_again', follow=True)
        post_order_count = Order.objects.all().count()
        self.assertEqual(pre_order_count, 1)
        self.assertEqual(post_order_count, 0)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.redirect_chain[0][1], 302)
        self.assertEqual(response.redirect_chain[0][0], "/order/")

# class OrderURLTestCaseLoggedInUser(TestCase):
#     """
#     Test urls are returning appropriate responses,
#     """
#     def setUp(self):
#         self.c = Client()
#         self.user = User.objects.create(username="TestUser", password="12345")
#         self.user_profile = UserProfile.objects.get(id=self.user.id)
#         order = Order.objects.create(
#             user_profile=self.user_profile,
#             full_name="Test Name",
#             email="test@test.com",
#             phone_number="07123123123",
#             address_one="Address Line 1",
#             address_two="Address Line 1",
#             postcode="NP11 1AA",
#             town_city="TestCity",
#             county="TestCounty",
#             country="TestCountry",
#             date=datetime.datetime.now(),
#             total_cost=0,
#         )
#         self.product_one = Product.objects.create(
#             flavour="Yum Yum",
#             description="Yum Yum Description",
#             price=6.99
#         )
#         self.item_one = OrderLineItem.objects.create(
#             order=self.order,
#             product=self.product_one,
#             quantity=5,
#         )
#         self.c.login(username=self.user.username, password="12345")


# def test_url_order_details(self):
#     self.c.login(username=my_user.username, password="my_userpass")
#     response = self.c.get('/order/details/')
#     self.assertEqual(response.status_code, 301)

# AND IF THBERE IS AN ORDER NUMBER?
    # def test_url_order_payment(self):
    #     order_number = Order.objects.first().order_number
    #     session = self.c.session
    #     session["order_number"] = order_number
    #     session.save()
    #     response = self.c.get('/order/payment/')
    #     self.assertEqual(response.status_code, 302)

#     def test_url_profile(self):
#         response = self.c.get('/profile/')
#         self.assertEqual(response.status_code, 200)
#         self.assertContains(response, "Your Profile")
#         self.assertContains(response, "Edit your delivery details")

#     def test_url_profile_address_info_renders(self):
#         user_profile = UserProfile.objects.all().first()
#         response = self.c.get('/profile/')
#         self.assertEqual(response.status_code, 200)
#         self.assertContains(response, user_profile.default_address_one)
#         self.assertContains(response, user_profile.default_address_two)
#         self.assertContains(response, user_profile.default_phone_number)

#     def test_url_profile_order_orderer_is_self(self):
#         response = self.c.get(f'/profile/{self.order.order_number}')
#         self.assertEqual(response.status_code, 200)
#         self.assertContains(response, "Order Number")
#         self.assertContains(response, "Return to Profile")

#     def test_url_profile_order_orderer_non_self(self):
#         self.client.logout()
#         new_user = User.objects.create_user('new_user', 'new_user@new_user.com', "new_userpass")
#         self.c.login(username=new_user.username, password="new_userpass")
#         response = self.c.get(f'/profile/{self.order.order_number}')
#         self.assertEqual(response.status_code, 302)

#     def test_url_profile_post_method_update_user_info(self):
#         response = self.c.post('/profile/', {
#             "default_address_one": "THIS IS A NEW ADDRESS LINE ONE",
#             "default_postcode": "BB11 1BB",
#             "default_town_city": "LIVERPOOL"
#         })
#         self.assertEqual(response.status_code, 200)
#         response = self.c.get('/profile/')
#         self.assertContains(response, "THIS IS A NEW ADDRESS LINE ONE")
#         self.assertContains(response, "BB11 1BB")
#         self.assertContains(response, "LIVERPOOL")
