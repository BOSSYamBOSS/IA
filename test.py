import numpy as np



### Nombres à la main

a = np.array([[0 for _ in range(5)] for j in range(5)]) # 1
a[:, 2] = 1
a[1, 1] = 1
a[1, 0] = 1
a[4, :] = 1

b = np.array([[0 for _ in range(5)] for j in range(5)]) # 2
b[:, 3] = 1
b[:, 1] = 1
b[(0, 2, 4), 2] = 1
b[1, 1] = 0
b[3, 3] = 0

c = np.array([[0 for _ in range(5)] for j in range(5)]) # 3
c[:, 3] = 1
c[0, 1:3] = 1
c[2, 1:3] = 1
c[4, 1:3] = 1

d = np.array([[0 for _ in range(5)] for j in range(5)]) # 4
d[:3, 1] = 1
d[2, 1:] = 1
d[1:, 3] = 1

e = np.array([[0 for _ in range(5)] for j in range(5)]) # 5
e[:, 3] = 1
e[:, 1] = 1
e[(0, 2, 4), 2] = 1
e[3, 1] = 0
e[1, 3] = 0

f = np.array([[0 for _ in range(5)] for j in range(5)]) # 6
f[:, 3] = 1
f[:, 1] = 1
f[(0, 2, 4), 2] = 1
f[1, 3] = 0

g = np.array([[0 for _ in range(5)] for j in range(5)]) # 7
g[0, 1:4] = 1
g[1, 3] = 1
g[2, 2] = 1
g[3, 1] = 1
g[4, 1] = 1

h = np.array([[0 for _ in range(5)] for j in range(5)]) # 8
h[:, 3] = 1
h[:, 1] = 1
h[(0, 2, 4), 2] = 1

i = np.array([[0 for _ in range(5)] for j in range(5)]) # 9
i[:, 3] = 1
i[:, 1] = 1
i[(0, 2, 4), 2] = 1
i[3, 1] = 0

j = np.array([[0 for _ in range(5)] for k in range(5)]) # 0
j[:, 3] = 1
j[:, 1] = 1
j[(0, 4), 2] = 1
"""
for n, nombre in enumerate([j, a, b, c, d, e, f, g, h, i]):
    #cv2.imwrite(f"{n}.png", nombre)
    print(nombre)
    print()
"""