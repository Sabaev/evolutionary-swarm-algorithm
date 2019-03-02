import random
import numpy as np

# Таблица
Table = np.array((
    (902000, 115800),
    (462000, 96000),
    (465000, 790000),
    (545000, 908000),
    (311000, 396000),
    (675000, 984000),
    (128000, 189000),
    (105000, 103000),
    (215000, 285000),
    (31000, 70000),
    (42000, 90000),
    (78000, 73000),
))


# Фитнес функция:
# Манхэттен – метрика городских кварталов
def MD(x, T=Table):
    s = 0.0
    for el in T:
        s += abs(x[0]*el[0]**x[1]-el[1])
    return s


# Генератор рандомных значений
def generate(N, lb=0.0, rb=10.0):
    r = []
    for i in range(N):
        r.append((random.uniform(lb, rb), random.uniform(lb, rb)))

    return r


# Роевой алгоритм
def ra(N, T):
    Y = np.array(generate(N))
    # X = Y.copy()
    X = Y
    ymax = Y[0]
    v = [0] * N

    for i in range(T):
        for j in range(N):
            if MD(X[j]) > MD(Y[j]):
                Y[j] = X[j]

            if MD(Y[j]) < MD(ymax):
                ymax = Y[j]

        for j in range(N):
            v[j] = v[j] + 1 * random.uniform(0.0, 1.0) * (Y[j] - X[j]) + 2 * random.uniform(0.0, 1.0) * (ymax - X[j])
            X[j] = X[j] + v[j]

    return ymax


print(ra(10, 20))
print(MD(ra(10, 20)))
