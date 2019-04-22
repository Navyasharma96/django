from django import forms
from .models import register,about,UserModel

class SignUpForm(forms.ModelForm):
    class Meta:
        model = UserModel
        fields=['email','username','name','password']




class register_form(forms.ModelForm):
    class Meta:
        model=register
        fields=['Name','Phno','DOB','Adress','Qualification','Email','Password']

class bio_form(forms.ModelForm):
    class Meta:
        model=about
        fields=['INTREST','Hobbies','Bio']