
from django.contrib import admin
from .models import Church, Contribution, Request, Donation,User
from django.contrib import admin


admin.site.register(User)

@admin.register(Church)
class ChurchAdmin(admin.ModelAdmin):
    list_display = ['name', 'country', 'email']

@admin.register(Contribution)
class ContributionAdmin(admin.ModelAdmin):
    list_display = ['church', 'contributor', 'amount', 'contribution_date']

@admin.register(Request)
class RequestAdmin(admin.ModelAdmin):
    list_display = ['church', 'title', 'amount_requested', 'deadline']

@admin.register(Donation)
class DonationAdmin(admin.ModelAdmin):
    list_display = ['church', 'request', 'amount_donated', 'donation_date']
