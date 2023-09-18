# import random
# lst = ['robot'] * 10
# lst += ['human'] * 10
# random.shuffle(lst)
# data = pd.DataFrame({'whoAmI'lst})
# data.head() |

import pandas as pd

data = pd.DataFrame(random.sample(['black', 'white']*10, 20) ,columns={'Colors'})
print(data