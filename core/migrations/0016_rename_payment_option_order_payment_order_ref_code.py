# Generated by Django 4.0 on 2021-12-18 20:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0015_order_being_delivered_order_received_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='payment_option',
            new_name='payment',
        ),
        migrations.AddField(
            model_name='order',
            name='ref_code',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]