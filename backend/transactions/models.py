from django.db import models
from accounts.models import User
from products.models import Product

class Transaction(models.Model):
    buyer = models.ForeignKey(User, related_name='buyer_transactions', on_delete=models.CASCADE)
    seller= models.ForeignKey(User, related_name='seller_transactions', on_delete=models.CASCADE)
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    status = models.CharField(max_length=50, choices=[('escrow', 'Escrow'), ('completed', 'Completed'), ('dispute', 'Dispute')])
    escrow_amount = models.DecimalField(max_digits=10, decimal_places=2)
    tracking_number = models.CharField(max_length=100, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Transaction {self.id} - {self.product.title}"
    
# Create your models here.
