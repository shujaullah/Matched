# Generated by Django 3.2.12 on 2022-04-12 16:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Apply', '0019_alter_profile_birth_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='birth_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]
