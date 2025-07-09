from django.db import models

class Expense(models.Model):
    uid = models.CharField(max_length=128)  # Firebase UID
    date = models.DateField()
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField(blank=True)
    who_paid = models.CharField(max_length=128)  # Firebase UID of who paid
    paid_status = models.BooleanField(default=False) # type: ignore
    raw_text = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.date} | {self.amount}€ | Paid by {self.who_paid}"
