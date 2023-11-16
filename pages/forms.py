# label
# initial
# disabled
# help_text
# widget
# required

from django import forms
from .models import Login

class LoginForm(forms.ModelForm):
    
    class Meta:
        
        model = Login
        fields = '__all__'
        # fields = ['field_name'] if you want spicial field
        
        
    