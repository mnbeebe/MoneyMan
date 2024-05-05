from django.db import models
from django.db.models import CheckConstraint, Q, F
from django.contrib.auth.models import User

# Create your models here.
class Expense(models.Model):
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField(null=True, blank=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateTimeField()

    class Meta: 
        ordering = ["date"]
        
        constraints = [
            CheckConstraint(
                check=Q(amount__gte = 0),
                name="amount_gte_0",
                violation_error_message="Expense value cannot be negative"
            ),
        ]

    def __str__(self) -> str:
        return f'{self.amount}'