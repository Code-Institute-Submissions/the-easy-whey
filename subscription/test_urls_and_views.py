from django.test import TestCase
from django.test import Client
from django.contrib.auth.models import User
from products.models import Product
from subscription.models import Order
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
        content = "Easy Whey to help you reach and maintain your goals!"
        self.assertContains(response, content)

    def test_url_order_details(self):
        response = self.c.get('/order/details/')
        self.assertEqual(response.status_code, 302)

    def test_url_order_items(self):
        response = self.c.get('/order/items/')
        self.assertEqual(response.status_code, 302)

    def test_url_order_payment_no_order_in_session(self):
        User.objects.create_user(
            'my_user',
            'my_user@my_user.com',
            "my_userpass"
        )
        user_profile = UserProfile.objects.all().first()
        Order.objects.create(
            user_profile=user_profile,
            full_name="Test Name",
            email="test@test.com",
            phone_number="07123123123",
            address_one="Address Line 1",
            address_two="Address Line 1",
            postcode="NP11 1AA",
            town_city="TestCity",
            county="TestCounty",
            country="GB",
            date=datetime.datetime.now(),
            total_cost=0,
        )
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
        content = "Easy Whey to help you reach and maintain your goals!"
        self.assertContains(response, content)

    def test_url_order_stripe_cancel(self):
        session = self.c.session
        session["checkout_key"] = False
        session.save()
        response = self.c.get('/stripe-cancel', follow=True)
        self.assertEqual(response.redirect_chain[0][1], 302)
        self.assertEqual(response.redirect_chain[0][0], "/order/")
        self.assertContains(response, "Why Order?")
        content = "Easy Whey to help you reach and maintain your goals!"
        self.assertContains(response, content)


