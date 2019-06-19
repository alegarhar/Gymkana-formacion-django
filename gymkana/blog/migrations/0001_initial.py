# Generated by Django 2.2.2 on 2019-06-19 12:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('subtitle', models.CharField(max_length=100)),
                ('body', models.TextField()),
                ('start_date', models.DateTimeField(verbose_name='started at')),
                ('end_date', models.DateTimeField(verbose_name='finished at')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='New',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('subtitle', models.CharField(max_length=100)),
                ('body', models.TextField()),
                ('publish_date', models.DateTimeField(auto_now=True)),
                ('image', models.ImageField(default='blog/images/default.jpg', null=True, upload_to='blog/images')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
