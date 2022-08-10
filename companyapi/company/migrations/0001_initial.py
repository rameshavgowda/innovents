# Generated by Django 4.0.4 on 2022-08-10 11:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='company',
            fields=[
                ('id', models.BigIntegerField(primary_key=True, serialize=False)),
                ('company_name', models.CharField(max_length=50)),
                ('Email_id', models.CharField(max_length=50)),
                ('Company_code', models.CharField(max_length=5, unique=True)),
                ('strength', models.IntegerField()),
                ('website', models.URLField()),
                ('created_time', models.TimeField()),
            ],
        ),
    ]
