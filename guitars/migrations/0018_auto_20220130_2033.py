# Generated by Django 3.2.9 on 2022-01-30 20:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('guitars', '0017_alter_guitar_no_strings'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='friendly_name',
            field=models.CharField(blank=True, default='', max_length=50),
        ),
        migrations.AlterField(
            model_name='guitar',
            name='approx_age_years',
            field=models.DecimalField(blank=True, decimal_places=0, default=0, max_digits=2),
        ),
        migrations.AlterField(
            model_name='guitar',
            name='body_top',
            field=models.CharField(blank=True, default='', max_length=50),
        ),
        migrations.AlterField(
            model_name='guitar',
            name='body_wood',
            field=models.CharField(blank=True, default='', max_length=50),
        ),
        migrations.AlterField(
            model_name='guitar',
            name='construction',
            field=models.CharField(blank=True, default='', max_length=25),
        ),
        migrations.AlterField(
            model_name='guitar',
            name='controls',
            field=models.CharField(blank=True, default='', max_length=250),
        ),
        migrations.AlterField(
            model_name='guitar',
            name='neck_profile',
            field=models.CharField(blank=True, default='', max_length=25),
        ),
        migrations.AlterField(
            model_name='guitar',
            name='neck_wood',
            field=models.CharField(blank=True, default='', max_length=25),
        ),
        migrations.AlterField(
            model_name='guitar',
            name='scale_length',
            field=models.CharField(blank=True, default='', max_length=25),
        ),
        migrations.AlterField(
            model_name='guitar',
            name='tuners',
            field=models.CharField(blank=True, default='', max_length=50),
        ),
    ]
