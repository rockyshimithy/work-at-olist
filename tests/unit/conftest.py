#!/usr/bin/env python
# -*- coding: utf-8 -*-

from datetime import datetime, timedelta
import pytz
import pytest
import factory.django

from telephone_call_manager.models import TelephoneCall
from telephone_bill_manager.models import TelephoneBill


class TelephoneCallFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = TelephoneCall

    type = 'start'
    timestamp = datetime(2016, 2, 29, 14, 2, 2, tzinfo=pytz.utc)
    call_id = 1
    source = 12345678900
    destination = 12345678901


class TelephoneBillFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = TelephoneBill

    subscriber = 12345678900
    period = datetime(2016, 2, 29, tzinfo=pytz.utc)
    destination = 12345678901
    start_date = datetime(2016, 2, 29, tzinfo=pytz.utc)
    start_time = datetime(2016, 2, 29, 14, 2, 2, tzinfo=pytz.utc)
    duration = timedelta(hours=2, minutes=3, seconds=4)
    price = 10.99


@pytest.fixture()
def telephone_call_type_start():
    return TelephoneCallFactory()


@pytest.fixture()
def telephone_call_type_end():
    return TelephoneCallFactory(type='end', source=None, destination=None)


@pytest.fixture()
def telephone_calls(telephone_call_type_start):
    telephone_calls = [
        telephone_call_type_start,
        telephone_call_type_end,
        TelephoneCallFactory(call_id=70, type='start', timestamp='2016-02-29T12:00:00Z'),
        TelephoneCallFactory(call_id=70, type='end', timestamp='2016-02-29T14:00:00Z'),
        TelephoneCallFactory(call_id=71, type='start', timestamp='2017-12-12T15:07:13Z'),
        TelephoneCallFactory(call_id=71, type='end', timestamp='2017-12-12T15:14:56Z'),
        TelephoneCallFactory(call_id=72, type='start', timestamp='2017-12-12T22:47:56Z'),
        TelephoneCallFactory(call_id=72, type='end', timestamp='2017-12-12T22:50:56Z'),
        TelephoneCallFactory(call_id=73, type='start', timestamp='2017-12-12T21:57:13Z'),
        TelephoneCallFactory(call_id=73, type='end', timestamp='2017-12-12T22:10:56Z'),
        TelephoneCallFactory(call_id=74, type='start', timestamp='2017-12-12T04:57:13Z'),
        TelephoneCallFactory(call_id=74, type='end', timestamp='2017-12-12T06:10:56Z'),
        TelephoneCallFactory(call_id=75, type='start', timestamp='2017-12-12T21:57:13Z'),
        TelephoneCallFactory(call_id=75, type='end', timestamp='2017-12-13T22:10:56Z'),
        TelephoneCallFactory(call_id=76, type='start', timestamp='2017-12-12T15:07:58Z'),
        TelephoneCallFactory(call_id=76, type='end', timestamp='2017-12-12T15:12:56Z'),
        TelephoneCallFactory(call_id=77, type='start', timestamp='2018-02-28T21:57:13Z'),
        TelephoneCallFactory(call_id=77, type='end', timestamp='2018-03-01T22:10:56Z'),
    ]

    return telephone_calls


@pytest.fixture()
def telephone_bill():
    return TelephoneBillFactory()

