# Generated by Django 4.2.1 on 2023-06-03 23:28

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('creditcards', '0002_alter_creditcard_card_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='creditcard',
            name='cvc',
            field=models.IntegerField(validators=[django.core.validators.MaxValueValidator(4)]),
        ),
    ]