# Generated by Django 3.1.7 on 2021-05-18 01:58

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('teacher_info', '0002_student_info'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student_info',
            name='Class',
            field=models.CharField(choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5')], default=1, max_length=2),
        ),
        migrations.CreateModel(
            name='AgentDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location', models.TextField()),
                ('identification_type', models.CharField(choices=[('others', 'Others')], max_length=20)),
                ('identification_number', models.CharField(max_length=20)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='agent_detail', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
