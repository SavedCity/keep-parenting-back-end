# Generated by Django 4.0.2 on 2022-02-20 16:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('childrenApp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='children',
            name='age_months',
        ),
        migrations.RemoveField(
            model_name='children',
            name='age_years',
        ),
        migrations.AddField(
            model_name='children',
            name='birth_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]