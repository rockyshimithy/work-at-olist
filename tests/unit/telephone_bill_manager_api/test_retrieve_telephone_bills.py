#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json
import pytest


@pytest.mark.django_db
def test_success_get_bill(client, bill):
    data = {'subscriber': 12345678900,
            'period': '2016-02'}

    response = client.get('/calls/', data=json.dumps(data), content_type='application/json')

    assert response.status_code == 200
