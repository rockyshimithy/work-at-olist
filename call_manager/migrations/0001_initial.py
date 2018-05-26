#!/usr/bin/env python
# -*- coding: utf-8 -*-


from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TelephoneCall',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('start', '0'), ('end', '1')], max_length=1, verbose_name='Type')),
                ('timestamp', models.DateTimeField(verbose_name='Timestamp of the event')),
                ('call_id', models.PositiveIntegerField(verbose_name='Call Identifier')),
                ('source', models.BigIntegerField(null=True)),
                ('destination', models.BigIntegerField(null=True)),
            ],
            options={
                'verbose_name': 'Telephone call',
                'verbose_name_plural': 'Telephone calls',
            },
        ),
        migrations.AlterUniqueTogether(
            name='telephonecall',
            unique_together={('type', 'call_id')},
        ),
    ]
