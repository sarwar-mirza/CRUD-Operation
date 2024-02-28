from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UsernameField, PasswordChangeForm
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _
from django.contrib.auth import password_validation
from .models import Picture

# Create Signup Form using Class based  
class SignUpForm(UserCreationForm):             # inherit UserCreationForm
    
    password1 = forms.CharField(
        label=_("Password"),
        strip=False,
        error_messages={'required': 'Enter your Password'},
        widget=forms.PasswordInput(attrs={"autocomplete": "new-password", "class":"form-control", "placeholder": "Password"}),
        help_text=password_validation.password_validators_help_text_html(),
    )
    password2 = forms.CharField(
        label=_("Confirm password(again)"),
        error_messages={'required': 'Re-Enter Password'},
        widget=forms.PasswordInput(attrs={"autocomplete": "new-password", "class":"form-control", "placeholder": "Re-Enter password"}),
        strip=False,
        help_text=_("Enter the same password as before, for verification."),
    )
    class Meta:
        model = User            # Database used Default Django model [database- SQLite-3]
        fields = ['username', 'first_name', 'last_name', 'email']   
        
        # Custom labels [Override]
        labels = {
            'email': 'Email',
        }
        
        # Custom error messages [Override]
        error_messages = {
            'username': {'required': 'Enter your Username'},
            'email': {'required': 'Enter your Email'},
        }
        
        # Custom widget [Override]
        widgets = {
            'username': forms.TextInput(attrs={"class": "form-control", "placeholder": "Username"}),
            'first_name': forms.TextInput(attrs={"class": "form-control", "placeholder": "First Name"}),
            'last_name': forms.TextInput(attrs={"class": "form-control", "placeholder": "Last Name"}),
            'email': forms.EmailInput(attrs={"class": "form-control", "placeholder": "@gmail.com"}),            
        }


# Create Login Form inherit AuthenticationForm using class based 
class LoginAuthenticationForm(AuthenticationForm):
    username = UsernameField(
        error_messages={'required': 'Enter your username'},
        widget=forms.TextInput(attrs={"autofocus": True, "class": "form-control", "placeholder": "Username"}))
    password = forms.CharField(
        label=_("Password"),
        strip=False,
        error_messages={'required':'Enter your password'},
        widget=forms.PasswordInput(attrs={"autocomplete": "current-password", "class": "form-control", "placeholder": "Password"}),
    )



# Create change passwor Form inherit PasswordChangeForm
class ChangePasswordForm(PasswordChangeForm):
    old_password = forms.CharField(
        label=_("Old password"),
        strip=False,
        error_messages={'required':'Enter your old password'},
        widget=forms.PasswordInput(
            attrs={"autocomplete": "current-password", "autofocus": True, "class":"form-control", "placeholder": "Old Password"}
        ),
    )
    
    new_password1 = forms.CharField(
        label=_("New password"),
        error_messages={'required':'Enter your new password'},
        widget=forms.PasswordInput(attrs={"autocomplete": "new-password", "class":"form-control", "placeholder": "New Password"}),
        strip=False,
        help_text=password_validation.password_validators_help_text_html(),
    )
    new_password2 = forms.CharField(
        label=_("Confirm password(again)"),
        strip=False,
        error_messages={'required':'Re-enter Password'},
        widget=forms.PasswordInput(attrs={"autocomplete": "new-password", "class":"form-control", "placeholder": "Confirm password(again)"}),
    )



# Image uploader form
class ImageUploaderForm(forms.ModelForm):
    class Meta:
        model = Picture
        fields = ['title', 'description', 'product_pic']
        
        labels = {
            'product_pic': 'Upload Image',
        }
        
        error_messages = {
            'title': {'required': 'Enter Your Title'},
            'description': {'required': 'Enter Your Description'},
            'product_pic': {'required': 'Enter Your Upload Image'},
        }
        
        widgets = {
            'title': forms.TextInput(attrs={"class": "form-control", "placeholder":"Title"}),
            'description': forms.Textarea(attrs={"class": "form-control", "placeholder": "Write now description..."}),
            'product_pic': forms.FileInput(attrs={"class": "form-control", "placeholder": "Image Uploader"})
        }