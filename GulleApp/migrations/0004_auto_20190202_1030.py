# Generated by Django 2.1.5 on 2019-02-02 10:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('GulleApp', '0003_auto_20190202_1025'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='message',
            name='time',
        ),
        migrations.AlterField(
            model_name='message',
            name='date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
