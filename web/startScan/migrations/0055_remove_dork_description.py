# Generated by Django 3.2.4 on 2023-09-22 08:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('startScan', '0054_auto_20230910_0533'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='dork',
            name='description',
        ),
    ]
