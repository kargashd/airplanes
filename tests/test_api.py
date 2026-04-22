import os
import sys
from unittest.mock import MagicMock, patch
import pytest
from src.api import AeroplanesAPI
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))


class TestAeroplanesAPI:

    @patch("src.api.requests.get")
    def test_connect_success(self, mock_get):
        """Тест успешного подключения"""
        mock_get.return_value = MagicMock(raise_for_status=MagicMock())
        api = AeroplanesAPI()
        api.connect()
        assert mock_get.call_count == 2

    @patch("src.api.requests.get")
    def test_connect_failure(self, mock_get):
        """Тест ошибки подключения"""
        mock_get.side_effect = Exception("Connection_error")
        api = AeroplanesAPI()
        with pytest.raises(Exception):
            api.connect()

    @patch("src.api.requests.get")
    def test_get_country_bounds_success(self, mock_get):
        """Тест получения границ страны"""
        mock_response = MagicMock()
        mock_response.json.return_value = [{"boundingbox": ["55.0", "60.0", "30.0", "40.0"]}]
        mock_get.return_value = mock_response

        api = AeroplanesAPI()
        result = api.get_country_bounds("Russia")

        assert result == (55.0, 60.0, 30.0, 40.0)

    @patch("src.api.requests.get")
    def test_get_country_bounds_not_found(self, mock_get):
        """Тест: страна не найдена"""
        mock_response = MagicMock()
        mock_response.json.return_value = []
        mock_get.return_value = mock_response

        api = AeroplanesAPI()
        with pytest.raises(ValueError, match="Страна 'NotFound' не найдена"):
            api.get_country_bounds("NotFound")

    @patch("src.api.requests.get")
    def test_get_aeroplanes_failure(self, mock_get):
        """Тест ошибки при получении самолётов."""
        mock_bounds = MagicMock()
        mock_bounds.json.return_value = [{"boundingbox": ["55.0", "60.0", "30.0", "40.0"]}]

        mock_get.side_effect = [mock_bounds, Exception("API error")]

        api = AeroplanesAPI()
        with pytest.raises(Exception):
            api.get_aeroplanes("Russia")
