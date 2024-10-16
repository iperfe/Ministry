from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission

class Church(models.Model):
    name = models.CharField(max_length=255)
    country = models.CharField(max_length=255)
    address = models.TextField()
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=20)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class Contribution(models.Model):
    church = models.ForeignKey(Church, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    contributor = models.CharField(max_length=255)
    contribution_date = models.DateField()
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.church.name} - {self.contributor} - {self.amount}"

class Request(models.Model):
    church = models.ForeignKey(Church, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.TextField()
    amount_requested = models.DecimalField(max_digits=10, decimal_places=2)
    deadline = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class Donation(models.Model):
    church = models.ForeignKey(Church, on_delete=models.CASCADE)
    request = models.ForeignKey(Request, on_delete=models.CASCADE)
    amount_donated = models.DecimalField(max_digits=10, decimal_places=2)
    donation_date = models.DateField()
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.church.name} - {self.request.title} - {self.amount_donated}"


class User(AbstractUser ):
    church = models.ForeignKey(Church, on_delete=models.CASCADE, null=True, blank=True)
    role = models.CharField(max_length=20, choices=[
        ('admin', 'Admin'),
        ('church_admin', 'Church Admin'),
        ('user', 'User ')
    ])
     # Adding related_name to avoid clashes
    groups = models.ManyToManyField(
        Group,
        related_name='custom_user_set',  # Custom related name for groups
        blank=True,
    )
    user_permissions = models.ManyToManyField(
        Permission,
        related_name='custom_user_set',  # Custom related name for user permissions
        blank=True,
    )
    def __str__(self):
        return self.username