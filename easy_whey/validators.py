from django.core.validators import RegexValidator

phone_error_message = 'Phone number must be entered in the format: 07xxxxxxxxx'
phone_regex = RegexValidator(regex=r"^(07)\d{9}$", message=phone_error_message)
