import pandas as pd
from sklearn.model_selection import train_test_split

iris = pd.read_csv('iris.csv')

# print(iris['sepal length'].value_counts()) # conta a quantidade de valor de uma coluna

# print(iris)
x, _, y, _ = train_test_split(iris.iloc[:, 0:5], iris.iloc[:, 4], test_size=  0.5, stratify = iris.iloc[:, 4])

# test_size define a quantidade da amostra estratificada que ira retornar: nova_amostragem = amostragem - amostragem*teste_size
# print(x, y)

# Outro exemplo

infert = pd.read_csv('infert.csv')

x1, _, y1, _ = train_test_split(infert.iloc[:, 2:9], infert.iloc[:, 1], test_size=  0.59677, stratify = infert.iloc[:, 1])


print(x1)
print(y1.value_counts())