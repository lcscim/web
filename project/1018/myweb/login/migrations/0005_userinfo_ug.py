# Generated by Django 2.1.2 on 2018-10-18 10:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0004_usergroup'),
    ]

    operations = [
        migrations.AddField(
            model_name='userinfo',
            name='ug',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='login.UserGroup'),
        ),
    ]
