import numpy as np
import matplotlib.pyplot as plt
import random

# Параметры модели
n = 10  # Размер сетки

# Инициализация сетки
grid = np.zeros((n, n), dtype=int)

# Заполнение сетки
num_blue = int(0.45 * n * n)
num_red = int(0.45 * n * n)
num_empty = n * n - num_blue - num_red

# Случайное распределение клеток
cells = [0] * num_empty + [1] * num_blue + [2] * num_red
random.shuffle(cells)
grid = np.array(cells).reshape((n, n))

def is_happy(grid, x, y):
    color = grid[x, y]
    if color == 0:
        return True  # Пустые клетки всегда счастливы
    neighbors = [(x-1, y-1), (x-1, y), (x-1, y+1),
                 (x, y-1),             (x, y+1),
                 (x+1, y-1), (x+1, y), (x+1, y+1)]
    same_color_count = 0
    for nx, ny in neighbors:
        if 0 <= nx < n and 0 <= ny < n and grid[nx, ny] == color:
            same_color_count += 1
    return same_color_count >= 2

def find_unhappy(grid):
    unhappy_cells = []
    for x in range(n):
        for y in range(n):
            if not is_happy(grid, x, y):
                unhappy_cells.append((x, y))
    return unhappy_cells

def find_empty(grid):
    empty_cells = []
    for x in range(n):
        for y in range(n):
            if grid[x, y] == 0:
                empty_cells.append((x, y))
    return empty_cells

def plot_grids(initial_grid, final_grid, steps):
    fig, axs = plt.subplots(1, 2, figsize=(12, 6))
    cmap = plt.cm.colors.ListedColormap(['white', 'blue', 'red'])
    bounds = [0, 1, 2, 3]
    norm = plt.cm.colors.BoundaryNorm(bounds, cmap.N)

    axs[0].imshow(initial_grid, cmap=cmap, norm=norm)
    axs[0].set_title('Initial State')
    axs[1].imshow(final_grid, cmap=cmap, norm=norm)
    axs[1].set_title(f'Final State (Step {steps})')
    plt.show()

# Сохранение начального состояния сетки
initial_grid = np.copy(grid)

# Моделирование
step = 0
while True:
    unhappy_cells = find_unhappy(grid)
    empty_cells = find_empty(grid)

    if not empty_cells:
        break

    if not unhappy_cells:
        break

    unhappy_cell = random.choice(unhappy_cells)
    empty_cell = random.choice(empty_cells)

    grid[empty_cell], grid[unhappy_cell] = grid[unhappy_cell], grid[empty_cell]
    step += 1

# Заполнение оставшихся пустых клеток случайными цветами
empty_cells = find_empty(grid)
for x, y in empty_cells:
    grid[x, y] = random.choice([1, 2])

# Отображение начального и конечного состояния сетки
plot_grids(initial_grid, grid, step)
