# Generated by Django 3.1.7 on 2021-05-17 04:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teacher_info', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='student_info',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('First_name', models.CharField(max_length=20)),
                ('Middle_name', models.CharField(max_length=20)),
                ('Last_name', models.CharField(max_length=20)),
                ('Address', models.CharField(max_length=50)),
                ('Class', models.IntegerField()),
                ('Roll_No', models.IntegerField()),
                ('Gender', models.BooleanField()),
            ],
        ),
    ]
