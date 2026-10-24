from django import forms
from .models import Account,UserProfile
import re

class RegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder':'Enter password'
        
    }))
    confirm_password = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder':'Confirm password'
    }))
    
    class Meta:
        model = Account
        fields = ['first_name','last_name','phone_number','email','password']
    
    def __init__(self,*args,**kwargs):
        super(RegistrationForm,self).__init__(*args,**kwargs)
        self.fields['first_name'].widget.attrs['placeholder'] = 'Enter first name'
        self.fields['last_name'].widget.attrs['placeholder'] = 'Enter last name'
        self.fields['phone_number'].widget.attrs['placeholder'] = 'Enter phone number'
        self.fields['email'].widget.attrs['placeholder'] = 'Enter email address'
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'

    def clean(self):
        cleaned_data = super(RegistrationForm, self).clean()
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')
        if password != confirm_password:
            raise forms.ValidationError("Password and Conform Password are not same.")

    def clean_first_name(self):
        first_name = self.cleaned_data.get('first_name')

        if first_name and len(first_name) < 4:
            raise forms.ValidationError(
                'First name cannot be less than 4 characters.'
            )

        return first_name

    def clean_last_name(self):
        last_name = self.cleaned_data.get('last_name')

        if last_name and len(last_name) < 4:
            raise forms.ValidationError(
                'last name cannot be less than 4 characters.'
            )

        return last_name

    def clean_phone_number(self):
        phone_number = self.cleaned_data.get('phone_number')

        if phone_number and len(phone_number) < 10:
            raise forms.ValidationError(
                'phone number cannot be less than 10 characters.'
            )

        return phone_number
    
    def clean_email(self):
        email = self.cleaned_data.get('email')
        pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        valid = re.match(pattern, email)
        if not valid:
            raise forms.ValidationError(
                'please enter valid email address.'
            )

        return email
    
    def clean_password(self):
        password = self.cleaned_data.get('password')
        SpecialSym = ['$', '@', '#', '%']
        val = True
        # Check length
        if len(password) < 6:
            raise forms.ValidationError('Length should be at least 6')
            val = False
        if len(password) > 20:
            raise forms.ValidationError('Length should not be greater than 20')
            val = False
        # Check for digits
        if not any(char.isdigit() for char in password):
            raise forms.ValidationError('Password should have at least one numeral')
            val = False
        # Check for uppercase letters
        if not any(char.isupper() for char in password):
            raise forms.ValidationError('Password should have at least one uppercase letter')
            val = False
        # Check for lowercase letters
        if not any(char.islower() for char in password):
            raise forms.ValidationError('Password should have at least one lowercase letter')
            val = False
        # Check for special symbols
        if not any(char in SpecialSym for char in password):
            raise forms.ValidationError('Password should have at least one of the symbols $@#%')
            val = False

        return password




class Userform(forms.ModelForm):
    class Meta:
        model = Account
        fields = ('first_name','last_name','phone_number')
    def __init__(self,*args,**kwargs):
        super(Userform,self).__init__(*args,**kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'

class UserProfileForm(forms.ModelForm):
    profile_picture = forms.ImageField(required=False,error_messages={'invalid':("Image files only")},widget=forms.FileInput)
    class Meta:
        model = UserProfile
        fields = ('address_line_1','address_line_2','profile_picture','city','country','state')

    def __init__(self,*args,**kwargs):
        super(UserProfileForm,self).__init__(*args,**kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'

