#!/usr/bin/env python3

import hxlm.routing

# hxlm.routing.routing_info()
# print(hxlm.routing.get_external_ip())

def test_get_external_ip():
    example1 = hxlm.routing.get_external_ip()

    assert type(example1) is str

    # At least is not empty
    assert len(example1) > 5