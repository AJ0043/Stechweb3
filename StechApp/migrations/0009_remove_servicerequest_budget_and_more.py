# Generated by Django 5.1.4 on 2025-04-29 09:58

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('StechApp', '0008_servicerequest'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='servicerequest',
            name='budget',
        ),
        migrations.AddField(
            model_name='servicerequest',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='servicerequest',
            name='message',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='servicerequest',
            name='phone',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='servicerequest',
            name='service_type',
            field=models.CharField(choices=[('web', 'Web Development'), ('seo', 'SEO'), ('marketing', 'Digital Marketing'), ('design', 'UI/UX Design'), ('ecommerce', 'E-commerce Solutions')], max_length=50),
        ),
    ]
