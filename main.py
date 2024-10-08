import pandas as pd

# Создание DataFrame с данными об учениках и их оценках от 1 до 5
data = {
    'Ученик': ['Ученик Петров', 'Ученик Сидоров', 'Ученик Кабанов', 'Ученик Шмелёв', 'Ученик Таймуразов',
               'Ученик Дебилёв', 'Ученик Козлинов', 'Ученик Парасюк', 'Ученик Кудиахметов', 'Ученик Горбунов'],
    'Математика': [4, 3, 3, 4, 3, 5, 4, 3, 5, 3],
    'Физика': [3, 4, 5, 5, 3, 3, 4, 4, 3, 5],
    'Химия': [5, 4, 3, 4, 4, 3, 4, 5, 3, 4],
    'Биология': [3, 3, 3, 4, 4, 4, 4, 4, 5, 3],
    'История': [4, 4, 5, 3, 3, 4, 5, 3, 4, 4]
}

df = pd.DataFrame(data)
print('----------------------------------------------------------------------')
# Вывод первых строк DataFrame
print("Оценки учеников:")
print(df.head())
print('----------------------------------------------------------------------')

# Вычисление средней оценки по каждому предмету
mean_scores = df.mean(numeric_only=True)
print("\nСредняя оценка по каждому предмету:")
print(mean_scores)
print('-----------------------------------------')

# Вычисление медианной оценки по каждому предмету
median_scores = df.median(numeric_only=True)
print("\nМедианная оценка по каждому предмету:")
print(median_scores)
print('-----------------------------------------')

# Вычисление Q1 и Q3 для оценок по математике и IQR
Q1_math = df['Математика'].quantile(0.25)
Q3_math = df['Математика'].quantile(0.75)
IQR_math = Q3_math - Q1_math
print("\nQ1 и Q3 для оценок по математике и IQR:")
print(f"Q1: {Q1_math},\nQ3: {Q3_math},\nIQR: {IQR_math}")
print('-----------------------------------------')

# Вычисление стандартного отклонения по каждому предмету
std_dev = df.std(numeric_only=True)
print("\nСтандартное отклонение по каждому предмету:")
print(std_dev)
print('-----------------------------------------')