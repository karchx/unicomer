# Generated by Django 4.2.1 on 2023-06-01 22:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=240, verbose_name='Name')),
                ('lastname', models.CharField(max_length=240, verbose_name='LastName')),
                ('email', models.EmailField(max_length=254)),
                ('password', models.CharField(max_length=50)),
                ('created_at', models.DateField(auto_now_add=True)),
            ],
        ),
    ]
