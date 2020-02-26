import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.DataFrame(
        {'stratifying_var': np.random.uniform(0, 100, 20),
         'price': np.random.normal(100, 5, 20)})


df['quartiles'] = pd.qcut(
        df['stratifying_var'],
        4,
        labels=['0-25%', '25-50%', '50-75%', '75-100%'])


print(df.boxplot(column='price', by='quartiles'))
d = 1
def funcas(*args,**kwargs):
    las = list(args)
    d = las[0] + 2
    print(d)
    return d

d2 = funcas(d)
x = d2 + 2
print(x)

plt.show()
