# Generated by Django 5.0.2 on 2024-04-11 06:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('log', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='cList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cOwner', models.CharField(max_length=32)),
                ('cModel', models.CharField(max_length=32)),
                ('cSerial', models.CharField(max_length=32)),
            ],
        ),
    ]
