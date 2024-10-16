from django import forms
from .models import Church, Contribution, Request, Donation


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
