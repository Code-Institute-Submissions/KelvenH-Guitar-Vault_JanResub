# Generated by Django 3.2.9 on 2022-01-29 01:33

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('site_admin', '0013_guitar_loans'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='guitar_loans',
            name='member',
        ),
        migrations.AddField(
            model_name='guitar_loans',
            name='user',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, related_name='guitar_member', to=settings.AUTH_USER_MODEL),
        ),
    ]
