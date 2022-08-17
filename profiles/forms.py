# from django import forms
# from allauth.account.forms import SignupForm

# class CustomSignupForm(SignupForm):
#     first_name = forms.CharField(required=True)
#     last_name = forms.CharField(required=True)

# this put the fields onto the form, not sure what happens if it gets filled in though
# also needs this is settings : ACCOUNT_FORMS = {'signup': 'profiles.forms.CustomSignupForm',}