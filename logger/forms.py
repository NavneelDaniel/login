from django import forms
from logger.models import UserProfileInfo
from django.contrib.auth.models import User
class UserForm(forms.ModelForm):
    


    error_messages = {'password_mismatch': ("The two password fields didn't match."),}
    email = forms.EmailField(max_length=200)

    password2 = forms.CharField(label= ("Password confirmation"),widget=forms.PasswordInput, help_text= None)

    
    



    class Meta():
        model = User
        fields = ('username','email','password', 'password2')
        help_texts = {
            'username': None,
            'password' : None,
            'email': None,
        }
class UserProfileInfoForm(forms.ModelForm):



     class Meta():

         model = UserProfileInfo
         fields = ('address',)