import argparse
import requests
import datetime

def get_current_weather(latitude, longitude, api_key):
    url = f'https://api.darksky.net/forecast/{api_key}/{latitude},{longitude}'
    response = requests.get(url)
    if response.status_code == 200:
        currently_weather = response.json()['currently']
        time = humanize_timestamp(currently_weather['time'])
        summary = currently_weather['summary']
        temperature = format_fahrenheit_to_celsius(currently_weather['temperature'])
        return {
            'time': time,
            'summary': summary,
            'temperature': temperature
        }
    else:
        return {}

def humanize_timestamp(timestamp):
    return datetime.datetime.fromtimestamp(timestamp).strftime('%d-%m-%Y %H:%M:%S')

def format_fahrenheit_to_celsius(fahrenheit):
    return 5.0/9 * (fahrenheit - 32)

parser = argparse.ArgumentParser(description='A little weather tool by coordinate')
parser.add_argument('latitude', help='a latitude of your choice')
parser.add_argument('longitude', help='a longitude of your choice')
parser.add_argument('-a', '--api-key', help='your API key for the Dark Sky API', default='701781aac440f0d13d611eab98bfc2cc')
args = parser.parse_args()
latitude = args.latitude
longitude = args.longitude
api_key = args.api_key
current_weather = get_current_weather(latitude, longitude, api_key)
print(f"The weather in location right now: {current_weather}.")
