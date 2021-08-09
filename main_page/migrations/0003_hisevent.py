# Generated by Django 3.1.4 on 2021-07-15 18:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_page', '0002_auto_20210715_2318'),
    ]

    operations = [
        migrations.CreateModel(
            name='HisEvent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('duration', models.CharField(max_length=50)),
                ('title', models.CharField(max_length=1000)),
                ('body', models.CharField(max_length=1000000)),
                ('link', models.CharField(max_length=100)),
                ('image', models.ImageField(blank=True, null=True, upload_to='')),
            ],
        ),
    ]