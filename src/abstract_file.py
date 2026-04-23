from abc import ABC, abstractmethod
from typing import List, Dict, Any


class AbstractFile(ABC):
    """Абстрактный класс для работы с файлами"""

    @abstractmethod
    def add_aeroplane(self, aeroplane: Dict[str, Any]) -> None:
        """Добавляет информацию о самолёте в файл"""
        pass

    @abstractmethod
    def get_aeroplanes(self, **filters) -> List[Dict[str, Any]]:
        """Получает данные из файла по указанным критериям"""
        pass

    @abstractmethod
    def delete_aeroplane(selfself, **criteria) -> None:
        """Удаляет информацию о самолётах по указанным критериям"""
        pass
