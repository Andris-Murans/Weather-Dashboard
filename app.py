import streamlit as st

from api_client import WeatherDataClient
from chart_strategy import get_chart_strategy


CITIES = {
    "Rīga": {
        "latitude": 56.9496,
        "longitude": 24.1052
    },
    "Liepāja": {
        "latitude": 56.5047,
        "longitude": 21.0108
    },
    "Daugavpils": {
        "latitude": 55.8747,
        "longitude": 26.5362
    }
}


st.title("Weather Dashboard")

st.write(
    "This dashboard shows real weather forecast data from Open-Meteo."
)

selected_city = st.selectbox(
    "Choose city",
    list(CITIES.keys())
)

selected_data_type = st.selectbox(
    "Choose data type",
    [
        "Temperature",
        "Wind Speed"
    ]
)

city_data = CITIES[selected_city]

client = WeatherDataClient()

weather = client.fetch_weather(
    city_data["latitude"],
    city_data["longitude"]
)

if weather is None:
    st.error("Could not load weather data. Please try again later.")

else:
    weather.city = selected_city
    country_info = client.fetch_country_info(
        "Latvia"
    )

    st.subheader(f"Weather data for {weather.city}")

    if country_info:

        st.write(
            "Country:",
            country_info["country"]
        )

        st.write(
            "Capital:",
            country_info["capital"]
        )

        st.write(
            "Region:",
            country_info["region"]
        )

        st.write(
            "Population:",
            country_info["population"]
        )

    st.write("Average temperature:", weather.average_temperature(), "°C")
    st.write("Average wind speed:", weather.average_wind_speed(), "km/h")

    strategy = get_chart_strategy(selected_data_type)

    fig = strategy.create_chart(weather)

    st.pyplot(fig)
