import requests
from models import WeatherData


class WeatherDataClient:

    def fetch_weather(self, latitude, longitude):

        url = (
            f"https://api.open-meteo.com/v1/forecast?"
            f"latitude={latitude}&longitude={longitude}"
            f"&hourly=temperature_2m,wind_speed_10m"
        )

        try:
            response = requests.get(url)

            response.raise_for_status()

            data = response.json()

            return WeatherData(
                city="Unknown",
                time_data=data["hourly"]["time"][:24],
                temperature_data=data["hourly"]["temperature_2m"][:24],
                wind_speed_data=data["hourly"]["wind_speed_10m"][:24]
            )

        except requests.exceptions.RequestException as error:
            print(f"API request failed: {error}")
            return None

        except KeyError:
            print("Unexpected API response format")
            return None

    def fetch_country_info(self, country_name):

        url = (
            f"https://restcountries.com/v3.1/name/"
            f"{country_name}"
        )

        try:

            response = requests.get(url)

            response.raise_for_status()

            data = response.json()

            country = data[0]

            return {
                "country": country["name"]["common"],

                "capital": country["capital"][0],

                "region": country["region"],

                "population": country["population"]
            }

        except requests.exceptions.RequestException as error:

            print(
                f"Country API request failed: {error}"
            )

            return None

        except (
            KeyError,
            IndexError
        ):

            print(
                "Unexpected country API response format"
            )

            return None       
        