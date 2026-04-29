import sys
import os
from src.aeroplane import Aeroplane
from src.utils import (
    filter_by_country,
    sort_by_altitude,
    sort_by_velocity,
    get_top_n,
    get_by_altitude_range
)
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))


def test_filter_by_country():
    """Тест проверяющий фильтрацию самолётов по стране"""
    aeroplanes = [
        Aeroplane("oli", "ne5", "USA", 1000.0, 100.0, 30.0),
        Aeroplane("via", "ba1", "Russia", 1000.0, 100.0, 30.0),
    ]

    filter_by_country(aeroplanes, "Russia")
    assert [
        Aeroplane("via", "ba1", "Russia", 1000.0, 100.0, 30.0),
        Aeroplane("oli", "ne5", "USA", 1000.0, 100.0, 30.0)
    ]


def test_sort_by_altitude():
    aeroplanes = [
        Aeroplane("oli", "ne5", "USA", 1100.0, 100.0, 30.0),
        Aeroplane("via", "ba1", "Russia", 1350.0, 100.0, 30.0),
        Aeroplane("via", "ba1", "Nigeria", 1200.0, 100.0, 30.0),
        Aeroplane("via", "ba1", "Latvia", 1110.0, 100.0, 30.0)
    ]

    sort_by_altitude(aeroplanes)
    assert [
        Aeroplane("oli", "ne5", "USA", 1100.0, 100.0, 30.0),
        Aeroplane("via", "ba1", "Latvia", 1110.0, 100.0, 30.0),
        Aeroplane("via", "ba1", "Nigeria", 1200.0, 100.0, 30.0),
        Aeroplane("via", "ba1", "Russia", 1350.0, 100.0, 30.0),
    ]


def test_sort_by_velocity():
    aeroplanes = [
        Aeroplane("oli", "ne5", "USA", 1100.0, 80.0, 30.0),
        Aeroplane("via", "ba1", "Russia", 1350.0, 111.0, 30.0),
        Aeroplane("via", "ba1", "Nigeria", 1200.0, 110.0, 30.0),
        Aeroplane("via", "ba1", "Latvia", 1110.0, 300.0, 30.0)
    ]

    sort_by_velocity(aeroplanes)
    assert [
        Aeroplane("oli", "ne5", "USA", 1100.0, 80.0, 30.0),
        Aeroplane("via", "ba1", "Nigeria", 1200.0, 110.0, 30.0),
        Aeroplane("via", "ba1", "Russia", 1350.0, 111.0, 30.0),
        Aeroplane("via", "ba1", "Latvia", 1110.0, 300.0, 30.0)
    ]


def test_get_top_n():
    aeroplanes = [
        Aeroplane("oli", "ne5", "USA", 1100.0, 80.0, 30.0),
        Aeroplane("via", "ba1", "Russia", 1350.0, 111.0, 30.0),
        Aeroplane("via", "ba1", "Nigeria", 1200.0, 110.0, 30.0),
        Aeroplane("via", "ba1", "Latvia", 1110.0, 300.0, 30.0)
    ]

    get_top_n(aeroplanes, 2)
    assert [
        Aeroplane("via", "ba1", "Russia", 1350.0, 111.0, 30.0),
        Aeroplane("via", "ba1", "Nigeria", 1200.0, 110.0, 30.0),
    ]


def test_get_by_altitude_range():
    aeroplanes = [
        Aeroplane("oli", "ne5", "USA", 1100.0, 80.0, 30.0),
        Aeroplane("via", "ba1", "Russia", 1350.0, 111.0, 30.0),
        Aeroplane("via", "ba1", "Nigeria", 1200.0, 110.0, 30.0),
        Aeroplane("via", "ba1", "Latvia", 1110.0, 300.0, 30.0)
    ]

    get_by_altitude_range(aeroplanes, 500.0, 1150.0)
    assert [
        Aeroplane("oli", "ne5", "USA", 1100.0, 80.0, 30.0),
        Aeroplane("via", "ba1", "Latvia", 1110.0, 300.0, 30.0)
    ]
