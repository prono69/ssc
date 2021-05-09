DATACENTERS = {
    'DC1': {'v4': '149.154.175.53', 'v6': '2001:b28:f23d:f001::a'},
    'DC2': {'v4': '149.154.167.51', 'v6': '2001:67c:4e8:f002::a'},
    'DC3': {'v4': '149.154.175.100', 'v6': '2001:b28:f23d:f003::a'},
    'DC4': {'v4': '149.154.167.91', 'v6': '2001:67c:4e8:f004::a'},
    'DC5': {'v4': '91.108.56.130', 'v6': '2001:b28:f23f:f005::a'},
    'TDC1': {'v4': '149.154.175.10', 'v6': '2001:b28:f23d:f001::e'},
    'TDC2': {'v4': '149.154.167.40', 'v6': '2001:67c:4e8:f002::e'},
    'TDC3': {'v4': '149.154.175.117', 'v6': '2001:b28:f23d:f003::e'},
}


def get_dc(dc_id: int, test_mode: bool) -> dict:
    dc = f'DC{dc_id}'
    if test_mode:
        dc = 'T' + dc
    if dc in DATACENTERS:
        return DATACENTERS[dc]
    raise Exception


def get_ipv4(dc_id: int, test_mode: bool = False) -> str:
    return get_dc(dc_id, test_mode)['v4']


def get_ipv6(dc_id: int, test_mode: bool = False) -> str:
    return get_dc(dc_id, test_mode)['v6']
