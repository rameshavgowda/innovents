from django.db import models
from django.core.validators import MinLengthValidator

# Create your models here.

class company(models.Model):
    Id = models.BigAutoField(primary_key = True)
    Company_name = models.CharField(max_length=50,null = False, validators=[MinLengthValidator(5)])
    Email_id = models.EmailField(max_length=50, null = False)
    Company_code=models.CharField(max_length=5 ,unique = True, null=True,validators=[MinLengthValidator(5)])
    Strength = models.IntegerField(null = True)
    Website= models.URLField(null = True)
    Created_datetime = models.DateTimeField(auto_now_add = True )
