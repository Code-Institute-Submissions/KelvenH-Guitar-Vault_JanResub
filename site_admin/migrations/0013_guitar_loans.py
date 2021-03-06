# Generated by Django 3.2.9 on 2022-01-28 23:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('guitars', '0017_alter_guitar_no_strings'),
        ('members', '0005_delete_membersplans'),
        ('site_admin', '0012_auto_20220128_2118'),
    ]

    operations = [
        migrations.CreateModel(
            name='Guitar_Loans',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('loan_status', models.CharField(choices=[('Pending', 'Pending'), ('Shipping', 'Shipping'), ('Performing', 'Performing')], default='Pending', max_length=20)),
                ('requested_date', models.DateField(auto_now_add=True)),
                ('shipped_date', models.DateField(blank=True, null=True)),
                ('returned_date', models.DateField(blank=True, null=True)),
                ('guitar', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='guitar_loans', to='guitars.guitar')),
                ('member', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='guitar_member', to='members.memberprofile')),
            ],
            options={
                'verbose_name_plural': 'Guitar Loans',
            },
        ),
    ]
