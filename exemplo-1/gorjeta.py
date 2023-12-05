#O objeteivo do programa é gerar uma figura que analize a porcentagem de gorjeta que um garçom recebe
#tendo como parametros de avaliação a nota da comida e a nota do atendimento

# bibliotecas importadas
import numpy as np
import matplotlib.pyplot as plt 

s = np.arange(0, 10.5, 0.5) # vetor de notas de serviço
c = np.arange(0, 10.5, 0.5) # notas da comida serv,
serv,com = np.meshgrid(s, c) # junção dos dois vetores

g1 = ((0.02/20) * (serv + com)) + 0.05 # função gorgeta

fig = plt.figure() # Criação da figura
ax = fig.add_subplot(111, projection='3d') # subplot para gerar uma projeção 3d 
ax.plot_surface(serv, com, g1)  # informações para os eixos x,y,z
ax.set_title('gorgeta') # titulo da figura
ax.set_xlabel('serv') # titulo do eixo x
ax.set_ylabel('com') # titulo do eixo Y

plt.show() # mostra a figura

# Função gorjeta g2 com pesos para serviço e comida
g2 = 0.8 * (((0.2 / 10) * serv) + 0.05) + 0.2 * (((0.2 / 10) * com) + 0.05)

# Plot da superfície
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(serv, com, g2)
ax.set_title('Gorjeta')
ax.set_ylabel('teste')
ax.grid(True)
plt.show()

# Gorjeta gor3 com condições
gor3 = np.zeros_like(s)
gor3[s < 3] = (0.1 / 3) * s[s < 3] + 0.05
gor3[(s >= 3) & (s <= 7)] = 0.15
gor3[(s > 7) & (s <= 10)] = (0.1 / 3) * (s[(s > 7) & (s <= 10)] - 7) + 0.15

# Plot do gráfico
plt.plot(s, gor3)
plt.title('Gorjeta')
plt.xlabel('serviço')
plt.ylabel('gorjeta')
plt.grid(True)
plt.show()

# Gorjeta gor4 com condições, duas dimenções e peso de 80% para o serviço
gor4 = np.zeros_like(serv)

gor4[serv < 3] = 0.8 * (((0.1 / 3) * serv[serv < 3]) + 0.05) + 0.2 * (((0.2 / 10) * com[serv < 3]) + 0.05)
gor4[(serv >= 3) & (serv < 7)] = 0.8 * 0.15 + 0.2 * (((0.2 / 10) * com[(serv >= 3) & (serv < 7)]) + 0.05)
gor4[(serv >= 7) & (serv <= 10)] = 0.8 * ((0.1 / 3) * (serv[(serv >= 7) & (serv <= 10)] - 7) + 0.15) + \
                                   0.2 * (((0.2 / 10) * com[(serv >= 7) & (serv <= 10)]) + 0.05)

# Plot da superfície
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(serv, com, gor4)
ax.set_title('Gorjeta')
ax.grid(True)
plt.show()

# Pertinência das notas para as categorias "ruim", "bom" e "excelente"
sruim = np.zeros_like(s)
sruim[s <= 2.5] = 1
sruim[(s > 2.5) & (s <= 5)] = (-1/2.5) * s[(s > 2.5) & (s <= 5)] + 2
sruim[s > 5] = 0

sbom = np.zeros_like(s)
sbom[s < 2.5] = 0
sbom[(s >= 2.5) & (s <= 5)] = (1/2.5) * s[(s >= 2.5) & (s <= 5)] - 1
sbom[(s > 5) & (s <= 7)] = 1
sbom[(s > 7) & (s <= 10)] = (-1/2.5) * s[(s > 7) & (s <= 10)] + 4

sexcelente = np.zeros_like(s)
sexcelente[s <= 7] = 0
sexcelente[(s > 7) & (s <= 10)] = (1/2.5) * s[(s > 7) & (s <= 10)] - 3

# Plot das pertinências
plt.figure()
plt.plot(s, sruim, label='Ruim')
plt.plot(s, sbom, label='Bom')
plt.plot(s, sexcelente, label='Excelente')
plt.grid(True)
plt.xlabel('serviço')
plt.ylabel('gorjeta')
plt.legend()
plt.show()

# Funções de pertinência para as categorias "baixa", "média" e "generosa"
gbaixa = np.zeros_like(s)
gbaixa[s <= 2.5] = (-1/2.5) * s[s <= 2.5] + 1
gbaixa[s > 2.5] = 0

gmedia = np.zeros_like(s)
gmedia[s <= 2.5] = 0
gmedia[(s > 2.5) & (s <= 5)] = (1/2.5) * s[(s > 2.5) & (s <= 5)] - 1
gmedia[(s > 5) & (s <= 7)] = (-1/2.5) * s[(s > 5) & (s <= 7)] + 3
gmedia[s > 7] = 0

generosa = np.zeros_like(s)
generosa[s <= 5] = 0
generosa[(s > 5) & (s < 7.5)] = (1/2.5) * s[(s > 5) & (s < 7.5)] - 2
generosa[s >= 7.5] = 1

# Plot das funções de pertinência
plt.figure()
plt.plot(s, gbaixa, label='Baixa')
plt.plot(s, gmedia, label='Média')
plt.plot(s, generosa, label='Generosa')
plt.grid(True)
plt.xlabel('serviço')
plt.ylabel('gorjeta')
plt.legend()
plt.show()

# Pertinência para uma nota específica
n = input('Digite o valor da nota: ')

uruim = np.zeros_like(n)
uruim[n < 2.5] = 1
uruim[(n >= 2.5) & (n < 5)] = (-1/2.5) * n[(n >= 2.5) & (n < 5)] + 2
uruim[n >= 5] = 0
print(f'Pertinência em "Ruim": {uruim}')

ubom = np.zeros_like(n)
ubom[n < 2.5] = 0
ubom[(n >= 2.5) & (n <= 5)] = (1/2.5) * n[(n >= 2.5) & (n <= 5)] - 1
ubom[(n > 5) & (n <= 7)] = 1
ubom[(n > 7) & (n <= 10)] = (-1/2.5) * n[(n > 7) & (n <= 10)] + 4
print(f'Pertinência em "Bom": {ubom}')

uexcelente = np.zeros_like(n)
uexcelente[n <= 7] = 0
uexcelente[(n > 7) & (n <= 10)] = (1/2.5) * n[(n > 7) & (n <= 10)] - 3
print(f'Pertinência em "Excelente": {uexcelente}')