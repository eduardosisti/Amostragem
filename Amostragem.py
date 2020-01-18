import pandas as pd
import numpy as np

base = pd.read_csv('iris.csv')
print(base.shape)

data1 = pd.DataFrame(base)
print(data1)