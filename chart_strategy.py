import matplotlib.pyplot as plt


class ChartStrategy:
    def create_chart(self, weather_data):
        raise NotImplementedError("This method must be implemented in child classes")


class TemperatureChartStrategy(ChartStrategy):
    def create_chart(self, weather_data):
        fig, ax = plt.subplots()

        ax.plot(
            [
                time.split("T")[1]
                for time in weather_data.time_data
            ],
            weather_data.temperature_data,
            marker="o"
        )

        ax.set_title(f"Temperature in {weather_data.city}")
        ax.set_xlabel("Time")
        ax.set_ylabel("Temperature °C")
        ax.grid(True)

        plt.xticks(rotation=45)

        return fig


class WindChartStrategy(ChartStrategy):
    def create_chart(self, weather_data):
        fig, ax = plt.subplots()

        ax.plot(
            [
                time.split("T")[1]
                for time in weather_data.time_data
            ],
            weather_data.wind_speed_data,
            marker="o"
        )

        ax.set_title(f"Wind speed in {weather_data.city}")
        ax.set_xlabel("Time")
        ax.set_ylabel("Wind speed km/h")
        ax.grid(True)

        plt.xticks(rotation=45)

        return fig

def get_chart_strategy(data_type):

    if data_type == "Temperature":
        return TemperatureChartStrategy()

    if data_type == "Wind Speed":
        return WindChartStrategy()

    raise ValueError("Unknown chart type")
