from django.contrib.auth.models import User
from django.test import TestCase
from products.models import Product
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
        self.product_one = Product.objects.create(
            flavour="Yum Yum",
            description="Yum Yum Description",
            price=6.99
        )
        self.item_one = OrderLineItem.objects.create(
            order=self.order,
            product=self.product_one,
            quantity=2,
        )

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
        self.assertEqual(float(self.order.total_cost), 13.98)

    def test_order_model_string_name(self):
        self.assertEqual(str(self.order), self.order.order_number)

    def test_order_is_paid_is_false_by_default(self):
        self.assertEqual(self.order.is_paid, False)

    def test_order_line_item_added_to_order(self):
        order_item_item = self.order.lineitems.all().count()
        self.assertEqual(order_item_item, 1)

    def test_order_line_item_added_is_correct_name(self):
        line_item_name = self.order.lineitems.all().first().product.flavour
        self.assertEqual(line_item_name, "Yum Yum")

    def test_order_line_item_added_is_correct_price(self):
        line_item_cost = self.order.lineitems.all().first().product_total
        self.assertEqual(float(line_item_cost), 13.98)

    def test_order_line_item_save_method(self):
        self.item_one.quantity = 3
        self.item_one.save()
        line_item_cost = self.order.lineitems.all().first().product_total
        self.assertEqual(float(line_item_cost), 20.97)

    def test_order_line_item_model_string_name(self):
        self.assertEqual(str(self.item_one), f"Product: Yum Yum order: {self.order.order_number}")