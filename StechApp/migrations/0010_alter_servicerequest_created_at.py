# Generated by Django 5.1.4 on 2025-04-29 09:59

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('StechApp', '0009_remove_servicerequest_budget_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='servicerequest',
            name='created_at',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
