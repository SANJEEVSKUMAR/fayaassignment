# Generated by Django 4.1.5 on 2023-04-04 07:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='status',
            field=models.BooleanField(default=False),
        ),
    ]
