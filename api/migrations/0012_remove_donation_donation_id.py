# Generated by Django 3.0.5 on 2020-04-08 03:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0011_donation_verified'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='donation',
            name='donation_id',
        ),
    ]
