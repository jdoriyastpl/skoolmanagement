import datetime
from django import forms
from django.contrib.auth import authenticate
from django.contrib.auth.forms import UserCreationForm
from account.models import User
from rolepermissions.roles import assign_role
from django import forms


class UserLoginForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)

    def clean(self, *args, **kwargs):
        email = self.cleaned_data.get("email")
        password = self.cleaned_data.get("password")

        if email and password:
            user = authenticate(email=email, password=password)
            if not user:
                raise forms.ValidationError("User Does Not Exist.")
            if not user.check_password(password):
                raise forms.ValidationError("Password Does not Match.")
            if not user.is_active:
                raise forms.ValidationError("User is not Active.")

        return super(UserLoginForm, self).clean(*args, **kwargs)

class UserRegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ("first_name",
                  "last_name",
                  "username",
                  "email",
                  "role",
                  "phone",
                  "picture",
                  "password1",
                  "password2" )

    def save(self, commit=True):
        user = super(UserCreationForm, self).save(commit=False)
        user.username = self.cleaned_data['username']
        user.email = self.cleaned_data['email']
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.phone = self.cleaned_data['phone']
        user.role = self.cleaned_data['role']
        if commit:
            assign_role(user, user.role)
            user.save()
        return user


class UserProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ("first_name",
                  "last_name",
                  "email",
                  "phone",
                  "picture",
                  "institute_name",
                  "phone",
                  "address")


class PasswordResetRequestForm(forms.Form):
    email_or_username = forms.CharField(label=("Email Or Username"), max_length=254)


class SetPasswordForm(forms.Form):
    """
    A form that lets a user change set their password without entering the old
    password
    """
    error_messages = {
        'password_mismatch': ("The two password fields didn't match."),
        }
    new_password1 = forms.CharField(label=("New password"),
                                    widget=forms.PasswordInput)
    new_password2 = forms.CharField(label=("New password confirmation"),
                                    widget=forms.PasswordInput)

    def clean_new_password2(self):
        password1 = self.cleaned_data.get('new_password1')
        password2 = self.cleaned_data.get('new_password2')
        if password1 and password2:
            if password1 != password2:
                raise forms.ValidationError(
                    self.error_messages['password_mismatch'],
                    code='password_mismatch',
                    )
        return password2
