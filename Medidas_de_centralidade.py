import numpy as np
from scipy import stats
import math as mt

dados = [40000, 18000, 12000, 250000, 30000, 140000, 300000, 40000, 800000]
media = np.mean(dados)
mediana = np.median(dados)
quartis = np.quantile(dados, [0, 0.25, 0.75, 1])
desvio_padrao = np.std(dados, ddof=1) #ddof = 1 é usado pois estamos usando a população e não uma amostra
describe = stats.describe(dados)

print(describe)
print(mt.sqrt(describe[3]))
print(desvio_padrao)





