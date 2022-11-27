# Generated by Django 4.1.3 on 2022-11-27 21:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Device',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, verbose_name='نام')),
                ('model', models.CharField(max_length=64, verbose_name='مدل')),
                ('brand', models.CharField(max_length=32, verbose_name='برند')),
                ('status', models.CharField(choices=[('س', 'سالم'), ('خ', 'خراب')], max_length=10, verbose_name='وضعیت')),
                ('data_created', models.DateTimeField(auto_now_add=True)),
                ('regular_checks', models.PositiveIntegerField()),
            ],
            options={
                'verbose_name': 'دستگاه',
                'verbose_name_plural': 'دستگاه ها',
            },
        ),
    ]
