from django.test import TestCase
from django.test import Client
from .models import Product, Nutrition, Ingredient
from .forms import ProductForm, NutritionForm, IngredientForm
# Create your tests here.


class ProductModelTestCase(TestCase):
    """
    Test product model object creation
    """
    def setUp(self):
        self.product = Product.objects.create(
            flavour="Tasty Flavour",
            description="Tasty Flavour Description",
            price=9.99
        )

    def test_product_exists_and_is_correct(self):
        product_count = Product.objects.all().count()
        self.assertEqual(product_count, 1)
        self.assertEqual(self.product.flavour, "Tasty Flavour")
        self.assertEqual(self.product.description, "Tasty Flavour Description")
        self.assertEqual(self.product.price, 9.99)

    def test_product_price_default_is_699(self):
        new_product = Product.objects.create(
            flavour="Tasty Flavour V2",
            description="Tasty Flavour Description V2",
        )
        self.assertEqual(new_product.price, "6.99")

    def test_product_price_model_constraint_too_big(self):
        price_product = Product.objects.create(
            flavour="Tasty Flavour V3",
            description="Tasty Flavour Description V3",
            price=999999
        )
        item = Product.objects.all().count()
        self.assertEqual(item, 1) # should remain 1 due to setup

    def test_product_price_model_constraint_too_small(self):
        price_product = Product.objects.create(
            flavour="Tasty Flavour V3",
            description="Tasty Flavour Description V3",
            price=9
        )
        item = Product.objects.all().count()
        self.assertEqual(item, 1) # should remain 1 due to setup


    def test_product_model_string_name(self):
        self.assertEqual(str(self.product), "Flavour: Tasty Flavour")





# class NutritionModelTestCase(TestCase):
#     """
#     Test product model object creation
#     """
#     def setUp(self):
#         self.contact_message = Contact.objects.create(
#             name="TestName",
#             email="testemail@email.com",
#             phone_number="07123123123",
#             message="Test message."
#         )

#     def test_message_details_name(self):
#         self.assertEqual(self.contact_message.name, "TestName")


# class IngredientModelTestCase(TestCase):
#     """
#     Test product model object creation
#     """
#     def setUp(self):
#         self.contact_message = Contact.objects.create(
#             name="TestName",
#             email="testemail@email.com",
#             phone_number="07123123123",
#             message="Test message."
#         )

#     def test_message_details_name(self):
#         self.assertEqual(self.contact_message.name, "TestName")