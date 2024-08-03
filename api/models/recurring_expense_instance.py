from django.db import models
from datetime import datetime
from .expense import Expense

class RecurringExpenseInstance(models.Model):
    STATUS_CHOICES = [
        ('PENDING', 'Pending'),
        ('PAID', 'Paid'),
        ('SKIPPED', 'Skipped'),
    ]
    
    expense = models.ForeignKey(Expense, on_delete=models.CASCADE)
    date = models.DateTimeField(default=datetime.now)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES)
    actual_payment_date = models.DateField(null=True, blank=True)
    actual_amount_paid = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    notes = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    deleted_at = models.DateTimeField(null=True, blank=True)