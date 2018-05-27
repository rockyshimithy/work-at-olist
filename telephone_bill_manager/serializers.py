#!/usr/bin/env python
# -*- coding: utf-8 -*-

from rest_framework import serializers

from .models import TelephoneBill


class TelephoneBillSerializer(serializers.ModelSerializer):

    subscriber = serializers.RegexField(r'\d{10,11}$', max_length=11, min_length=10, required=True,
                                        help_text='Subscriber telephone number')
    period = serializers.DateField(help_text='Period of the telephone bill')

    # TODO: Fix start_date, start_time
    destination = serializers.RegexField(r'\d{10,11}$', max_length=11, min_length=10,
                                         help_text='Telephone number that received the call')
    start_date = serializers.DateField(help_text='Start date of the telephone bill')
    start_time = serializers.DateTimeField(help_text='Start time of the telephone bill')
    duration = serializers.DurationField(help_text='Duration of the telephone call')
    price = serializers.DecimalField(max_digits=99, decimal_places=2, help_text='Price of the telephone call')

    def validate(self, data):
        pass

    class Meta:
        model = TelephoneBill
        fields = ('id', 'subscriber', 'period', 'destination', 'start_date', 'start_time', 'duration', 'price')
