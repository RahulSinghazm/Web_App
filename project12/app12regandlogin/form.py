from django import forms
from . models import Reg

class RegForm(forms.ModelForm):
    class Meta:
        model=Reg
        widgets={'pwd':forms.PasswordInput()}
        fields={'user','pwd','fname','lname','dob','mobno'}
class LoginForm(forms.Form):
    user=forms.CharField(max_length=20)
    pwd=forms.CharField(widget=forms.PasswordInput)