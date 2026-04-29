from src.api import AeroplanesAPI
from src.aeroplane import Aeroplane
from src.file import JSONSaver
from src.utils import filter_by_country, get_top_n


def user_interaction():
    """Функция взаимодействия с пользователем через консоль."""
    print("\n" + "=" * 50)
    print("Добро пожаловать в программу отслеживания самолётов")
    print("=" * 50 + "\n")

    country = input("Введите название страны (на английском): ")

    print(f"\nПолучение данных о самолётах над {country}...")
    api = AeroplanesAPI()

    try:
        aeroplanes_data = api.get_aeroplanes(country)
    except Exception as e:
        print(f"Ошибка при получении данных: {e}")
        return

    if not aeroplanes_data:
        print("Самолётов не найдено")
        return

    aeroplanes = Aeroplane.cast_to_object_list(aeroplanes_data)
    print(f"Найдено самолётов: {len(aeroplanes)}")

    saver = JSONSaver()
    for plane in aeroplanes:
        saver.add_aeroplane({
            "icao24": plane.icao24,
            "callsign": plane.callsign,
            "origin_country": plane.origin_country,
            "altitude": plane.altitude,
            "velocity": plane.velocity,
            "heading": plane.heading
        })
    print(f"Данные сохранены в файл: {saver._filename}")
    print()

    n = input("Введите количество самолётов для вывода в топ N (по высоте): ")
    try:
        n = int(n)
    except ValueError:
        print("Введено не число. Будет выведено 5 самолётов")
        n = 5
    print()

    top_planes = get_top_n(aeroplanes, n)
    print(f"Топ {len(top_planes)} самолётов по высоте:")
    for i, plane in enumerate(top_planes, 1):
        print(f"{i}. {plane.callsign} ({plane.origin_country}) - высота: {plane.altitude} м, скорость: {plane.velocity} м/с")
    print()

    filter_country = input("Введите страну для фильтрации самолётов (или Enter чтобы пропустить): ")
    if filter_country:
        filtered = filter_by_country(aeroplanes, filter_country)
        print(f"\nСамолёты из страны {filter_country}:")
        if filtered:
            for plane in filtered:
                print(f"  {plane.callsign} - высота: {plane.altitude} м")
        else:
            print("  Самолётов не найдено")
    print()
    print("Программа завершена. До свидания!")


if __name__ == "__main__":
    user_interaction()
