# Generated by Django 5.0.4 on 2024-04-20 09:36

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('log', '0005_cvisit_loadhours_cvisit_workinghours'),
    ]

    operations = [
        migrations.AddField(
            model_name='clist',
            name='cTechnician',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='technician', to=settings.AUTH_USER_MODEL),
        ),
    ]