# Generated by Django 3.2.12 on 2022-05-03 14:57

from django.db import migrations, models
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('Apply', '0033_remove_profile_birth_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='Education',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('school', models.CharField(max_length=200)),
                ('expected_tution', models.IntegerField()),
                ('interests', multiselectfield.db.fields.MultiSelectField(blank=True, choices=[('tech', 'Technology'), ('eng', 'Engineering'), ('bio', 'Biology'), ('art', 'Art'), ('ath', 'Athletics'), ('fin', 'Finance'), ('bus', 'Business')], max_length=28)),
            ],
        ),
    ]
