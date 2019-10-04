# Generated by Django 2.2.4 on 2019-10-02 15:11

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('authapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='shopuser',
            name='activation_key',
            field=models.CharField(blank=True, max_length=128, verbose_name='activation key'),
        ),
        migrations.AddField(
            model_name='shopuser',
            name='activation_key_expire',
            field=models.DateTimeField(default=datetime.datetime(2019, 10, 4, 15, 11, 37, 281553, tzinfo=utc), verbose_name='key relevance'),
        ),
    ]