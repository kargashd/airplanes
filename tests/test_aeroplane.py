import os
import sys
from unittest.mock import patch
import pytest
from src.aeroplane import Aeroplane
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))


class TestAeroplane:

    def test_create_aeroplane(self):
        """Тест создания самолёта"""
        plane = Aeroplane("abc123", "Ea1", "Russia", 100.0, 2000.0, 80.0)
        assert plane.icao24 == "abc123"
        assert plane.callsign == "Ea1"
        assert plane.origin_country == "Russia"
        assert plane.altitude == 100.0
        assert plane.velocity == 2000.0
        assert plane.heading == 80.0

    def test_validate_altitude_negative(self):
        """Тест на отрицательную высоту"""
        with pytest.raises(ValueError, match="Высота не должна быть отрицательной"):
            Aeroplane("abc123", "Ea1", "Russia", -100.0, 2000.0, 80.0)

    def test_validate_velocity_negative(self):
        """Тест на отрицательную скорость"""
        with pytest.raises(ValueError, match="Скорость не может быть отрицательной"):
            Aeroplane("abc123", "Ea1", "Russia", 100.0, -2000.0, 80.0)

    def test_validate_heading_out_of_range(self):
        """Тест на курс вне диапазона 0-360"""
        with pytest.raises(ValueError, match="Курс не может быть отрицательным или больше 360"):
            Aeroplane("abc123", "Ea1", "Russia", 100.0, 200.0, 400.0)

    @patch("src.aeroplane.Aeroplane._validate_altitude")
    def test_mock_validate_altitude(self, mock_validate):
        """Тест с mock: подмена валидации высоты."""
        mock_validate.return_value = 5000.0
        plane = Aeroplane("abc123", "CALL1", "USA", 10000.0, 200.0, 90.0)
        assert plane.altitude == 5000.0
        mock_validate.assert_called_once_with(10000.0)

    @patch("src.aeroplane.Aeroplane._validate_velocity")
    def test_mock_validate_velocity(self, mock_validate):
        """Тест с mock: подмена валидации скорости."""
        mock_validate.return_value = 300.0
        plane = Aeroplane("abc123", "CALL1", "USA", 10000.0, 200.0, 90.0)
        assert plane.velocity == 300.0
        mock_validate.assert_called_once_with(200.0)
