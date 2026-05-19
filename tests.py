import pytest

from api_client import WeatherDataClient
from models import WeatherData
from chart_strategy import (
    TemperatureChartStrategy,
    WindChartStrategy,
    get_chart_strategy
)


# TEST 1
# Check if API returns WeatherData object

def test_fetch_weather_returns_object():

    client = WeatherDataClient()

    weather = client.fetch_weather(
        56.9496,
        24.1052
    )

    assert isinstance(weather, WeatherData)


# TEST 2
# Check if temperature data exists

def test_temperature_data_exists():

    client = WeatherDataClient()

    weather = client.fetch_weather(
        56.9496,
        24.1052
    )

    assert len(weather.temperature_data) > 0


# TEST 3
# Check if wind speed data exists

def test_wind_speed_data_exists():

    client = WeatherDataClient()

    weather = client.fetch_weather(
        56.9496,
        24.1052
    )

    assert len(weather.wind_speed_data) > 0


# TEST 4
# Check if average temperature is float

def test_average_temperature():

    client = WeatherDataClient()

    weather = client.fetch_weather(
        56.9496,
        24.1052
    )

    average = weather.average_temperature()

    assert isinstance(average, float)


# TEST 5
# Check if average wind speed is float

def test_average_wind_speed():

    client = WeatherDataClient()

    weather = client.fetch_weather(
        56.9496,
        24.1052
    )

    average = weather.average_wind_speed()

    assert isinstance(average, float)


# TEST 6
# Check if city data contains 24 hours

def test_weather_data_length():

    client = WeatherDataClient()

    weather = client.fetch_weather(
        56.9496,
        24.1052
    )

    assert len(weather.time_data) == 24


# TEST 7
# Check if Temperature strategy is selected

def test_temperature_strategy_selection():

    strategy = get_chart_strategy(
        "Temperature"
    )

    assert isinstance(
        strategy,
        TemperatureChartStrategy
    )


# TEST 8
# Check if Wind strategy is selected

def test_wind_strategy_selection():

    strategy = get_chart_strategy(
        "Wind Speed"
    )

    assert isinstance(
        strategy,
        WindChartStrategy
    )


# TEST 9
# Check invalid chart type

def test_invalid_chart_type():

    with pytest.raises(
        ValueError,
        match="Unknown chart type"
    ):

        get_chart_strategy(
            "Humidity"
        )


# TEST 10
# Check WeatherData object creation with sample data

def test_sample_weather_data():

    weather = WeatherData(
        city="Test City",

        time_data=["00:00", "01:00"],

        temperature_data=[10, 20],

        wind_speed_data=[5, 15]
    )

    assert weather.average_temperature() == 15.0

    assert weather.average_wind_speed() == 10.0


# TEST 11
# Check empty temperature list error

def test_empty_temperature_list():

    weather = WeatherData(
        city="Test City",
        time_data=[],
        temperature_data=[],
        wind_speed_data=[]
    )

    with pytest.raises(ZeroDivisionError):

        weather.average_temperature()


# TEST 12
# Check REST Countries API

def test_country_info():

    client = WeatherDataClient()

    country_info = client.fetch_country_info(
        "Latvia"
    )

    assert country_info["country"] == "Latvia"
       