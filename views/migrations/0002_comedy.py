# Generated by Django 4.0.4 on 2022-05-24 03:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('views', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comedy',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60)),
                ('image', models.ImageField(blank=True, null=True, upload_to='')),
                ('year', models.IntegerField()),
            ],
        ),
    ]
