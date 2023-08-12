import numpy as np

np.random.seed(20)

my_list = [i for i in np.random.randint(1, 10, size=10)]
print(my_list)
my_stroke = ' '.join([str(i) for i in my_list])
for i in range(len(my_list)):
    if min(my_list)
