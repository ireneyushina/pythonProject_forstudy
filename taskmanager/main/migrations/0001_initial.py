# Generated by Django 4.1.6 on 2023-02-13 12:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Buyer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('usernumber', models.PositiveIntegerField(verbose_name='Номер получателя')),
            ],
        ),
    ]