import numpy as np

if __name__ == '__main__':
    a = np.zeros(shape=(7, 7, 9, 5), dtype=np.float32)
    print(a)
    print("---------")
    a[3, 3, 8, 0] = 1
    a[3, 3, 8, 1] = 0.9
    a[3, 3, 8, 2] = 0.7
    a[3, 3, 8, 3] = 0.66333
    a[3, 3, 8, 4] = 0.1214
    print(a)
