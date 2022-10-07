from django.test import TestCase
from django.test import Client
from .models import Contact
# Create your tests here.


class ModelTestCase(TestCase):
    """
    Test contact model object creation
    """

    def setUp(self):
        self.contact_message = Contact.objects.create(
            name="TestName",
            email="testemail@email.com",
            phone_number="07123123123",
            message="Test message."
        )

    def test_message_details_name(self):
        self.assertEqual(self.contact_message.name, "TestName")

    def test_message_details_email(self):
        self.assertEqual(self.contact_message.email, "testemail@email.com")

    def test_message_details_phone_number(self):
        self.assertEqual(self.contact_message.phone_number, "07123123123")

    def test_message_details_message(self):
        self.assertEqual(self.contact_message.message, "Test message.")

    def test_model_string_name(self):
        self.assertEqual(str(self.contact_message),
                         "Message received from TestName, testemail@email.com")

    def test_model_phone_number_invalid(self):
        c = Client()
        response = c.post('/contact/', {
            'name': 'TestName',
            'email': 'testemail@email.com',
            'phone_number': '0712312312',
            'message': 'Test message.',
            }
        )
        errors = response.context["form"].errors
        message = "Phone number must be entered in the format: 07xxxxxxxxx"
        self.assertEqual(errors["phone_number"][0], message)
