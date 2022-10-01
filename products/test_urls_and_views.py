from django.test import TestCase
from django.test import Client
from django.contrib.auth.models import User
from .models import Product, Nutrition, Ingredient
from .forms import ProductForm, NutritionForm, IngredientForm

# Create your tests here.


class ProductsURLTestCaseNonSuperUser(TestCase):
    """
    Test urls are returning appropriate responses - non superuser,
    non-super users get redirected
    """
    def setUp(self):
        self.c = Client()

    def test_url_home(self):
        response = self.c.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Making protein easy.")

    def test_url_product_admin(self):
        response = self.c.get('/product/admin/')
        self.assertEqual(response.status_code, 302)

    def test_url_admin_add(self):
        response = self.c.get('/product/admin/add/')
        self.assertEqual(response.status_code, 302)

    def test_url_admin_edit(self):
        response = self.c.get('/product/admin/edit/')
        self.assertEqual(response.status_code, 302)

    def test_url_admin_edit_item_product_or_nutrition(self):
        response = self.c.get('/product/admin/edit/item/1')
        self.assertEqual(response.status_code, 302)

    def test_url_admin_edit_item_ingredient(self):
        response = self.c.get('/product/admin/edit/item/1/ingredient/1')
        self.assertEqual(response.status_code, 302)

    def test_url_admin_edit_delete_product(self):
        response = self.c.get('/product/admin/edit/delete/1')
        self.assertEqual(response.status_code, 302)

    def test_url_admin_edit_delete_ingredient(self):
        response = self.c.get('/product/admin/edit/item/delete_ingredient/1')
        self.assertEqual(response.status_code, 302)


class ProductsURLTestCaseSuperUser(TestCase):
    """
    Test urls are returning appropriate responses - superuser
    """

    def setUp(self):
        self.c = Client()
        self.my_admin = User.objects.create_superuser('myuser', 'testemail@email.com', "password")
        self.c.login(username=self.my_admin.username, password="password")
        self.product = Product.objects.create(
            flavour="Tasty Flavour",
            description="Tasty Flavour Description",
            price=6.99
        )
        self.nutrition = Nutrition.objects.create(
            product=self.product,
            energy=400,
            fat=10,
            carbohydrate=10,
            sugars=10,
            protein=80,
            salt=0.5
        )
        self.ingredient_one = Ingredient.objects.create(
            product=self.product,
            name="Tasty Ingredient 1"
        )
        self.ingredient_two = Ingredient.objects.create(
            product=self.product,
            name="Tasty Ingredient 2"
        )

    def test_url_product_admin(self):
        response = self.c.get('/product/admin/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Admin Product Management")
        self.assertContains(response, "Use below links to either add a new product")

    def test_url_product_admin_add_product(self):
        pre_total = Product.objects.all().count()
        response = self.c.post('/product/admin/add/', {
            "flavour": "Added Flavour",
            "description": "Added Flavour Description",
            "price": 699,
            "product_form_submit_button": "product_form_submit_button"
        })
        post_total = Product.objects.all().count()
        item = Product.objects.get(flavour="Added Flavour")
        self.assertEqual(item.flavour, "Added Flavour")
        self.assertEqual(item.description, "Added Flavour Description")
        self.assertEqual(item.price, 699)
        self.assertEqual(pre_total, 1)
        self.assertEqual(post_total, 2)

    def test_url_product_admin_add_nutrition(self):
        self.product_two = Product.objects.create(
            flavour="Tasty Flavour",
            description="Tasty Flavour Description",
            price=6.99
        )
        pre_total = Nutrition.objects.all().count()
        response = self.c.post('/product/admin/add/', {
            "product": self.product_two.id,
            "energy": 500,
            "fat": 9,
            "carbohydrate": 9,
            "sugars": 9,
            "protein": 90,
            "salt": 0.4,
            "nutrition_form_submit_button": "nutrition_form_submit_button"
        })
        post_total = Nutrition.objects.all().count()
        item = Nutrition.objects.get(product=self.product_two.id)
        self.assertEqual(item.product, self.product_two)
        self.assertEqual(item.energy, 500)
        self.assertEqual(item.fat, 9)
        self.assertEqual(item.carbohydrate, 9)
        self.assertEqual(item.sugars, 9)
        self.assertEqual(item.protein, 90)
        self.assertEqual(item.salt, 0.4)
        self.assertEqual(pre_total, 1)
        self.assertEqual(post_total, 2)

    def test_url_product_admin_add_ingredient(self):
        self.product_three = Product.objects.create(
            flavour="Last Tasty Flavour",
            description="Last Tasty Flavour Description",
            price=6.99
        )
        pre_total = Ingredient.objects.all().count()
        response = self.c.post('/product/admin/add/', {
            "product": self.product_three.id,
            "name": "Last Ingredient",
            "ingredient_form_submit_button": "ingredient_form_submit_button"
        })
        post_total = Ingredient.objects.all().count()
        item = Ingredient.objects.all().last()
        self.assertEqual(item.product, self.product_three)
        self.assertEqual(item.name, "Last Ingredient")
        self.assertEqual(pre_total, 2)
        self.assertEqual(post_total, 3)

    def test_url_product_admin_edit_page(self):
        response = self.c.get('/product/admin/edit/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Edit or Delete Products")

    def test_url_product_admin_edit_product(self):
        self.assertEqual(self.product.flavour, "Tasty Flavour")
        response = self.c.post('/product/admin/edit/item/1', {
            "flavour": "Edit Tasty Flavour",
            "description": "Edit Tasty Flavour Description",
            "price": 799,
            "product_form_edit_button": "product_form_edit_button"
        })
        item = Product.objects.all().first()
        self.assertEqual(item.flavour, "Edit Tasty Flavour")

    def test_url_product_admin_edit_nutrition(self):
        self.assertEqual(self.nutrition.energy, 400)
        self.assertEqual(self.nutrition.protein, 80)
        response = self.c.post('/product/admin/edit/item/1', {
            "product": 1,
            "energy": 500,
            "fat": 9,
            "carbohydrate": 9,
            "sugars": 9,
            "protein": 90,
            "salt": 0.4,
            "nutrition_form_edit_button": "nutrition_form_edit_button"
        }, follow=True)
        item = Nutrition.objects.get(product_id=1)
        self.assertEqual(item.energy, 500)
        self.assertEqual(item.protein, 90)

    def test_url_product_admin_edit_ingredient(self):
        self.assertEqual(self.ingredient_one.name, "Tasty Ingredient 1")
        response = self.c.post(f'/product/admin/edit/item/1/ingredient/{self.ingredient_one.id}', {
            "name": "Edit Ingredient 1",
        })
        item = Product.objects.get(id=1)
        self.assertEqual(item.ingredient.first().name, "Edit Ingredient 1")
