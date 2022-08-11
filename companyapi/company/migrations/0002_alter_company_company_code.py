# Generated by Django 4.0.4 on 2022-08-11 10:30

from django.db import migrations, models
import uuid
from .. models import company

class Migration(migrations.Migration):

    dependencies = [
        ('company', '0001_initial'),
    ]

    def gen_uuid(apps, schema_editor):
        for row in company.objects.all():
            row.Company_code = uuid.uuid4()
            row.save()
    operations = [
        migrations.AlterField(
            model_name='company',
            name='Company_code',
            field=models.CharField(default=uuid.uuid1, max_length=5, null=True, unique=True),
        ),
        migrations.RunPython(gen_uuid),

        migrations.AlterField(
            model_name='company',
            name='Company_code',
            field=models.SlugField(default=uuid.uuid4, unique=True),
        ),
    ]