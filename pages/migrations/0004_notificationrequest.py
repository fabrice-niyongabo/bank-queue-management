# Generated by Django 4.0.6 on 2022-09-04 19:45

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0003_alter_queuedetails_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='NotificationRequest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False)),
                ('phone', models.CharField(max_length=10)),
                ('names', models.CharField(max_length=50)),
                ('queueLength', models.IntegerField()),
                ('date', models.DateTimeField(default=datetime.datetime(2022, 9, 4, 21, 45, 6, 722605))),
            ],
        ),
    ]
