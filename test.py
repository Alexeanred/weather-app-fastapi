import requests
def getTemp():
    r = requests.get('https://api.weather.gov/gridpoints/TOP/31,80/forecast').json()
    day_temp = r['properties']['periods'][0]
    return {
        'temperature': day_temp['temperature'],
        'wind_speed': day_temp['windSpeed'],
        'status': day_temp['shortForecast'],
        'icon': day_temp['icon'],
        'time': day_temp['startTime']
    }

print(getTemp()['time'].split("T")[0])
