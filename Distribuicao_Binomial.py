from scipy.stats import binom

# pmf( número de acertos, tentativas, probabilidade de cada evento)

# Jogar uma moeda 5 vezes, qual a probabilidade de dar cara 3 vezes?
prob = binom.pmf(3, 5, 0.5)

# Passar por 4 sinais de 4 tempos, qual a probabilidade de pegar sinal verde nenhuma, 1, 2, 3, 4 vezes seguidas?

prob2 = binom.pmf(0, 4, 0.25)
prob3 = binom.pmf(1, 4, 0.25)
prob4 = binom.pmf(2, 4, 0.25)
prob5 = binom.pmf(3, 4, 0.25)
prob6 = binom.pmf(4, 4, 0.25)

print(prob2, prob3, prob4, prob5, prob6, sep='\n')

# Probabilidade acumulativa

Pacumulada = binom.cdf(0, 4, 0.25)
print(Pacumulada)

# Concurso com 12 questões, qual a probabilidade de acertar 7 questões considerando que cada questão tem 4 alternativas?

prob7 = binom.pmf(9, 12, 0.25)
print(prob7)