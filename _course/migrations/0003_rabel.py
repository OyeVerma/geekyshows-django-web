# Generated by Django 3.2.8 on 2021-10-10 08:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('_course', '0002_auto_20211010_1345'),
    ]

    operations = [
        migrations.CreateModel(
            name='rabel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
    ]
