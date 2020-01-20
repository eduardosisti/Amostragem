import pandas as pd
import numpy as np

base = pd.read_csv('iris.csv')
# print(base.shape)

data1 = pd.DataFrame(base)
# print(data1)

# Código que gera 150 dados com valores entre 0 e 1 com probabilidade de 50% para cada um

# np.random.seed(123) # Seed, esta parte faz com que os resultados da amostra sempre sejam os mesmos
amostra = np.random.choice(a=[0, 1], size=150, replace=True, p=[0.5,0.5])

print(len(amostra))
n0 = len(amostra[amostra == 0])
n1 = len(amostra[amostra == 1])
print(f'A quantidade de números 1 = {n0} e a quantidade de números 0 = {n1}')

# exemplo = jogando um dado justo 6 vezes, qual a média esperada

dados = np.random.choice(a=[1, 2, 3, 4, 5, 6], size=100000, replace=True)

somadados = 0
for soma in dados:
    somadados += soma

print(sum(dados)) # soma os dados da lista (mesma cosia que o de cima)
print(somadados/100000)
print(np.std(dados,ddof=1))
