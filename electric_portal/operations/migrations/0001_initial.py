# Generated by Django 4.2.9 on 2024-03-22 23:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Operation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('operation_malfunctionNumber', models.CharField(blank=True, max_length=50, null=True)),
                ('operation_malfunctionType', models.CharField(blank=True, max_length=50, null=True)),
                ('operation_workNumber', models.CharField(blank=True, max_length=50, null=True)),
                ('operation_employmentType', models.CharField(blank=True, max_length=50, null=True)),
                ('operation_contractor', models.CharField(blank=True, max_length=50, null=True)),
                ('operation_date', models.CharField(blank=True, max_length=50, null=True)),
                ('operation_site', models.CharField(blank=True, max_length=50, null=True)),
                ('operation_materials', models.CharField(blank=True, max_length=50, null=True)),
                ('operation_consultantName', models.CharField(blank=True, max_length=50, null=True)),
                ('operation_type', models.CharField(blank=True, max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='OperationFile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(upload_to='pdf-files')),
                ('operation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='operations.operation')),
            ],
        ),
    ]
