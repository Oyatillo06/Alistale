# Generated by Django 4.0.2 on 2022-02-28 12:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userapp', '0004_alter_manzil_zipcode'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mijoz',
            name='email',
            field=models.EmailField(max_length=254, null=True),
        ),
    ]
