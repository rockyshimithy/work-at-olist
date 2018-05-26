#!/usr/bin/env python
# -*- coding: utf-8 -*-

from rest_framework import serializers

from .models import TelephoneCall


class TelephoneCallSerializer(serializers.ModelSerializer):

    type = serializers.ChoiceField(choices=('start', 'end'), help_text='Record type. Options are "start" or "end"')
    timestamp = serializers.DateTimeField(required=True, help_text='Timestamp of the event')
    call_id = serializers.IntegerField(min_value=1, required=True, help_text='Unique identifier for the call')
    source = serializers.RegexField(r'\d{10,11}$', max_length=11, min_length=10, required=False,
                                    help_text=('This field is required when type is "start". '
                                               'Telephone number that originated the call'))
    destination = serializers.RegexField(r'\d{10,11}$', max_length=11, min_length=10, required=False,
                                         help_text=('This field is required when type is "start". '
                                                    'Telephone number that received the call'))

    def validate(self, data):
        if data['type'] == 'start':
            if 'source' not in data or 'destination' not in data:
                raise serializers.ValidationError(
                    'This field is required when type is "start"')
        else:
            if 'source' in data or 'destination' in data:
                data['source'] = None
                data['destination'] = None
        return data

    class Meta:
        model = TelephoneCall
        fields = ('id', 'type', 'timestamp', 'call_id', 'source', 'destination')
