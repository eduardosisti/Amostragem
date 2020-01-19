import numpy as np
import pandas as pd
from math import ceil

populacao = 150
amostra = 15

#ceil = arredonda a divisão para cima

k = ceil(populacao/amostra)


# cria um número aleatório que começa no low e termina no high(+1 pois o limite superior não conta) com tamanho size
r = np.random.randint( low = 1, high = k + 1, size = 1)

acumulador = r[0]
sorteados = []

for i in range(amostra):
    sorteados.append(acumulador)
    acumulador += k

iris = pd.read_csv("iris.csv")
Amostragem_sistemica = iris.loc[sorteados]
print(Amostragem_sistemica)