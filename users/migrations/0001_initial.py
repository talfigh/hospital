# Generated by Django 4.1.2 on 2023-03-02 09:13

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("hospital", "__first__"),
        ("auth", "0012_alter_user_first_name_max_length"),
    ]

    operations = [
        migrations.CreateModel(
            name="Personnel",
            fields=[
                (
                    "user",
                    models.OneToOneField(
                        default="",
                        on_delete=django.db.models.deletion.CASCADE,
                        primary_key=True,
                        related_name="person",
                        serialize=False,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "hospital",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="hospital.hospital",
                        verbose_name="نام بیمارستان",
                    ),
                ),
            ],
            options={
                "verbose_name": "پرسنل",
                "verbose_name_plural": "پرسنل",
            },
        ),
    ]
