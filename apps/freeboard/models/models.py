from django.db import models


# Create your models here.
class Transaction(models.Model):
    TransactionID = models.IntegerField()
    ProductID = models.IntegerField()
    ReferenceOrderID = models.IntegerField()
    ReferenceOrderLineID = models.IntegerField()
    TransactionDate = models.DateTimeField()
    TransactionType = models.CharField(max_length=2)
    Quantity = models.IntegerField()
    ActualCost = models.IntegerField()
    ModifiedDate = models.DateTimeField

