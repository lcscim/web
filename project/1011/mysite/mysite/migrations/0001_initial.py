# Generated by Django 2.1.2 on 2018-10-11 10:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=64)),
                ('sex', models.CharField(max_length=64)),
                ('email', models.CharField(max_length=64)),
            ],
        ),
    ]
