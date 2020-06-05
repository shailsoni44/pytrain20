# Generated by Django 2.1.5 on 2020-06-05 00:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Register',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25)),
                ('email', models.EmailField(max_length=15, unique=True)),
                ('Repeat_email', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=15)),
                ('re_password', models.CharField(max_length=15)),
            ],
            options={
                'verbose_name_plural': 'Register',
            },
        ),
    ]