# Generated by Django 2.2 on 2019-04-18 11:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('navu', '0005_auto_20190418_1649'),
    ]

    operations = [
        migrations.AlterField(
            model_name='register',
            name='Password',
            field=models.CharField(max_length=255),
        ),
    ]