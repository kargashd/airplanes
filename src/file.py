import json
import os
from typing import List, Dict, Any
from src.abstract_file import AbstractFile


class JSONSaver(AbstractFile):
    """Класс для работы с файлами в формате JSON"""

    def __init__(self, filename: str = "aeroplanes.json"):
        """Конструктор класса JSONSaver"""
        self._filename = filename
        self._ensure_file_exists()

    def _ensure_file_exists(self) -> None:
        """Создаёт файл, если он не существует"""
        if not os.path.exists(self._filename):
            with open(self._filename, "w", encoding="utf-8") as f:
                json.dump([], f)

    def _load_data(self) -> List[Dict[str, Any]]:
        """Загружает данные из JSON-файла"""
        with open(self._filename, "r", encoding="utf-8") as f:
            return json.load(f)

    def _save_data(self, data: List[Dict[str, Any]]) -> None:
        """Сохраняет данные в JSON-файл"""
        with open(self._filename, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=2)

    def add_aeroplane(self, aeroplane: Dict[str, Any]) -> None:
        """Добавляет информацию о самолёте в файл"""
        data = self._load_data()

        for item in data:
            if item.get("icao24") == aeroplane.get("icao24"):
                return

        data.append(aeroplane)
        self._save_data(data)

    def get_aeroplanes(self, **filters) -> List[Dict[str, Any]]:
        """Получает данные из файла по указанным критериям"""
        data = self._load_data()

        if not filters:
            return data

        result = []
        for item in data:
            match = True
            for key, value in filters.items():
                if item.get(key) != value:
                    match = False
                    break
            if match:
                result.append(item)
        return result

    def delete_aeroplane(self, **criteria) -> None:
        """Удаляет информацию о самолётах по указанным критериям"""
        data = self._load_data()

        if not criteria:
            return

        new_data = []
        for item in data:
            keep = True
            for key, value in criteria.items():
                if item.get(key) == value:
                    keep = False
                    break
            if keep:
                new_data.append(item)

        self._save_data(new_data)
