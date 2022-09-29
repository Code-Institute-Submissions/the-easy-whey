from django.test import TestCase
from django.test import Client
from django.contrib.auth.models import User
from .models import Contact

# Create your tests here.


class ContactURLTestCaseNonSuperUser(TestCase):
    """
    Test urls are returning appropriate responses - non superuser,
    non-super users get redirected to login page
    """
    def setUp(self):
        self.c = Client()

    def test_url_contact(self):
        response = self.c.get('/contact/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Please fill out the form below.")

    def test_url_contact_admin(self):
        response = self.c.get('/contact/admin/')
        self.assertEqual(response.status_code, 302)

    def test_url_contact_admin_message(self):
        response = self.c.get('/contact/admin/1')
        self.assertEqual(response.status_code, 302)

    def test_url_contact_admin_delete(self):
        response = self.c.get('/contact/admin/delete/1')
        self.assertEqual(response.status_code, 302)
    

class ContactURLTestCaseSuperUser(TestCase):
    """
    Test urls are returning appropriate responses - superuser
    """

    def setUp(self):
        self.c = Client()
        self.my_admin = User.objects.create_superuser('myuser', 'testemail@email.com', "password")
        self.c.login(username=self.my_admin.username, password="password")

    def test_url_contact_admin_no_messages(self):
        response = self.c.get('/contact/admin/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "There are no messages!")
        self.assertNotContains(response, "From")

    def test_url_contact_admin_with_message(self):
        self.contact_message = Contact.objects.create(
            name="TestName",
            email="testemail@email.com",
            phone_number="07123123123",
            message="Test message."
        )
        response = self.c.get('/contact/admin/')
        self.assertContains(response, "TestName")
        self.assertContains(response, "testemail@email.com")
        self.assertContains(response, "Utilities")

    def test_url_contact_admin_with_message_view_message(self):
        self.contact_message = Contact.objects.create(
            name="TestName",
            email="testemail@email.com",
            phone_number="07123123123",
            message="Test message."
        )
        response = self.c.get(f'/contact/admin/{self.contact_message.id}')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Message from:</strong> TestName.")
        self.assertContains(response, "Email:</strong> testemail@email.com.")
        self.assertContains(response, "Phone:</strong> 07123123123")
        msg = "Message:</strong></p>\n                <p>Test message."
        self.assertContains(response, msg)

    def test_url_contact_admin_create_message(self):
        pre_total = Contact.objects.all().count()
        response = self.c.post('/contact/', {
            'name': 'TestNameCreateMessage',
            'email': 'testemailCreateMessage@email.com',
            'phone_number': '07123123123',
            'message': 'Test message, create message.',
            }
        )
        post_total = Contact.objects.all().count()
        contact = Contact.objects.get(name="TestNameCreateMessage")
        self.assertEqual(pre_total, 0)
        self.assertEqual(post_total, 1)
        self.assertEqual(contact.name, "TestNameCreateMessage")
        self.assertEqual(contact.email, "testemailCreateMessage@email.com")
        self.assertEqual(contact.phone_number, "07123123123")
        self.assertEqual(contact.message, "Test message, create message.")

    def test_url_contact_admin_delete_message(self):
        pre_total = Contact.objects.all().count()
        self.contact_message = Contact.objects.create(
            name="TestNameDelete",
            email="testemaildelete@email.com",
            phone_number="07123123123",
            message="Test message delete."
        )
        post_total = Contact.objects.all().count()
        response = self.c.get(f'/contact/admin/delete/{self.contact_message.id}')
        post_delete_total = Contact.objects.all().count()
        self.assertEqual(pre_total, 0)
        self.assertEqual(post_total, 1)
        self.assertEqual(post_delete_total, 0)
