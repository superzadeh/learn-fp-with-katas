import collections
import unittest

from weather import (
    load_file,
    compute_temperature_spead,
    convert_temperature_values,
    get_smallest_temperature_spread,
)

compare = lambda x, y: collections.Counter(x) == collections.Counter(y)


class DataMuningKata(unittest.TestCase):
    def test_weather_loads_file(self):
        # Arrange
        file_name = "weather.dat"

        # Act
        result = load_file(file_name)

        # Assert
        assert result is not None

    def test_weather_removes_summery(self):
        # Arrange
        file_name = "weather.dat"

        # Act
        result = load_file(file_name)

        # Assert
        assert len(result[result.Dy == "mo"]) == 0

    def test_weather_loads_all_columns(self):
        # Arrange
        data = load_file("weather.dat")
        # Act
        result = len(data.columns)
        # Assert
        assert result == 17

    def test_weather_loads_header(self):
        # Arrange
        data = load_file("weather.dat")
        expected_headers = [
            "Dy",
            "MxT",
            "MnT",
            "AvT",
            "HDDay",
            "AvDP",
            "1HrP",
            "TPcpn",
            "WxType",
            "PDir",
            "AvSp",
            "Dir",
            "MxS",
            "SkyC",
            "MxR",
            "MnR",
            "AvSLP",
        ]

        # Act
        actual_headers = data.columns

        # Assert
        assert compare(actual_headers, expected_headers)

    def test_weather_should_compute_temperature_spread(self):
        # Arrange
        data = load_file("weather.dat")

        # Act
        data["temperature_spread"] = compute_temperature_spead(
            convert_temperature_values(data["MxT"]),
            convert_temperature_values(data["MnT"]),
        )

        # Assert
        assert data.iloc[0]["temperature_spread"] == 29
        assert data.iloc[8]["temperature_spread"] == 54
        assert data.iloc[25]["temperature_spread"] == 33

    def test_weather_convert_temperature_values(self):
        # Arrange
        data = load_file("weather.dat")

        # Act
        data["MnT"] = convert_temperature_values(data["MnT"])

        # Assert
        assert data["MnT"][8] == 32

    def test_weather_gets_smallest_temperature_spread(self):
        # Arrange
        data = load_file("weather.dat")

        # Act
        smallest_spread = get_smallest_temperature_spread(data)

        # Assert
        assert smallest_spread == 13
