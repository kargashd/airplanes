import sys
import os
import json
from unittest.mock import patch
from src.file import JSONSaver
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))


class TestJSONSaver:

    def test_add_aeroplane(self, tmp_path):
        """Тест добавления самолёта в файл."""
        filename = tmp_path / "test.json"
        saver = JSONSaver(str(filename))
        aeroplane = {"icao24": "123", "callsign": "CALL1"}
        saver.add_aeroplane(aeroplane)
        with open(filename, "r", encoding="utf-8") as f:
            data = json.load(f)
        assert len(data) == 1
        assert data[0]["icao24"] == "123"

    def test_add_aeroplane_no_duplicate(self, tmp_path):
        """Тест проверяет, что дубликат не добавляется."""
        filename = tmp_path / "test.json"
        saver = JSONSaver(str(filename))
        aeroplane = {"icao24": "123", "callsign": "CALL1"}
        saver.add_aeroplane(aeroplane)
        saver.add_aeroplane(aeroplane)
        with open(filename, "r", encoding="utf-8") as f:
            data = json.load(f)
        assert len(data) == 1

    def test_get_aeroplanes_all(self, tmp_path):
        """Тест получения всех самолётов из файла."""
        filename = tmp_path / "test.json"
        saver = JSONSaver(str(filename))
        saver.add_aeroplane({"icao24": "123"})
        saver.add_aeroplane({"icao24": "456"})
        result = saver.get_aeroplanes()
        assert len(result) == 2

    def test_get_aeroplanes_filtered(self, tmp_path):
        """Тест получения самолётов по фильтру."""
        filename = tmp_path / "test.json"
        saver = JSONSaver(str(filename))
        saver.add_aeroplane({"icao24": "123", "origin_country": "USA"})
        saver.add_aeroplane({"icao24": "456", "origin_country": "Russia"})
        result = saver.get_aeroplanes(origin_country="USA")
        assert len(result) == 1
        assert result[0]["icao24"] == "123"

    def test_delete_aeroplane(self, tmp_path):
        """Тест удаления самолёта из файла."""
        filename = tmp_path / "test.json"
        saver = JSONSaver(str(filename))
        saver.add_aeroplane({"icao24": "123"})
        saver.add_aeroplane({"icao24": "456"})
        saver.delete_aeroplane(icao24="123")
        result = saver.get_aeroplanes()
        assert len(result) == 1
        assert result[0]["icao24"] == "456"

    @patch("src.file.JSONSaver._load_data")
    def test_add_aeroplane_mock(self, mock_load):
        """Тест с mock: проверяет вызов _load_data."""
        mock_load.return_value = []
        saver = JSONSaver("test.json")
        aeroplane = {"icao24": "123"}
        saver.add_aeroplane(aeroplane)
        mock_load.assert_called_once()
