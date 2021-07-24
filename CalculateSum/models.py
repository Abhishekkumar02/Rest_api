from django.db import models


# Create your models here.
class CalculateSum(models.Model):
    number1 = models.IntegerField()
    number2 = models.IntegerField()
    answer = models.IntegerField()
    uniqueIdentifier = models.CharField(max_length=100, null=False, blank=False)

    def __str__(self):
        return self.number1
