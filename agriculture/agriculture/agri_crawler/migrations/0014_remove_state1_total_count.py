# Generated by Django 2.1.2 on 2019-02-12 04:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('agri_crawler', '0013_state1_total_count'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='state1',
            name='total_count',
        ),
    ]
