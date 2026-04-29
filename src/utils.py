from typing import List
from src.aeroplane import Aeroplane


def filter_by_country(aeroplanes: List[Aeroplane], country: str) -> List[Aeroplane]:
    """Фильтрует самолёты по стране регистрации"""
    return [p for p in aeroplanes if p.origin_country == country]


def sort_by_altitude(aeroplanes: List[Aeroplane], reverse: bool = True) -> List[Aeroplane]:
    """Сортирует самолёты по высоте"""
    return sorted(aeroplanes, key=lambda p: p.altitude, reverse=reverse)


def sort_by_velocity(aeroplanes: List[Aeroplane], reverse: bool = True) -> List[Aeroplane]:
    """Сортирует самолёты по скорости"""
    return sorted(aeroplanes, key=lambda p: p.velocity, reverse=reverse)


def get_top_n(aeroplanes: List[Aeroplane], n: int) -> List[Aeroplane]:
    """Возвращает топ N самолётов по высоте"""
    if n <= 0:
        return []
    sorted_planes = sort_by_altitude(aeroplanes, reverse=True)
    return sorted_planes[:n]


def get_by_altitude_range(aeroplanes: List[Aeroplane], min_alt: float, max_alt: float) -> List[Aeroplane]:
    """Возвращает самолёты в диапазоне высот"""
    return [p for p in aeroplanes if min_alt <= p.altitude <= max_alt]
