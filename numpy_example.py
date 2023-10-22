import numpy as np

m = np.array([[1, 2], [3, 4]])
print(2 * m)
print(m.shape)
print(m.size)

# wyznacznik macierzy
print(np.linalg.det(m))

# wektory własne
print(np.linalg.eigvals(m))

# macierz odwrotna A^-1 czyli A*/det(A), gdzie A* =
inv_m = np.linalg.inv(m)
print(inv_m)

# mnożenie macierzowe
print(np.matmul(m, inv_m))

#rozwiązywanie układu równań liniowych Ax = b
b = np.array([1, -1])
x = np.matmul(b, np.linalg.inv(m))
print(x)