class OrderURLTestCaseLoggedInUser(TestCase):
    """
    Test urls are returning appropriate responses,
    """

    def setUp(self):
        self.c = Client()
        self.new_user = User.objects.create_user(
            'new_user',
            'new_user@new_user.com',
            "new_userpass"
        )
        self.user_profile = UserProfile.objects.all().first()
        self.c.login(username="new_user", password="new_userpass")
        self.order = Order.objects.create(
            user_profile=self.user_profile,
            full_name="Test Name",
            email="test@test.com",
            phone_number="07123123123",
            address_one="Address Line 1",
            address_two="Address Line 1",
            postcode="NP11 1AA",
            town_city="TestCity",
            county="TestCounty",
            country="GB",
            date=datetime.datetime.now(),
            total_cost=0,
        )
        self.product_choc = Product.objects.create(
            flavour="Chocolate Whey Protein",
            description="Chocolate Yum Description",
            price=6.99
        )
        self.product_banana = Product.objects.create(
            flavour="Banana Whey Protein",
            description="Banana Yum Description",
            price=6.99
        )
        self.product_strawb = Product.objects.create(
            flavour="Strawberry Whey Protein",
            description="Strawberry Yum Description",
            price=6.99
        )
        self.product_c_and_c = Product.objects.create(
            flavour="Cookies & Cream Whey Protein",
            description="Cookies Yum Description",
            price=6.99
        )

    def test_url_order_redirects_to_order_details(self):
        response = self.c.get('/order/', follow=True)
        self.assertRedirects(response, '/order/details/')
        self.assertContains(response, "Your Details")
        self.assertTemplateUsed(response, "order/order_details.html")

    def test_url_order_details_submission(self):
        pre_order_count = Order.objects.all().count()
        self.assertEqual(pre_order_count, 1)
        response = self.c.post('/order/details/', {
            "full_name": "Test Name Post",
            "email": "testpost@test.com",
            "phone_number": "07789789789",
            "address_one": "Address Line A",
            "address_two": "Address Line B",
            "postcode": "NP11 1BB",
            "town_city": "Test City",
            "county": "Test County",
            "country": "GB",
            "save_information": False,
        }, follow=True)
        post_order_count = Order.objects.all().count()
        self.assertEqual(post_order_count, 2)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "order/order_items.html")
        self.assertContains(response, "Please note, all bags weigh 500g.")

    def test_url_order_save_info_checkbox_checked(self):
        user = UserProfile.objects.get(id=self.new_user.id)
        self.assertEqual(user.default_address_one, None)
        self.assertEqual(user.default_address_two, None)
        response = self.c.post('/order/details/', {
            "full_name": "Test Name Post",
            "email": "testpost@test.com",
            "phone_number": "07789789789",
            "address_one": "Address Line A",
            "address_two": "Address Line B",
            "postcode": "NP11 1BB",
            "town_city": "Test City",
            "county": "Test County",
            "country": "GB",
            "save_information": True,
        }, follow=True)
        session = self.c.session
        session["save_information"] = True
        session.save()
        self.assertEqual(Order.objects.all().count(), 2)
        user = UserProfile.objects.get(id=self.new_user.id)
        self.assertEqual(user.default_address_one, "Address Line A")
        self.assertEqual(user.default_address_two, "Address Line B")

    def test_url_order_items_no_session_id(self):
        response = self.c.get('/order/items/', follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertRedirects(response, "/order/details/")

    def test_url_order_items_with_session_id(self):
        session = self.c.session
        session["order_number"] = "fake_order_number"
        session.save()
        response = self.c.get('/order/items/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "order/order_items.html")
        self.assertContains(response, "Please note, all bags weigh 500g.")

    def test_url_order_items_submission(self):
        session = self.c.session
        session["order_number"] = self.order.order_number
        session.save()
        response = self.c.post('/order/items/', {
            "chocolate_quantity": 2,
            "banana_quantity": 0,
            "strawberry_quantity": 0,
            "cookies_and_cream_quantity": 0,
        })
        order = Order.objects.get(id=self.order.id)
        self.assertEqual(order.lineitems.all()[0].quantity, 2)
        self.assertEqual(order.lineitems.all()[1].quantity, 0)
        self.assertEqual(order.lineitems.all()[2].quantity, 0)
        self.assertEqual(order.lineitems.all()[3].quantity, 0)
        self.assertEqual(float(order.total_cost), 13.98)

    def test_url_order_payment_session_present(self):
        order_number = Order.objects.first().order_number
        session = self.c.session
        session["order_number"] = order_number
        session.save()
        response = self.c.get('/order/payment/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Payment")
        self.assertTemplateUsed(response, "order/payment.html")

    def test_create_checkout_session_redirects(self):
        response = self.c.get('/create-checkout-session', follow=True)
        self.assertRedirects(response, "/order/details/")
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "An error occured, please try again.")
        self.assertTemplateUsed(response, "order/order_details.html")

    def test_stripe_success_response_updates_database(self):
        session = self.c.session
        session["checkout_key"] = True
        session["order_number"] = self.order.order_number
        session.save()
        response = self.c.get('/stripe-success')
        order = Order.objects.get(id=self.order.id)
        self.assertEqual(order.user_profile, self.user_profile)
        self.assertEqual(order.is_paid, True)
        self.assertTemplateUsed(response, "order/success.html")

    def test_stripe_cancel_response_updates_database(self):
        session = self.c.session
        session["checkout_key"] = True
        session["order_number"] = self.order.order_number
        session.save()
        response = self.c.get('/stripe-cancel')
        order = Order.objects.get(id=self.order.id)
        self.assertEqual(order.user_profile, self.user_profile)
        self.assertEqual(order.is_paid, False)
        self.assertTemplateUsed(response, "order/cancel.html")

    def test_url_order_try_again(self):
        User.objects.create_user(
            'my_user',
            'my_user@my_user.com',
            "my_userpass"
        )
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
        self.assertEqual(pre_order_count, 2)
        self.assertEqual(post_order_count, 1)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.redirect_chain[0][1], 302)
        self.assertEqual(response.redirect_chain[0][0], "/order/")
