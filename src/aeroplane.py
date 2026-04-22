from typing import Any, Dict, List


class Aeroplane:
    """Класс для работы с информацией о самолёте"""

    __slots__ = ("icao24", "callsign", "origin_country", "altitude", "velocity", "heading")

    def __init__(
        self, icao24: str, callsign: str, origin_country: str, altitude: float, velocity: float, heading: float
    ):
        """Конструктор класса Aeroplane"""
        self.icao24 = icao24
        self.callsign = callsign
        self.origin_country = origin_country
        self.altitude = self._validate_altitude(altitude)
        self.velocity = self._validate_velocity(velocity)
        self.heading = self._validate_heading(heading)

    @staticmethod
    def _validate_altitude(altitude: float) -> float:
        """Проверяет, что высота не отрицательная"""
        if altitude < 0:
            raise ValueError(f"Высота не должна быть отрицательной: {altitude}")
        return altitude

    @staticmethod
    def _validate_velocity(velocity: float) -> float:
        """Проверяет, что скорость не отрицательная"""
        if velocity < 0:
            raise ValueError(f"Скорость не может быть отрицательной: {velocity}")
        return velocity

    @staticmethod
    def _validate_heading(heading: float) -> float:
        """Проверяет, что курс не в диапозоне от 0 до 360"""
        if heading < 0 or heading > 360:
            raise ValueError(f"Курс не может быть отрицательным или больше 360: {heading}")
        return heading

    def __lt__(self, other: "Aeroplane") -> bool:  # Магический метод 'less than' - меньше чем
        """Сравнение по высоте: меньше"""
        return self.altitude < other.altitude

    def __gt__(self, other: "Aeroplane") -> bool:  # Магический метод 'greater than' - больше чем
        """Сравнение по высоте: больше"""
        return self.altitude > other.altitude

    def __eq__(self, other: "Aeroplane") -> bool:  # Магический метод 'equal
        """Сравнение по высоте: равно"""
        return self.altitude == other.altitude

    def plane_faster(self, other: "Aeroplane") -> bool:
        """Сравнение по скорости: быстрее"""
        return self.velocity > other.velocity

    def plane_slower(self, other: "Aeroplane") -> bool:
        """Сравнение по скорости: медленнее"""
        return self.velocity < other.velocity

    def plane_equal(self, other: "Aeroplane") -> bool:
        """Сравнение по скорости: равно"""
        return self.velocity == other.velocity

    @classmethod
    def cast_to_object_list(cls, data: List[Dict[str, Any]]) -> List["Aeroplane"]:
        """Преобразует список словарей в список объектов Aeroplane"""
        result = []
        for item in data:
            result.append(
                cls(
                    icao24=item.get("icao24", ""),
                    callsign=item.get("callsign", ""),
                    origin_country=item.get("origin_country", ""),
                    altitude=item.get("altitude", 0.0),
                    velocity=item.get("velocity", 0.0),
                    heading=item.get("heading", 0.0),
                )
            )
        return result
