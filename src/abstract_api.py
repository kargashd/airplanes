from abc import ABC, abstractmethod


class AbstractAPI(ABC):
    """Абстрактный класс для работы с API"""

    @abstractmethod
    def connect(self):
        """Подключение к API"""
        pass

    @abstractmethod
    def get_country_bounds(self, country_name: str):
        """Получение координат страны"""
        pass

    @abstractmethod
    def get_aeroplanes(self, country_name: str):
        """Получение информации о самолётах"""
        pass
