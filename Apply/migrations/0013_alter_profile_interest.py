# Generated by Django 3.2.12 on 2022-04-05 17:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Apply', '0012_auto_20220405_1306'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='interest',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Apply.user_interests'),
        ),
    ]