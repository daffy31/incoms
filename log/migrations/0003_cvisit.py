# Generated by Django 5.0.2 on 2024-04-16 07:59

import django.db.models.expressions
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('log', '0002_clist'),
    ]

    operations = [
        migrations.CreateModel(
            name='cVisit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('visitReason', models.CharField(max_length=32)),
                ('visitDate', models.DateField()),
                ('itemDetails', models.ForeignKey(blank='True', null='True', on_delete=django.db.models.expressions.Case, related_name='details', to='log.clist')),
            ],
        ),
    ]