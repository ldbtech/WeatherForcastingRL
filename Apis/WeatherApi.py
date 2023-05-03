import requests

"""
This API 
"""


def setupWeather(api_key="ad109fd7f5fbf69e5f6ef765b630ffe4", place="New York"):
    params = {"access_key": api_key, "query": place}

    api_result = requests.get("http://api.weatherstack.com/current", params)
    api_response = api_result.json()

    temp = api_response["current"]["temperature"]  # Celcius
    humidity = api_response["current"]["humidity"]
    wind = api_response["current"]["wind_speed"]  # Km/hr

    # print(temp)
    # print(humidity)
    # print(wind)

    return {"temp": temp, "humidity": humidity, "wind": wind}
print(setupWeather())