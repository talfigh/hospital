# Generated by Django 4.2.3 on 2023-07-20 00:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Hospital',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, verbose_name='نام')),
                ('location', models.CharField(blank=True, max_length=64, verbose_name='آدرس')),
                ('phone_number', models.IntegerField(blank=True, verbose_name='شماره تماس')),
            ],
            options={
                'verbose_name': 'بیمارستان',
                'verbose_name_plural': 'بیمارستان ها',
            },
        ),
    ]
