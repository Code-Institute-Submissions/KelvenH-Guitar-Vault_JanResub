# Generated by Django 3.2.9 on 2021-11-13 12:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('guitars', '0004_auto_20211112_1920'),
    ]

    operations = [
        migrations.AlterField(
            model_name='guitar',
            name='condition',
            field=models.CharField(blank=True, choices=[('Excellent', 'Excellent'), ('Good', 'Good'), ('Cosmetic', 'Well Used (displays cosmetic signs of use only)'), ('Defective', 'Some form of damage / wear which affects performance. (No guitars can be added to the vault if defective. Existing guitars rated by users as defective will be marked as "unavailable" until inspected by Guitar Vault')], max_length=25, null=True),
        ),
        migrations.AlterField(
            model_name='guitar',
            name='no_strings',
            field=models.DecimalField(blank=True, decimal_places=0, max_digits=2, null=True),
        ),
    ]
