# Generated by Django 3.2.8 on 2021-10-12 14:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('_course', '0003_rabel'),
    ]

    operations = [
        migrations.CreateModel(
            name='inhritance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student_name', models.CharField(max_length=50)),
                ('teacher_name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('password', models.CharField(max_length=50)),
            ],
        ),
    ]