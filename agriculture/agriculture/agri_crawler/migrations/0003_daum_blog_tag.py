# Generated by Django 2.1.3 on 2019-01-09 09:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('agri_crawler', '0002_naver_main_url'),
    ]

    operations = [
        migrations.AddField(
            model_name='daum_blog',
            name='tag',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
