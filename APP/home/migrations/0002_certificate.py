# Generated by Django 4.0.5 on 2023-02-11 02:36

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Certificate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('address', models.CharField(max_length=100)),
                ('hospitalName', models.CharField(max_length=50)),
                ('date', models.DateTimeField()),
                ('doctorName', models.CharField(choices=[('1', 'Doctor_1'), ('2', 'Doctor_2'), ('3', 'Doctor_3'), ('4', 'Doctor_4'), ('5', 'Doctor_5')], max_length=10)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]