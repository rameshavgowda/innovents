from django.db import models

# Create your models here.


class company(models.Model):
    id = models.BigIntegerField(primary_key=True)
    company_name = models.CharField(max_length=50, null=False)
    Email_id = models.CharField(max_length=50, null=False)
    Company_code=models.CharField(max_length=5, unique=True)
    strength = models.IntegerField()
    website= models.URLField()
    created_time = models.TimeField()


