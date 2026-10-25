from pathlib import Path
import csv
import matplotlib.pyplot as plt

# Создаем объект Path после импорта его из библиотеки и прописываем путь к файлу 
# читаем файл сначала как большую строку, которую затем разрезаем по символам переноса
path = Path('IMOEX_261020_261020.csv')
lines = path.read_text().splitlines()

# Далее создается объект reader. Он используется для парсинга всех строк в файле. 
# Чтобы создать объект reader, мы вызываем функцию csv.reader() 
# и передаем ей список строк из файла CSV.
reader = csv.reader(lines, delimiter=';')
header_row = next(reader)

# print(header_row)

# Чтобы было проще понять структуру данных в файле, выведем каждый заголовок и его позицию в спискe
# Функция enumerate() возвращает индекс каждого элемента и его значение при переборе списка. 
# (Обратите внимание: строка print(header_row) удалена ради этой более подробной версии.

# for index, column_header in enumerate(header_row):
#   print(index, column_header)

prices = []

for row in reader:
    # 1. Защита от пустых строк в конце файла
    if len(row) > 4:
        try:
            # 2. Используем float вместо int, так как цены имеют дробную часть!
            price = float(row[4]) 
            prices.append(price)
        except ValueError:
            # Если в строке вместо цены попадется текст (например, итоговая строка), 
            # мы просто ее пропустим, а не уроним программу
            continue

# Выведем первые 5 цен, чтобы не засорять терминал (их может быть тысячи)
# print("Первые 5 цен:")
# print(prices[:5])

# А теперь проверим, что данные собрались
# print(f"\nВсего извлечено цен: {len(prices)}")

# Берем первые 500 цен для наглядности, иначе график будет слишком плотным
# (на 60 000 точках линия просто сольется в пятно)
plot_data = prices[:500]

# Настраиваем размер окна графика
plt.figure(figsize=(10, 5))

# Строим график
plt.plot(plot_data, color='blue', linewidth=1)

# Добавляем заголовок и подписи осей
plt.title('Динамика цен IMOEX (первые 500 записей)', fontsize=14)
plt.xlabel('Номер записи (время)', fontsize=12)
plt.ylabel('Цена (руб.)', fontsize=12)

# Добавляем сетку для удобства
plt.grid(True, linestyle='--', alpha=0.6)

# Создаем простую скользящую среднюю за 50 периодов (SMA-50)
# Логика: берем текущую цену, плюс 49 предыдущих, и делим на 50.
window_size = 50
sma_values = []

for i in range(len(plot_data)):
    if i < window_size:
        sma_values.append(None) # Пока данных мало, среднюю не считаем
    else:
        # Берем срез из 50 последних цен и считаем среднее
        avg = sum(plot_data[i - window_size:i]) / window_size
        sma_values.append(avg)

# Строим оба графика
plt.figure(figsize=(10, 5))
plt.plot(plot_data, color='blue', linewidth=1, label='Цена (Last)')
plt.plot(sma_values, color='red', linewidth=2, label=f'SMA-{window_size}')

plt.title('IMOEX с наложением скользящей средней', fontsize=14)
plt.xlabel('Номер записи', fontsize=12)
plt.ylabel('Цена', fontsize=12)
plt.grid(True, linestyle='--', alpha=0.6)
plt.legend() # Добавляем легенду, чтобы понимать, где какая линия
plt.show()