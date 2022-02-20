from django.forms import ModelForm

from django import forms
from ..models import Profile
from django.contrib.auth.models import User


class EditProfileForm(ModelForm):

    class Meta:
        model = Profile
        fields = ('bio', 'phone', 'github')


class EditUserForm(ModelForm):
    class Meta:
        model = User
        fields = ('username', 'email')

    username = forms.CharField(max_length=128, disabled=True)
    email = forms.EmailField(disabled=True)
    old_password = forms.CharField(widget=forms.PasswordInput, required=False)
    new_password = forms.CharField(widget=forms.PasswordInput, required=False)
    confirm_password = forms.CharField(widget=forms.PasswordInput, required=False)

    def save(self, commit=True):
        user = super(EditUserForm, self).save(commit=False)
        new_password = self.cleaned_data['new_password']
        if new_password:
            confirm_password = self.cleaned_data['confirm_password']
            check = user.check_password(self.cleaned_data['old_password'])
            if check and new_password == confirm_password:
                user.set_password(new_password)
            else:
                commit = False
                user = None
        if commit:
            user.save()
        return user
