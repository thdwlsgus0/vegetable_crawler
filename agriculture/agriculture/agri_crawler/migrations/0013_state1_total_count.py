# Generated by Django 2.1.2 on 2019-02-12 04:45

import agri_crawler.models
from django.db import migrations
import djongo.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('agri_crawler', '0012_auto_20190203_1930'),
    ]

    operations = [
        migrations.AddField(
            model_name='state1',
            name='total_count',
            field=djongo.models.fields.EmbeddedModelField(model_container=agri_crawler.models.media_count, model_form_class=agri_crawler.models.media_countForm, null=True),
        ),
    ]
