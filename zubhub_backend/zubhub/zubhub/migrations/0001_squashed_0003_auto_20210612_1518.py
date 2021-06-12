# Generated by Django 2.2.7 on 2021-06-12 15:29

from django.db import migrations, models


class Migration(migrations.Migration):

    replaces = [('zubhub', '0001_squashed_0007_auto_20210612_0115'), ('zubhub', '0002_auto_20210612_1517'), ('zubhub', '0003_auto_20210612_1518')]

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FAQ',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.TextField(blank=True, null=True)),
                ('answer', models.TextField(blank=True, null=True)),
            ],
            options={
                'verbose_name': 'FAQ',
                'verbose_name_plural': 'FAQs',
            },
        ),
        migrations.CreateModel(
            name='Help',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('about', models.TextField(blank=True, null=True)),
                ('edited_on', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'verbose_name': 'Help',
                'verbose_name_plural': 'Help',
            },
        ),
        migrations.CreateModel(
            name='Privacy',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('privacy_policy', models.TextField(blank=True, null=True)),
                ('terms_of_use', models.TextField(blank=True, null=True)),
                ('edited_on', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'verbose_name': 'Privacy',
                'verbose_name_plural': 'Privacy',
            },
        ),
        migrations.CreateModel(
            name='Hero',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=100, null=True)),
                ('image', models.ImageField(null=True, upload_to='')),
                ('image_url', models.URLField(blank=True, max_length=1000)),
                ('activity_url', models.URLField(max_length=1000, null=True)),
            ],
            options={
                'verbose_name': 'Hero',
                'verbose_name_plural': 'Heroes',
            },
        ),
    ]