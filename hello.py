# Python 3.14 Core
#C:\Users\talan\AppData\Local\Python\pythoncore-3.14-64\python.exe

print("Hello, World!")

import numpy as np
import sys

def greet(name):
    return f"Hello, {name}!"

print(greet("Sarah"))

def random_array(size):
    return np.random.rand(size)

print(random_array(5))

print(np.std(random_array(10)))

print(np.mean(random_array(10)))
print(sys.executable)
