from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    name = models.CharField(max_length=255, unique=True)

    class Meta:
        verbose_name_plural = 'categories'
    
    def __str__(self) -> str:
        return self.name
    

# Transaction can be ether Income or Expense
# Has a amount
class Transaction(models.Model):
    TRANSACTION_TYPE_CHOICE = (
        ('Income', 'Income'),
        ('Expense', 'Expense')
    ) 
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    type = models.CharField(max_length=10, choices=TRANSACTION_TYPE_CHOICE)
    amount = models.DecimalField(max_digits=10,decimal_places=2)
    date = models.DateField()

    def __str__(self) -> str:
        return f'{self.type} of {self.amount} on {self.category} by {self.user}'
    