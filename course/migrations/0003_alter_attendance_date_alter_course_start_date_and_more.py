# Generated by Django 4.1.3 on 2024-06-10 10:15

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0002_alter_student_token_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attendance',
            name='date',
            field=models.DateField(default=datetime.date(2024, 6, 10)),
        ),
        migrations.AlterField(
            model_name='course',
            name='start_date',
            field=models.DateField(default=datetime.date(2024, 6, 10)),
        ),
        migrations.AlterField(
            model_name='student',
            name='token_id',
            field=models.CharField(default='83322890', max_length=150),
        ),
    ]
