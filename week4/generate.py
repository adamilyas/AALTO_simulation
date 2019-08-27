import numpy as np

def generate_uniform_point_r(radius=1):
    # in radians
    r_uniform = radius*np.sqrt(np.random.rand())
    U = np.random.rand()
    rad = 2 * np.pi * U
    x, y = np.cos(rad), np.sin(rad)
    return r_uniform*x, r_uniform*y

def generate_except():
    x, y = generate_uniform_point_r(100)
    if (x-70)**2 + y**2 <= 20**2:
        x, y = generate_except()
        return x, y
    return x, y

def transmission_rate(x, y, r_min = 10, alpha = 3, c_max = 100):
    r = np.sqrt(x**2 + y**2)
    if r <= r_min:
        return c_max
    return c_max * (r_min/ r)**alpha

ls = [generate_except() for _ in range(100000000)]
EXPECTED = np.mean([transmission_rate(x, y) for x, y in ls])
print(EXPECTED)
