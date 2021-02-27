from requests import get


def routing_info():
    print('We <3 MANRS')


def get_external_ip():
    # ip = get('https://api.ipify.org').text
    ip = get('https://api64.ipify.org/').text
    # print('My public IP address is: {}'.format(ip))
    return ip
