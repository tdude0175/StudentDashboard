# Generated by Django 2.0.6 on 2020-01-03 14:31

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('StudentDashBoard', '0004_auto_20200103_1429'),
    ]

    operations = [
        migrations.AddField(
            model_name='scorecardmodel',
            name='cohort',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='StudentDashBoard.ClassModel'),
        ),
        migrations.AlterField(
            model_name='attendacemodels',
            name='dateTimeRecord',
            field=models.DateTimeField(default=datetime.datetime(2020, 1, 3, 14, 31, 36, 962441, tzinfo=utc)),
        ),
    ]
