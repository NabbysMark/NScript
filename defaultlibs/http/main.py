import requests

def get(url, params=None, headers=None):
    resp = requests.get(url, params=params, headers=headers)
    return resp.text

def post(url, data=None, json=None, headers=None):
    resp = requests.post(url, data=data, json=json, headers=headers)
    return resp.text

def status(url):
    resp = requests.get(url)
    return resp.status_code
