from django.db import models
from datetime import datetime
from .user import User
from .category import Category

class Expense(models.Model):
    EXPENSE_TYPES = [
        ('FIXED', 'Fixed'),
        ('RECURRING', 'Recurring'),
    ]
    RECURRING_FREQUENCIES = [
        ('DAILY', 'Daily'),
        ('WEEKLY', 'Weekly'),
        ('MONTHLY', 'Monthly'),
        ('YEARLY', 'Yearly'),
    ]
    
    name = models.CharField(max_length=255)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField(blank=True)
    date = models.DateTimeField(default=datetime.now)
    expense_type = models.CharField(max_length=10, choices=EXPENSE_TYPES)
    recurring_frequency = models.CharField(max_length=10, choices=RECURRING_FREQUENCIES, null=True, blank=True)
    recurring_start_date = models.DateField(null=True, blank=True)
    recurring_end_date = models.DateField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    deleted_at = models.DateTimeField(null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)