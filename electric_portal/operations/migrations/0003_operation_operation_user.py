# Generated by Django 4.2.9 on 2024-03-23 01:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0010_rename_feeder_num_assay_cable_length_and_more'),
        ('operations', '0002_operation_day_operation_month_operation_year'),
    ]

    operations = [
        migrations.AddField(
            model_name='operation',
            name='operation_user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='home.usertable'),
            preserve_default=False,
        ),
    ]
