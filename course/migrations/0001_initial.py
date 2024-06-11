# Generated by Django 4.1.1 on 2022-11-15 20:41

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Student",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("full_name", models.CharField(max_length=200)),
                ("phone_number", models.CharField(max_length=120)),
                ("wallet", models.IntegerField(default=0)),
                ("token_id", models.CharField(default="58138710", max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name="Course",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=120)),
                ("title", models.TextField(blank=True, null=True)),
                ("price", models.PositiveBigIntegerField()),
                (
                    "time",
                    models.CharField(
                        choices=[
                            ("1", "7.30:9.30"),
                            ("2", "10.00:12:00"),
                            ("3", "13.00:15.00"),
                            ("4", "15.30:17.30"),
                        ],
                        max_length=150,
                    ),
                ),
                (
                    "days",
                    models.CharField(
                        choices=[("1", "Dush-Chor-Jum"), ("2", "Sesh-Pay-Shan")],
                        max_length=150,
                    ),
                ),
                ("room", models.PositiveBigIntegerField()),
                ("start_date", models.DateField(default=datetime.date(2022, 11, 16))),
                ("end_date", models.DateField(blank=True, null=True)),
                ("is_ended", models.BooleanField(default=False)),
                ("students", models.ManyToManyField(to="course.student")),
                (
                    "teacher",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="AttendanceGroup",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "time",
                    models.CharField(
                        choices=[
                            ("1", "7.30:9.30"),
                            ("2", "10.00:12:00"),
                            ("3", "13.00:15.00"),
                            ("4", "15.30:17.30"),
                        ],
                        max_length=150,
                    ),
                ),
                ("date", models.DateField()),
                ("status", models.CharField(max_length=150)),
                (
                    "course",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="course.course"
                    ),
                ),
                (
                    "teacher",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Attendance",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("date", models.DateField(default=datetime.date(2022, 11, 16))),
                ("present", models.BooleanField(default=True)),
                (
                    "attendance",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="course.attendancegroup",
                    ),
                ),
                (
                    "student",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="course.student"
                    ),
                ),
            ],
        ),
    ]