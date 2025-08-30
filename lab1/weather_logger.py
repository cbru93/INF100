"""Weather logger."""

import requests
from pathlib import Path
from typing import TypedDict
import json

class WeatherLog(TypedDict):
    """Weather log data."""
    time: str
    air_temperature: float

url = "https://api.met.no/weatherapi/nowcast/2.0/complete?lat=60.3894&lon=5.33"
response = requests.get(url, headers={"User-Agent": "no.uib.ii.inf100"}, timeout=10)
data = response.json()
time = data["properties"]["timeseries"][0]["time"]
air_temperature = data["properties"]["timeseries"][0]["data"]["instant"]["details"]["air_temperature"]

script_dir = Path(__file__).parent
weather_log_path = script_dir / 'weather_log.json'
try:
    weather_log = json.loads(weather_log_path.read_text(encoding='utf-8'))
except FileNotFoundError:
    weather_log = []

weather_log_data: list[WeatherLog] = {
    "time": time,
    "air_temp": air_temperature,
}

weather_log.append(weather_log_data)
weather_log_path.write_text(json.dumps(weather_log, indent=4), encoding='utf-8')


# with Path('weather_log.json').open('a', encoding='utf-8') as file:
#     json.dump({'date': date, 'air_temperature': air_temperature}, file)

print(weather_log)
print(time)
print(air_temperature)


