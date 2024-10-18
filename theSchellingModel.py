import random
import matplotlib.pyplot as plt
import numpy as np

# Размер поля
n = 100

# Доли цветов и пустых клеток
blue_ratio = 0.45
red_ratio = 0.45
empty_ratio = 0.10

# Создание поля
field = [[' ' for _ in range(n)] for _ in range(n)]

# Заполнение поля случайным образом
for i in range(n):
    for j in range(n):
        if random.random() < blue_ratio:
            field[i][j] = 'B'  # Синий
        elif random.random() < (blue_ratio + red_ratio):
            field[i][j] = 'R'  # Красный
        else:
            field[i][j] = ' '  # Пустой

# Функция для проверки счастья клетки
def is_happy(field, i, j, color):
    happy_count = 0
    for di in range(-1, 2):
        for dj in range(-1, 2):
            if (0 <= i + di < n) and (0 <= j + dj < n) and (di != 0 or dj != 0):
                if field[i + di][j + dj] == color:
                    happy_count += 1
    return happy_count >= 2

# Функция для вывода поля
def print_field(field):
    for row in field:
        print(' '.join(row))

# Моделирование
steps = 1000  # Количество шагов
print_interval = 100  # Интервал вывода

for step in range(steps):
    # Находим несчастную клетку
    unhappy_cells = []
    for i in range(n):
        for j in range(n):
            if field[i][j] != ' ' and not is_happy(field, i, j, field[i][j]):
                unhappy_cells.append((i, j))

    # Если есть несчастные клетки, перемещаем одну из них
    if unhappy_cells:
        i, j = random.choice(unhappy_cells)
        color = field[i][j]
        empty_cells = [(x, y) for x in range(n) for y in range(n) if field[x][y] == ' ']
        x, y = random.choice(empty_cells)
        field[i][j] = ' '
        field[x][y] = color

    # Печать поля через заданный интервал
    if (step + 1) % print_interval == 0:
        print(f"Шаг {step + 1}:")
        print_field(field)

        # Преобразовать поле в числовой массив с целочисленными значениями цветов
        field_array = np.array(field)
        field_array[field_array == 'B'] = 0
        field_array[field_array == 'R'] = 1
        field_array[field_array == ' '] = 2

        # Преобразовать тип данных в float
        field_array = field_array.astype(float)

        # Отобразить изображение
        plt.imshow(field_array, cmap='viridis')
        plt.title(f"Шаг {step + 1}")
        plt.show()