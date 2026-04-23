# Airplanes Tracking Project

Проект для отслеживания самолётов в воздушном пространстве выбранной страны. Получает данные через OpenSky API, сохраняет информацию в JSON-файл, позволяет фильтровать и сортировать самолёты по высоте и скорости.

## Содержание
- [Технологии](#технологии)
- [Начало работы](#начало-работы)
- [Структура проекта](#структура-проекта)
- [Тестирование](#тестирование)
- [Contributing](#contributing)
- [Команда проекта](#команда-проекта)

## Технологии
- Python 3.12+
- Requests
- Pytest
- Flake8
- Black
- Isort
- Mypy

## Начало работы

### Требования
Для установки и запуска проекта необходим Python версии 3.12 или выше.

### Установка зависимостей

#### Клонируйте репозиторий:

git clone https://github.com/kargashd/airplanes.git
cd airplanes

#### Создайте и активируйте виртуальное окружение:

python -m venv .venv
.venv\Scripts\activate

macOS/Linux
python3 -m venv .venv
source .venv/bin/activate


#### Установите зависимости:

pip install -r requirements.txt

### Использование

Запустите проект:python main.py

Программа запросит:

- Название страны на английском

- Количество самолётов для топа N по высоте

- Страну для фильтрации (опционально)

### Структура проекта

```bash
airplanes/
├── src/
│   ├── abstract_api.py          # Абстрактный класс для API
│   ├── api.py                   # Класс AeroplanesAPI
│   ├── abstract_file.py         # Абстрактный класс для файлов
│   ├── file.py                  # Класс JSONSaver
│   ├── aeroplane.py             # Класс Aeroplane
│   ├── utils.py                 # Вспомогательные функции
│   └── main.py                  # Точка входа
├── tests/
│   ├── test_api.py              # Тесты для API
│   ├── test_aeroplane.py        # Тесты для класса Aeroplane
│   ├── test_file.py             # Тесты для JSONSaver
│   └── test_utils.py            # Тесты для утилит
├── .env.example                 # Шаблон переменных окружения
├── .flake8                      # Конфигурация линтера
├── .gitignore                   # Игнорируемые Git файлы
├── pyproject.toml               # Конфигурация black, isort, mypy, pytest
├── requirements.txt             # Зависимости проекта
└── README.md                    # Документация проекта
```

## Тестирование
Для тестирования всех модулей используется Pytest.
Чтобы протестрировать проект введите команду "pytest" или "pytest --cov=src" в терминале


## Contributing
Сообщайте об ошибках и предлагайте идеи через раздел Issues на GitHub.

Для отправки доработок создайте pull request из ветки feature в develop.

Код должен соответствовать PEP 8 и проходить проверки flake8, black, isort, mypy.

### Зачем вы разработали этот проект?
Проект разработан в рамках прохождения курса "Python-разработчик" от Skypro.

## Команда проекта
Daniil Kargashin — разработчик

Email: danilo98.24fevral@yandex.ru

Ссылка на проект: https://github.com/kargashd/bank_utils
