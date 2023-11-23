# bibliotecas importadas
import numpy as np
import matplotlib.pyplot as plt 

s = np.arange(0, 10.5, 0.5) # vetor de notas de serviço
c = np.arange(0, 10.5, 0.5) # notas da comida serv,
serv,com = np.meshgrid(s, c) # junção dos dois vetores

g1 = ((0.02/20) * (serv + com)) + 0.05 # função gorgeta

fig = plt.figure() 
ax = fig.add_subplot(111, projection='3d') 
ax.plot_surface(serv, com, g1) 
ax.set_title('gorgeta') 
ax.set_xlabel('serv') 
ax.set_ylabel('com')

plt.show()
