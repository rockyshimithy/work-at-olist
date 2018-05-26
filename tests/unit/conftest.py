#!/usr/bin/env python
# -*- coding: utf-8 -*-

from datetime import datetime
import pytz
import pytest
import factory.django

from call_manager.models import TelephoneCall


class TelephoneCallFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = TelephoneCall

    type = 'start'
    timestamp = datetime(2016, 2, 29, 14, 2, 2, tzinfo=pytz.utc)
    call_id = 1
    source = 12345678900
    destination = 12345678901


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
    ]

    return telephone_calls
