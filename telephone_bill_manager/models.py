#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.db import models


class TelephoneBill(models.Model):

    subscriber = models.BigIntegerField(null=False, verbose_name='Subscriber telephone number')
    period = models.DateField(verbose_name='Period of the telephone bill')

    # TODO: Fix start_date, start_time
    destination = models.BigIntegerField(null=False, verbose_name='Telephone number that received the call')
    start_date = models.DateField(verbose_name='Start date of the telephone bill')
    start_time = models.DateTimeField(verbose_name='Start time of the telephone bill')
    duration = models.DurationField(verbose_name='Duration of the telephone call')
    price = models.DecimalField(max_digits=99, decimal_places=2, verbose_name='Price of the telephone call')

    class Meta:
        verbose_name = 'Telephone bill'
        verbose_name_plural = 'Telephone bills'
