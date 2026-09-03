
print("Hello, World!")

import numpy as np

def greet(name):
    return f"Hello, {name}!"

print(greet("Sarah"))

def random_array(size):
    return np.random.rand(size)

print(random_array(5))

print(np.std(random_array(10)))

print(np.mean(random_array(10)))
