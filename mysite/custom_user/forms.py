from __future__ import unicode_literals
from django import forms
from django.contrib.auth import get_user_model
from django.utils.translation import ugettext_lazy as _


User = get_user_model()

class EmailUserCreateForm(forms.ModelForm):
    password1 = forms.CharField(widget=forms.PasswordInput)
    password2 = forms.CharField(widget=forms.PasswordInput,
                                help_text=_('Enter the same password as above, for verification.'))
    
    class Meta:
        model = User
        fields = ['email', 'name']
        
    def clean_password2(self):
        password1 = self.cleaned_data['password1']
        password2 = self.cleaned_data['password2']
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords Don't Match")
        return password2
        
    def save(self, commit=True):
        user = super(EmailUserCreateForm, self).save(commit=False)
        password = self.cleaned_data['password1']
        user.set_password(password)
        if commit:
            user.save()
        return user
    
    
class UserLoginForm(forms.Form):
    email = forms.EmailField(widget=forms.widgets.TextInput)
    password = forms.CharField(widget=forms.PasswordInput)
    
    
class EmailTestForm(forms.Form):
    email = forms.EmailField(widget=forms.widgets.TextInput)