# Generated by Django 3.0.7 on 2020-07-21 12:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Card',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('eudra_number', models.CharField(max_length=14)),
                ('cebk_number', models.CharField(max_length=14)),
                ('sponsor', models.TextField()),
                ('center_number', models.CharField(max_length=6)),
                ('center_name', models.TextField()),
                ('crf_version', models.CharField(max_length=20)),
                ('doctor_name', models.CharField(max_length=25)),
                ('doctor_phonenumber', models.CharField(max_length=15)),
                ('doctor_fax', models.CharField(max_length=20)),
                ('doctor_email', models.CharField(max_length=20)),
                ('patient_initials', models.CharField(max_length=2)),
                ('scrining_number', models.CharField(max_length=5)),
            ],
        ),
    ]
