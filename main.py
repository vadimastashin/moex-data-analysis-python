from pathlib import Path
import csv

# Создаем объект Path после импорта его из библиотеки и прописываем путь к файлу 
# читаем файл сначала как большую строку, которую затем разрезаем по символам переноса
path = Path('sitka_weather_07-2021_simple.csv')
lines = path.read_text().splitlines()

# Далее создается объект reader. Он используется для парсинга всех строк в файле. 
# Чтобы создать объект reader, мы вызываем функцию csv.reader() 
# и передаем ей список строк из файла CSV.
reader = csv.reader(lines)
header_row = next(reader)
print(header_row)