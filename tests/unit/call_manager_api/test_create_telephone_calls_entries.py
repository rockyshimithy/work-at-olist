#!/usr/bin/env python
# -*- coding: utf-8 -*-

from datetime import datetime
import json
import pytest
import pytz

from call_manager.models import TelephoneCall


@pytest.mark.django_db
def test_success_post_calls(client):
    data = {'type': 'start',
            'timestamp': '2016-02-29T14:02:02Z',
            'call_id': 1,
            'source': 12345678900,
            'destination': 12345678900}

    response = client.post('/calls/', data=json.dumps(data), content_type='application/json')

    telephone_calls = TelephoneCall.objects.all()

    assert response.status_code == 201
    assert data['type'] == telephone_calls[0].type
    assert datetime(2016, 2, 29, 14, 2, 2, tzinfo=pytz.utc) == telephone_calls[0].timestamp
    assert data['call_id'] == telephone_calls[0].call_id
    assert data['source'] == telephone_calls[0].source
    assert data['destination'] == telephone_calls[0].destination


@pytest.mark.django_db
def test_fail_post_calls_wrong_type(client):
    data = {'type': 'count',
            'timestamp': '2016-02-29T14:02:02Z',
            'call_id': 1,
            'source': 12345678900,
            'destination': 12345678900}

    response = client.post('/calls/', data=json.dumps(data), content_type='application/json')

    telephone_calls = TelephoneCall.objects.all()

    assert response.status_code == 400
    assert len(telephone_calls) == 0
    assert response.json()['type'][0] == '"count" is not a valid choice.'


@pytest.mark.django_db
def test_fail_post_calls_null_type(client):
    data = {'type': None,
            'timestamp': '2016-02-29T14:02:02Z',
            'call_id': 1,
            'source': 12345678900,
            'destination': 12345678900}

    response = client.post('/calls/', data=json.dumps(data), content_type='application/json')

    telephone_calls = TelephoneCall.objects.all()

    assert response.status_code == 400
    assert len(telephone_calls) == 0
    assert response.json()['type'][0] == 'This field may not be null.'


@pytest.mark.django_db
def test_fail_post_calls_no_type(client):
    data = {'timestamp': '2016-02-29T14:02:02Z',
            'call_id': 1,
            'source': 12345678900,
            'destination': 12345678900}

    response = client.post('/calls/', data=json.dumps(data), content_type='application/json')

    telephone_calls = TelephoneCall.objects.all()

    assert response.status_code == 400
    assert len(telephone_calls) == 0
    assert response.json()['type'][0] == 'This field is required.'


@pytest.mark.django_db
def test_fail_post_calls_wrong_timestamp(client):
    data = {'type': 'start',
            'timestamp': '2016-02-29',
            'call_id': 1,
            'source': 12345678900,
            'destination': 12345678900}

    response = client.post('/calls/', data=json.dumps(data), content_type='application/json')

    telephone_calls = TelephoneCall.objects.all()

    assert response.status_code == 400
    assert len(telephone_calls) == 0
    assert response.json()['timestamp'][0] == 'Datetime has wrong format. Use one of these formats instead:' \
                                              ' YYYY-MM-DDThh:mm[:ss[.uuuuuu]][+HH:MM|-HH:MM|Z].'


@pytest.mark.django_db
def test_fail_post_calls_null_timestamp(client):
    data = {'type': 'end',
            'timestamp': None,
            'call_id': 1,
            'source': 12345678900,
            'destination': 12345678900}

    response = client.post('/calls/', data=json.dumps(data), content_type='application/json')

    telephone_calls = TelephoneCall.objects.all()

    assert response.status_code == 400
    assert len(telephone_calls) == 0
    assert response.json()['timestamp'][0] == 'This field may not be null.'


@pytest.mark.django_db
def test_fail_post_calls_no_timestamp(client):
    data = {'type': 'end',
            'call_id': 1,
            'source': 12345678900,
            'destination': 12345678900}

    response = client.post('/calls/', data=json.dumps(data), content_type='application/json')

    telephone_calls = TelephoneCall.objects.all()

    assert response.status_code == 400
    assert len(telephone_calls) == 0
    assert response.json()['timestamp'][0] == 'This field is required.'


