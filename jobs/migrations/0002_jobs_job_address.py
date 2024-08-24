# Generated by Django 5.0.3 on 2024-05-02 18:20

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('address', '0001_initial'),
        ('jobs', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='jobs',
            name='job_address',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, to='address.address'),
            preserve_default=False,
        ),
    ]
