# Generated by Django 4.2.9 on 2024-03-10 12:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0008_assay_day_assay_year'),
    ]

    operations = [
        migrations.CreateModel(
            name='Counter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('counter_img', models.ImageField(default='img/unknown.png', upload_to='counter')),
            ],
        ),
        migrations.CreateModel(
            name='MissionLock',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mission_lock_img', models.ImageField(default='img/unknown.png', upload_to='mission_lock')),
            ],
        ),
        migrations.RemoveField(
            model_name='depthofexcavation',
            name='assay',
        ),
        migrations.RemoveField(
            model_name='fossilview',
            name='assay',
        ),
        migrations.RemoveField(
            model_name='metercapacity',
            name='assay',
        ),
        migrations.RemoveField(
            model_name='residencecard',
            name='assay',
        ),
        migrations.RemoveField(
            model_name='artificialsecuritycard',
            name='location_ne',
        ),
        migrations.RemoveField(
            model_name='assay',
            name='voltage_type',
        ),
        migrations.RemoveField(
            model_name='assignedtask',
            name='location_ne',
        ),
        migrations.RemoveField(
            model_name='cuttercapacity',
            name='location_ne',
        ),
        migrations.RemoveField(
            model_name='fighter',
            name='location_ne',
        ),
        migrations.RemoveField(
            model_name='fireextinguisher',
            name='location_ne',
        ),
        migrations.RemoveField(
            model_name='firstaid',
            name='location_ne',
        ),
        migrations.RemoveField(
            model_name='object',
            name='location_ne',
        ),
        migrations.RemoveField(
            model_name='obstacle',
            name='location_ne',
        ),
        migrations.RemoveField(
            model_name='paramedic',
            name='location_ne',
        ),
        migrations.RemoveField(
            model_name='permit',
            name='location_ne',
        ),
        migrations.RemoveField(
            model_name='picturesofsite',
            name='location_ne',
        ),
        migrations.RemoveField(
            model_name='preworkmeeting',
            name='location_ne',
        ),
        migrations.RemoveField(
            model_name='recipientcard',
            name='location_ne',
        ),
        migrations.RemoveField(
            model_name='riskassessment',
            name='location_ne',
        ),
        migrations.RemoveField(
            model_name='safetybarrier',
            name='location_ne',
        ),
        migrations.RemoveField(
            model_name='safeworkprocedure',
            name='location_ne',
        ),
        migrations.RemoveField(
            model_name='sourcecard',
            name='location_ne',
        ),
        migrations.RemoveField(
            model_name='subscriptionnumber',
            name='location_ne',
        ),
        migrations.RemoveField(
            model_name='teammodel',
            name='location_ne',
        ),
        migrations.RemoveField(
            model_name='tuvforequipmentanddriver',
            name='location_ne',
        ),
        migrations.RemoveField(
            model_name='violation',
            name='location_ne',
        ),
        migrations.RemoveField(
            model_name='workteam',
            name='location_ne',
        ),
        migrations.DeleteModel(
            name='CableLength',
        ),
        migrations.DeleteModel(
            name='DepthOfExcavation',
        ),
        migrations.DeleteModel(
            name='FossilView',
        ),
        migrations.DeleteModel(
            name='MeterCapacity',
        ),
        migrations.DeleteModel(
            name='ResidenceCard',
        ),
        migrations.AddField(
            model_name='missionlock',
            name='assay',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.assay'),
        ),
        migrations.AddField(
            model_name='counter',
            name='assay',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.assay'),
        ),
    ]
