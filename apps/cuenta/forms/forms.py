from django                     import forms
from django.contrib.auth.forms  import AuthenticationForm
from apps.cuenta.models         import User

class SignInForm(AuthenticationForm):

    class Meta:
        model 	= User
        fields 	= ('username', 'password')
