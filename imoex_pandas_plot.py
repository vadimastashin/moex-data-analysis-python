import pandas as pd
import matplotlib.pyplot as plt

# 1. Читаем файл. Указываем точку с запятой как разделитель!
file_path = 'IMOEX_261020_261020.csv'
df = pd.read_csv(file_path, sep=';')

# 2. Убираем угловые скобки из названий колонок (чтобы было красивее)
# <TICKER> станет TICKER, <LAST> станет LAST и т.д.
df.columns = [col.strip('<>') for col in df.columns]

# 3. Берем только первые 500 строк для графика
df_subset = df.head(500).copy()

# 4. Считаем скользящую среднюю (SMA-50) В ОДНУ СТРОКУ
df_subset['SMA_50'] = df_subset['LAST'].rolling(window=50).mean()

# 5. Строим график средствами Pandas
plt.figure(figsize=(10, 5))
plt.plot(df_subset['LAST'], color='blue', linewidth=1, label='Цена (Last)')
plt.plot(df_subset['SMA_50'], color='red', linewidth=2, label='SMA-50 (Pandas)')

plt.title('IMOEX: Сравнение подхода на Pandas', fontsize=14)
plt.xlabel('Номер записи', fontsize=12)
plt.ylabel('Цена', fontsize=12)
plt.grid(True, linestyle='--', alpha=0.6)
plt.legend()
plt.show()

# Бонус: выведем первые 5 строк таблицы, чтобы увидеть структуру DataFrame
print("Первые 5 строк данных:")
print(df[['DATE', 'TIME', 'LAST']].head())