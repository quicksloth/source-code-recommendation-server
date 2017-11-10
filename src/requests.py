import requests

def get_source_codes(data):
    url = 'http://0.0.0.0:1111/crawl'
    headers = {'Content-Type': 'application/json'}
    print('going to request new version')
    requests.request(url=url, method='GET', data=data, headers=headers)