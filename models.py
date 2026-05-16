class WeatherData:

    def __init__(
        self,
        city,
        time_data,
        temperature_data,
        wind_speed_data
    ):

        self.city = city

        self.time_data = time_data

        self.temperature_data = temperature_data

        self.wind_speed_data = wind_speed_data

    def average_temperature(self):

        return round(
            sum(self.temperature_data)
            / len(self.temperature_data),
            2
        )

    def average_wind_speed(self):

        return round(
            sum(self.wind_speed_data)
            / len(self.wind_speed_data),
            2
        )
    