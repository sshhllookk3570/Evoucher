# Generated by Django 3.1.7 on 2021-04-03 17:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Voucher', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='voucher',
            name='expiry_date',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='voucher',
            name='start_date',
            field=models.DateField(),
        ),
    ]
