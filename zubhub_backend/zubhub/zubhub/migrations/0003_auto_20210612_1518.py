# Generated by Django 2.2.7 on 2021-06-12 15:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zubhub', '0002_auto_20210612_1517'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hero',
            name='activity_url',
            field=models.URLField(max_length=1000, null=True),
        ),
    ]