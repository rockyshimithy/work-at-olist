#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json
import pytest


@pytest.mark.django_db
def test_success_get_bill(client, telephone_bill):
    response = client.get('/bills/12345678900/', content_type='application/json')

    assert response.status_code == 200

#
# @pytest.mark.django_db
# def test_fail_get_bill_without_subscriber(client, telephone_bill):
#     response = client.get('/bills//', content_type='application/json')
#
#     assert response.status_code == 400
#
#
# @pytest.mark.django_db
# def test_fail_get_bill_wrong_subscriber(client, telephone_bill):
#     response = client.get('/bills/xpto/', content_type='application/json')
#
#     assert response.status_code == 400
#
#
# @pytest.mark.django_db
# def test_fail_get_bill_subscriber_does_not_exist(client, telephone_bill):
#     response = client.get('/bills/xpto/', content_type='application/json')
#
#     assert response.status_code == 400