import requests

response = requests.get('https://jsonplaceholder.typicode.com/posts')
data = response.json()

# Выводим данные в консоль
for post in data[:5]: 
    print(f"Title: {post['title']}")


import pandas as pd

df = pd.read_csv('data.csv')

print(df.head())

mean_value = df['value'].mean()
print(f"Среднее значение: {mean_value}")

filtered_data = df[df['value'] > mean_value]
print(filtered_data)

import numpy as np


array = np.array([1, 2, 3, 4, 5])


squared = array ** 2  
mean_value = np.mean(array)  

# Вывод результатов
print(f"Исходный массив: {array}")
print(f"Квадраты: {squared}")
print(f"Среднее значение: {mean_value}")
