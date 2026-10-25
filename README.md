Название проекта: Анализ биржевых данных IMOEX на Python.

Цель: Сравнение базового модуля csv и библиотеки Pandas для расчета индикатора SMA-50.

Что внутри: impex.py — ручной парсинг и вывод графика, imoex_pandas.py - с помощью Pandas и imoex_pandas_plot.py — вывод графика.

Результат: 

![График IMOEX и SMA-50](Figure_1.png)
![График IMOEX и SMA-50](Figure_2.png)
![График IMOEX и SMA-50](Figure_3.png)

### Требования
Для работы скриптов необходим Python версии 3.8 или выше.
Используемые библиотеки: `pandas`, `matplotlib`.

### Установка и запуск

1. Клонируйте репозиторий:
   git clone https://github.com/vadimastashin/moex-data-analysis-python.git

2. Создайте у себя виртуальное окружение:
    python -m venv .venv
    .\.venv\Scripts\activate  # Для Windows
3. Установите зависимости:
  pip install -r requirements.txt
4. Запустите скрипт:
  python impoex_pandas.py python или imoex_pandas_plot.py

### Структура проекта
* `imoex.py` — скрипт с использованием встроенного модуля `csv` (ручной парсинг).
* `imoex_pandas.py` — скрипт с использованием библиотеки `pandas` для загрузки и анализа.
* `imoex_pandas_plot.py` — скрипт для визуализации данных.
* `IMOEX_261020_261020.csv` — исходные данные (выгрузка из Finam).
