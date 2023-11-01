import requests
def getLocation(ip):
    r = requests.get('https://ipinfo.io/{ip}/json'.format(ip=ip)).json()
    return {
        'city': r['city'],
        'loc': r['loc']
    }
print(getLocation('123.20.217.83'))
def getGrid(loc):
    r = requests.get('https://api.weather.gov/points/{loc}'.format(loc=loc)).json()
    return r
print(getGrid(getLocation('184.193.202.198')['loc']))