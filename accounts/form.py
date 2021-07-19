from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile

class Register_form(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','email','password1','password2','first_name','last_name']

class Profile_form(ModelForm):
    class Meta:
        model = Profile
        fields = ['type','line1','city','state','pincode','profile_pic']

