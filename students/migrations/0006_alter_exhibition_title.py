# Generated by Django 4.1.2 on 2022-11-03 15:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0005_alter_exhibition_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='exhibition',
            name='title',
            field=models.CharField(max_length=120),
        ),
    ]
