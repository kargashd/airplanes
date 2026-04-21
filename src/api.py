import requests
from src.abstract_api import AbstractAPI


class AeroplanesAPI(AbstractAPI):
    """Класс для работы с API nominatim и opensky"""

    def __init__(self):
        self._base_url_nominatim = "https://nominatim.openstreetmap.org/search"
        self._base_url_opensky = "https://opensky-network.org/api/states/all"

    def _connect(self, url: str, params: dict = None) -> requests.Response:
        """Приватный метод для отправки запроса"""
        response = requests.get(url, params=params, timeout=10)
        response.raise_for_status()
        return response

    def connect(self) -> None:
        """Проверка подключения к API"""
        self._connect(self._base_url_nominatim, {"q": "test", "format": "json"})
        self._connect(self._base_url_opensky)

    def get_country_bounds(self, country_name: str) -> tuple[float, float, float, float]:
        """Получение границ страны"""
        params = {"q": country_name, "format": "json", "limit": 1}
        response = self._connect(self._base_url_nominatim, params)
        data = response.json()

        if not data:
            raise ValueError(f"Страна '{country_name}' не найдена")

        bounds = data[0]["boundingbox"]
        return float(bounds[0]), float(bounds[1]), float(bounds[2]), float(bounds[3])

    def get_aeroplanes(self, country_name: str) -> list[dict]:
        """Получение данных о самолётах"""
        south, north, west, east = self.get_country_bounds(country_name)
        params = {"lamin": south, "lamax": north, "lomin": west, "lomax": east}
        response = self._connect(self._base_url_opensky, params)
        data = response.json()

        result = []
        for state in data.get("states", []):
            result.append({
                "icao24": state[0],
                "callsign": state[1],
                "origin_country": state[2],
                "longitude": state[5],
                "latitude": state[6],
                "altitude": state[7],
                "velocity": state[9],
                "heading": state[10]
            })
        return result
