import requests
def getLocation(ip):
    r = requests.get('https://ipinfo.io/{ip}/json'.format(ip=ip)).json()
    return {
        'city': r['city'],
        'loc': r['loc']
    }
print(getLocation('123.20.217.83'))