# Generated by Django 2.1.5 on 2020-06-05 09:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CRUD_OPS', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='register',
            name='email',
            field=models.EmailField(max_length=50, unique=True),
        ),
    ]
