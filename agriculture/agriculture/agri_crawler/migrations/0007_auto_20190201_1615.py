# Generated by Django 2.1.2 on 2019-02-01 07:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('agri_crawler', '0006_auto_20190131_2200'),
    ]

    operations = [
        migrations.AddField(
            model_name='daum_blog',
            name='nickname',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='daum_blog',
            name='keyword',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='naver',
            name='keyword',
            field=models.CharField(max_length=130, null=True),
        ),
    ]
