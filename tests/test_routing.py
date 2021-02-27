#!/usr/bin/env python3

import hxlm.routing

# hxlm.routing.routing_info()
# print(hxlm.routing.get_external_ip())


def test_get_external_ip():
    example1 = hxlm.routing.get_external_ip()

    assert type(example1) is str

    # At least is not empty
    assert len(example1) > 5


def test_request_cache_resource():
    please = hxlm.routing.request_cache_resource(
            url='https://example.org/dataset/data.csv',
            hpeer='192.0.2.0')
    assert please['please'] == 'HRCACHE'


def test_request_priority_access():
    please=hxlm.routing.request_priority_access(
        url = 'https://example.org/dataset/data.csv',
        requester = '192.0.2.0')
    assert please['please'] == 'HRQOSME'
