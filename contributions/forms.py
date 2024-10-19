from django import forms
from .models import Church, Contribution, Request, Donation
from .models import User

class CustomUserCreationForm(forms.ModelForm):
    password1 = forms.CharField(widget=forms.PasswordInput, label='Password')
    password2 = forms.CharField(widget=forms.PasswordInput, label='Confirm Password')
    
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2', 'church', 'role')

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")
        return password2


class ChurchForm(forms.ModelForm):
    class Meta:
        model = Church
        fields = ['name', 'country', 'address', 'email', 'phone_number', 'description']

class ContributionForm(forms.ModelForm):
    class Meta:
        model = Contribution
        fields = ['amount', 'contributor', 'contribution_date', 'description']

class RequestForm(forms.ModelForm):
    class Meta:
        model = Request
        fields = ['title', 'description', 'amount_requested', 'deadline']

class DonationForm(forms.ModelForm):
    class Meta:
        model = Donation
        fields = ['amount_donated', 'donation_date', 'description']
