# Generated by Django 5.0.2 on 2024-04-16 08:03

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('log', '0003_cvisit'),
    ]

    operations = [
        migrations.CreateModel(
            name='visitCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('visitReason', models.CharField(max_length=64)),
            ],
        ),
        migrations.AlterField(
            model_name='cvisit',
            name='visitReason',
            field=models.ForeignKey(blank='True', null='True', on_delete=django.db.models.deletion.CASCADE, related_name='vReason', to='log.visitcategory'),
        ),
    ]