# Generated by Django 5.1.4 on 2025-04-30 13:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('StechApp', '0014_servicerequest_desktop_package_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='JobApplication',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(max_length=15)),
                ('education', models.CharField(choices=[('Graduation', 'Graduation'), ('Postgraduation', 'Postgraduation'), ('Schooling', 'Schooling')], max_length=20)),
                ('resume', models.FileField(upload_to='resumes/')),
                ('applied_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
