# Generated by Django 3.2 on 2021-05-15 13:33

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_auto_20210515_1325'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registeration',
            name='phone',
            field=models.CharField(max_length=10, validators=[django.core.validators.RegexValidator('^\\d{0,10}$')]),
        ),
        migrations.AlterField(
            model_name='registeration',
            name='roll_no',
            field=models.CharField(max_length=6, primary_key=True, serialize=False, validators=[django.core.validators.RegexValidator('^\\d{1,10}$')]),
        ),
    ]
