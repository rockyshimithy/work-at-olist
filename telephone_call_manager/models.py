#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.db import models


class TelephoneCall(models.Model):

    RECORD_TYPES = (
        ('start', '0'),
        ('end', '1'),
    )

    type = models.CharField(max_length=1, choices=RECORD_TYPES, verbose_name='Type')
    timestamp = models.DateTimeField(verbose_name='Timestamp of the event')
    call_id = models.PositiveIntegerField(verbose_name='Call Identifier')
    source = models.BigIntegerField(null=True, verbose_name='Telephone number that originated the call')
    destination = models.BigIntegerField(null=True, verbose_name='Telephone number that received the call')

    class Meta:
        verbose_name = 'Telephone call'
        verbose_name_plural = 'Telephone calls'
        unique_together = ('type', 'call_id',)
