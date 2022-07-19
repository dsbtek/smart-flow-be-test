from django.db import models
from users.models import User

# Create your models here.
class Kyc(models.Model):
    status_choices = [
        ('Done', 'Done'),
        ('Not Done', 'Not Done'),
    ]
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True,)
    location = models.CharField(max_length=100,)
    customer_name = models.CharField(max_length=100,)
    amount_paid = models.CharField(max_length=100,)
    volume_dispensed = models.IntegerField()
    status = models.CharField(max_length=50, choices=status_choices,)