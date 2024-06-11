# Generated by Django 4.1.3 on 2024-06-11 07:40

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0003_alter_attendance_date_alter_course_start_date_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='students/'),
        ),
        migrations.AlterField(
            model_name='attendance',
            name='date',
            field=models.DateField(default=datetime.date(2024, 6, 11)),
        ),
        migrations.AlterField(
            model_name='course',
            name='start_date',
            field=models.DateField(default=datetime.date(2024, 6, 11)),
        ),
        migrations.AlterField(
            model_name='student',
            name='token_id',
            field=models.CharField(default='67714894', max_length=150),
        ),
    ]