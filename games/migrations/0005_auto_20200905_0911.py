# Generated by Django 3.1 on 2020-09-05 09:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0004_auto_20200905_0909'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game',
            name='negative_ratings',
            field=models.DecimalField(
                blank=True, decimal_places=0, max_digits=10, null=True),
        ),
        migrations.AlterField(
            model_name='game',
            name='positive_ratings',
            field=models.DecimalField(
                blank=True, decimal_places=0, max_digits=10, null=True),
        ),
        migrations.AlterField(
            model_name='game',
            name='required_age',
            field=models.DecimalField(
                blank=True, decimal_places=0, max_digits=10, null=True),
        ),
    ]
