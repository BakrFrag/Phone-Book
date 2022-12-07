from django.db import models
from django.core.validators import RegexValidator

# Create your models here.
class Contact(models.Model):
    """
    reprsents contact name , contact name unique
    """
    username = models.CharField(max_length=256 , unique=True)


class PhoneNumber(models.Model):
    number = models.CharField(max_length=256,unique=True,validators=[
        RegexValidator(
       
            regex='^01\d{9}' , 
            message="Phone Numbers Must Start With 01 & all Are Numbers",
        ),
    ])
    contact = models.ForeignKey(Contact , on_delete= models.CASCADE , related_name="numbers")
    


