# Generated by Django 4.0.6 on 2022-08-02 15:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='queuedetails',
            old_name='jsonDate',
            new_name='joinedTimeAndDate',
        ),
        migrations.AddField(
            model_name='queuedetails',
            name='leaveTimeAndDate',
            field=models.TextField(blank=b'I01\n', default='-', null=True),
        ),
    ]