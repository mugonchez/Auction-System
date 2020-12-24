# Generated by Django 2.1.4 on 2019-05-19 08:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0043_auto_20190518_1018'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderdetails',
            name='confirm',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='orderdetails',
            name='address_of_delivery',
            field=models.CharField(choices=[('Ng', 'Nchiru CBD'), ('Am', 'Ambassadors'), ('Rw', 'Railways'), ('Up', 'Uhuru park')], default='Ngara', max_length=50),
        ),
    ]