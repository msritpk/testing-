# Generated by Django 4.0.4 on 2023-02-11 12:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0010_certificate_username'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='certificate',
            name='username',
        ),
    ]
