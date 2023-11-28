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