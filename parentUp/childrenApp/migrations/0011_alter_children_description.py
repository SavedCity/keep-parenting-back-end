# Generated by Django 4.0.2 on 2022-02-21 16:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('childrenApp', '0010_alter_children_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='children',
            name='description',
            field=models.TextField(null=True),
        ),
    ]
