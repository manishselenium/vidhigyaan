# Generated by Django 4.1 on 2022-08-29 05:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_remove_contact_phone'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='phone',
            field=models.CharField(default='9752324265', max_length=12),
        ),
    ]
