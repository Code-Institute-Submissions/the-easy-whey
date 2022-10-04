# from django.test import TestCase
# from django.test import Client
# from django.contrib.auth.models import User
# from subscription.models import Order
# from .models import UserProfile

# # Create your tests here.


# class ProfileURLTestCaseNonLoggedInUser(TestCase):
#     """
#     Test urls are returning appropriate responses,
#     non-logged in users get redirected and if order is not theirs
#     """
#     def setUp(self):
#         self.c = Client()
#         self.my_user = User.objects.create_user('my_user', 'my_user@my_user.com', "my_userpass")
#         self.user_profile = UserProfile.objects.all().first()
#         self.order = Order.objects.create(user_profile=self.user_profile)

#     def test_url_profile(self):
#         response = self.c.get('/profile')
#         self.assertEqual(response.status_code, 301)

#     def test_url_profile_created_orderer_is_self(self):
#         response = self.c.get(f'/profile/{self.order.order_number}')
#         self.assertEqual(response.status_code, 302)

# class ProfileURLTestCaseLoggedInUser(TestCase):
#     """
#     Test urls are returning appropriate responses,
#     logged in users arent redirected unless order is not theirs
#     """
#     def setUp(self):
#         self.c = Client()
#         self.my_user = User.objects.create_user('my_user', 'my_user@my_user.com', "my_userpass")
#         self.user_profile = UserProfile.objects.all().first()
#         self.order = Order.objects.create(user_profile=self.user_profile)
#         self.user_profile.default_address_one = "Test Address Line 1"
#         self.user_profile.default_address_two = "Test Address Line 2"
#         self.user_profile.default_town_city = "Test City"
#         self.user_profile.default_postcode = "AA99 9AA"
#         self.user_profile.default_phone_number = "07123123123"
#         self.user_profile.default_county = "Test County"
#         self.user_profile.default_country = "UK"
#         self.user_profile.save()
#         self.c.login(username=self.my_user.username, password="my_userpass")

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















# # class ProductsURLTestCaseSuperUser(TestCase):
# #     """
# #     Test urls are returning appropriate responses - superuser
# #     """

# #     def setUp(self):
# #         self.c = Client()
# #         self.my_admin = User.objects.create_superuser('myuser', 'testemail@email.com', "password")
# #         self.c.login(username=self.my_admin.username, password="password")
# #         self.product = Product.objects.create(
# #             flavour="Tasty Flavour",
# #             description="Tasty Flavour Description",
# #             price=6.99
# #         )
# #         self.nutrition = Nutrition.objects.create(
# #             product=self.product,
# #             energy=400,
# #             fat=10,
# #             carbohydrate=10,
# #             sugars=10,
# #             protein=80,
# #             salt=0.5
# #         )
# #         self.ingredient_one = Ingredient.objects.create(
# #             product=self.product,
# #             name="Tasty Ingredient 1"
# #         )
# #         self.ingredient_two = Ingredient.objects.create(
# #             product=self.product,
# #             name="Tasty Ingredient 2"
# #         )

# #     def test_url_product_admin(self):
# #         response = self.c.get('/product/admin/')
# #         self.assertEqual(response.status_code, 200)
# #         self.assertContains(response, "Admin Product Management")
# #         self.assertContains(response, "Use below links to either add a new product")

# #     def test_url_product_admin_add_product(self):
# #         pre_total = Product.objects.all().count()
# #         response = self.c.post('/product/admin/add/', {
# #             "flavour": "Added Flavour",
# #             "description": "Added Flavour Description",
# #             "price": 699,
# #             "product_form_submit_button": "product_form_submit_button"
# #         })
# #         post_total = Product.objects.all().count()
# #         item = Product.objects.get(flavour="Added Flavour")
# #         self.assertEqual(item.flavour, "Added Flavour")
# #         self.assertEqual(item.description, "Added Flavour Description")
# #         self.assertEqual(item.price, 699)
# #         self.assertEqual(pre_total, 1)
# #         self.assertEqual(post_total, 2)

# #     def test_url_product_admin_add_nutrition(self):
# #         self.product_two = Product.objects.create(
# #             flavour="Tasty Flavour",
# #             description="Tasty Flavour Description",
# #             price=6.99
# #         )
# #         pre_total = Nutrition.objects.all().count()
# #         response = self.c.post('/product/admin/add/', {
# #             "product": self.product_two.id,
# #             "energy": 500,
# #             "fat": 9,
# #             "carbohydrate": 9,
# #             "sugars": 9,
# #             "protein": 90,
# #             "salt": 0.4,
# #             "nutrition_form_submit_button": "nutrition_form_submit_button"
# #         })
# #         post_total = Nutrition.objects.all().count()
# #         item = Nutrition.objects.get(product=self.product_two.id)
# #         self.assertEqual(item.product, self.product_two)
# #         self.assertEqual(item.energy, 500)
# #         self.assertEqual(item.fat, 9)
# #         self.assertEqual(item.carbohydrate, 9)
# #         self.assertEqual(item.sugars, 9)
# #         self.assertEqual(item.protein, 90)
# #         self.assertEqual(item.salt, 0.4)
# #         self.assertEqual(pre_total, 1)
# #         self.assertEqual(post_total, 2)

# #     def test_url_product_admin_add_ingredient(self):
# #         self.product_three = Product.objects.create(
# #             flavour="Last Tasty Flavour",
# #             description="Last Tasty Flavour Description",
# #             price=6.99
# #         )
# #         pre_total = Ingredient.objects.all().count()
# #         response = self.c.post('/product/admin/add/', {
# #             "product": self.product_three.id,
# #             "name": "Last Ingredient",
# #             "ingredient_form_submit_button": "ingredient_form_submit_button"
# #         })
# #         post_total = Ingredient.objects.all().count()
# #         item = Ingredient.objects.all().last()
# #         self.assertEqual(item.product, self.product_three)
# #         self.assertEqual(item.name, "Last Ingredient")
# #         self.assertEqual(pre_total, 2)
# #         self.assertEqual(post_total, 3)

# #     def test_url_product_admin_edit_page(self):
# #         response = self.c.get('/product/admin/edit/')
# #         self.assertEqual(response.status_code, 200)
# #         self.assertContains(response, "Edit or Delete Products")

# #     def test_url_product_admin_edit_product(self):
# #         self.assertEqual(self.product.flavour, "Tasty Flavour")
# #         response = self.c.post('/product/admin/edit/item/1', {
# #             "flavour": "Edit Tasty Flavour",
# #             "description": "Edit Tasty Flavour Description",
# #             "price": 799,
# #             "product_form_edit_button": "product_form_edit_button"
# #         })
# #         item = Product.objects.all().first()
# #         self.assertEqual(item.flavour, "Edit Tasty Flavour")