import numpy as np

# Функция сигмоида
# Необходима для определения значения весов

def nonlin(x, deriv=False):
    if (deriv == True):
        return (x) * (1 - (x))
    return 1 / (1 + np.exp(-x))

# Набор входных данных
X = np.array([[1, 0, 1],
              [1, 0, 1],
              [0, 1, 0],
              [0, 1, 0]])

# Выходные данные
y = np.array([[0, 0, 1, 1]]).T

# Сделаем случайные числа более определенными
np.random.seed(1)

# Инициализируем веса случайным образом со средним 0
syn0 = 2 * np.random.random((3, 1)) -1

l1 = []

for iter in range(10000):
    l0 = X
    l1 = nonlin(np.dot(l0, syn0))

    l1_error = y - l1

    l1_delta = l1_error * nonlin(l1, True)

    syn0 += np.dot(l0.T, l1_delta)

print("Выходные данные после тренировки: ")
print(l1)

new_one = np.array([1, 1, 1])
l1_new = nonlin(np.dot(new_one, syn0))
print("Новые данные: ")
print(l1_new)