@pytest.mark.django_db
def test_fail_post_calls_wrong_call_id(client):
    data = {'type': 'start',
            'timestamp': '2016-02-29T14:02:02Z',
            'call_id': 'xyz',
            'source': 12345678900,
            'destination': 12345678900}

    response = client.post('/calls/', data=json.dumps(data), content_type='application/json')

    telephone_calls = TelephoneCall.objects.all()

    assert response.status_code == 400
    assert len(telephone_calls) == 0
    assert response.json()['call_id'][0] == 'A valid integer is required.'


@pytest.mark.django_db
def test_fail_post_calls_null_call_id(client):
    data = {'type': 'end',
            'timestamp': '2016-02-29T14:02:02Z',
            'call_id': None,
            'source': 12345678900,
            'destination': 12345678900}

    response = client.post('/calls/', data=json.dumps(data), content_type='application/json')

    telephone_calls = TelephoneCall.objects.all()

    assert response.status_code == 400
    assert len(telephone_calls) == 0
    assert response.json()['call_id'][0] == 'This field may not be null.'


@pytest.mark.django_db
def test_fail_post_calls_no_call_id(client):
    data = {'type': 'end',
            'timestamp': '2016-02-29T14:02:02Z',
            'source': 12345678900,
            'destination': 12345678900}

    response = client.post('/calls/', data=json.dumps(data), content_type='application/json')

    telephone_calls = TelephoneCall.objects.all()

    assert response.status_code == 400
    assert len(telephone_calls) == 0
    assert response.json()['call_id'][0] == 'This field is required.'


@pytest.mark.django_db
def test_fail_post_calls_wrong_source_and_destination(client):
    data = {'type': 'start',
            'timestamp': '2016-02-29T14:02:02Z',
            'call_id': 1,
            'source': 12345678,
            'destination': 123456789000}

    response = client.post('/calls/', data=json.dumps(data), content_type='application/json')

    telephone_calls = TelephoneCall.objects.all()

    assert response.status_code == 400
    assert len(telephone_calls) == 0
    assert response.json()['source'][0] == 'Ensure this field has at least 10 characters.'
    assert response.json()['destination'][0] == 'Ensure this field has no more than 11 characters.'


@pytest.mark.django_db
def test_fail_post_calls_null_source_and_destination(client):
    data = {'type': 'start',
            'timestamp': '2016-02-29T14:02:02Z',
            'call_id': 1,
            'source': None,
            'destination': None}

    response = client.post('/calls/', data=json.dumps(data), content_type='application/json')

    telephone_calls = TelephoneCall.objects.all()

    assert response.status_code == 400
    assert len(telephone_calls) == 0
    assert response.json()['source'][0] == 'This field may not be null.'
    assert response.json()['destination'][0] == 'This field may not be null.'


@pytest.mark.django_db
def test_fail_post_calls_type_start_no_source_and_destination(client):
    data = {'type': 'start',
            'timestamp': '2016-02-29T14:02:02Z',
            'call_id': 1}

    response = client.post('/calls/', data=json.dumps(data), content_type='application/json')

    telephone_calls = TelephoneCall.objects.all()

    assert response.status_code == 400
    assert len(telephone_calls) == 0
    assert response.json()['non_field_errors'][0] == 'This field is required when type is "start"'


@pytest.mark.django_db
def test_success_post_calls_type_end_no_source_and_destination(client):
    data = {'type': 'end',
            'timestamp': '2016-02-29T14:02:02Z',
            'call_id': 1}

    response = client.post('/calls/', data=json.dumps(data), content_type='application/json')

    telephone_calls = TelephoneCall.objects.all()

    assert response.status_code == 201
    assert data['type'] == telephone_calls[0].type
    assert datetime(2016, 2, 29, 14, 2, 2, tzinfo=pytz.utc) == telephone_calls[0].timestamp
    assert data['call_id'] == telephone_calls[0].call_id
    assert telephone_calls[0].source is None
    assert telephone_calls[0].destination is None


@pytest.mark.django_db
def test_success_post_calls_type_end_with_source_and_destination(client):
    data = {'type': 'end',
            'timestamp': '2016-02-29T14:02:02Z',
            'call_id': 1,
            'source': 1234567800,
            'destination': 1234567890}

    response = client.post('/calls/', data=json.dumps(data), content_type='application/json')

    telephone_calls = TelephoneCall.objects.all()

    assert response.status_code == 201
    assert data['type'] == telephone_calls[0].type
    assert datetime(2016, 2, 29, 14, 2, 2, tzinfo=pytz.utc) == telephone_calls[0].timestamp
    assert data['call_id'] == telephone_calls[0].call_id
    assert telephone_calls[0].source is None
    assert telephone_calls[0].destination is None
