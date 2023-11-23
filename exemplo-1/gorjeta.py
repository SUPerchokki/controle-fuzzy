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
