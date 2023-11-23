s = [0:0.5:10]; % vetor de notas de serviço
c = [0:0.5:10]; % notas da comida
[serv,com] = meshgrid(s,c); % junção dos dois vetores
g1 = ((0.02/20) * (serv + com)) + 0.05; %função gorgeta
surf(serv,com,g1), grid, title('gorgeta'), ylabel('teste')

