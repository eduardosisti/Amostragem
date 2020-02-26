import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Jogo 1
simulacoes = 10000  # Número de simulações de Monte Carlo
Jogos = 100  # Número de jogos
limiar = 40  # limiar onde se maior ou igual você ganha
aposta = 1  # Aposta de cada jogo

sim_results_1 = []
for sim in range(simulacoes):
    result = []
    for g in range(Jogos):
        number = int(np.random.uniform() * 100)  # Número inteiro randômico de 1 a 100
        if number >= limiar:
            result.append(aposta)
        else:
            result.append(-aposta)
    sim_results_1.append(sum(result))
print('Média do jogo 1: ', round(np.mean(sim_results_1), 2))
print('Probabilidade de sair ganhando: ', round(sum([1 for i in sim_results_1 if i > 0]) / simulacoes, 2))
print('\n')

# Jogo 2
simulacoes = 10000
Jogos = 10
limiar = 40
aposta = 10

sim_results_2 = []
for sim in range(simulacoes):
    result = []
    for g in range(Jogos):
        number = int(np.random.uniform() * 100)
        if number >= limiar:
            result.append(aposta)
        else:
            result.append(-aposta)
    sim_results_2.append(sum(result))
print('Média do jogo 2: ', round(np.mean(sim_results_2), 2))
print('Probabilidade de sair ganhando: ', round(sum([1 for i in sim_results_2 if i > 0]) / simulacoes, 2))
print('\n')

# Jogo 3
simulacoes = 10000
Jogos = 1
limiar = 40
aposta = 100

sim_results_3 = []
for sim in range(simulacoes):
    result = []
    for g in range(Jogos):
        number = int(np.random.uniform() * 100)
        if number >= limiar:
            result.append(aposta)
        else:
            result.append(-aposta)
    sim_results_3.append(sum(result))
print('Média do jogo 3: ', round(np.mean(sim_results_3), 2))
print('Probabilidade de sair ganhando: ', round(sum([1 for i in sim_results_3 if i > 0]) / simulacoes, 2))

# Histograma que mostra a distribuição dos resultados de Monte Carlo
fig, ax = plt.subplots(figsize=(8, 6))
sns.distplot(sim_results_1, kde=False, bins=60, label='Jogar 100 vezes')
sns.distplot(sim_results_2, kde=False, bins=60, label='Jogar 10 vezes')
sns.distplot(sim_results_3, kde=False, bins=60, label='Jogar 1 vez', color='green')

ax.set_xlabel('Dinheiro ganho pelo jogador', fontsize=16)
ax.set_ylabel('Frequência', fontsize=16)
plt.legend()
plt.tight_layout()

plt.savefig(fname='jogo_hist', dpi=150)
plt.show()