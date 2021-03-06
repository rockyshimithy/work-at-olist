# Generated by Django 2.0 on 2018-05-27 16:22

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
                ('source', models.BigIntegerField(null=True, verbose_name='Telephone number that originated the call')),
                ('destination', models.BigIntegerField(null=True, verbose_name='Telephone number that received the call')),
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
