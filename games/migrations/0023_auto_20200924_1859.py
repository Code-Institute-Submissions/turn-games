# Generated by Django 3.1.1 on 2020-09-24 18:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0022_auto_20200924_1852'),
    ]

    operations = [
        migrations.RenameField(
            model_name='game',
            old_name='price_calculated',
            new_name='price_calculated_value',
        ),
    ]
