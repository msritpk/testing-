# Generated by Django 4.0.4 on 2023-02-11 18:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0013_certificate_ticketid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='certificate',
            name='ticketid',
            field=models.CharField(default='1001', max_length=100),
        ),
    ]