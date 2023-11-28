s = [0:0.5:10]; % vetor de notas de serviço
c = [0:0.5:10]; % notas da comida
[serv,com] = meshgrid(s,c); % junção dos dois vetores
g1 = ((0.02/20) * (serv + com)) + 0.05; %função gorjeta
surf(serv,com,g1), grid, title('gorjeta'), ylabel('teste')


// agora considerando pedos de serviço, 80% para o serviço e 20% para a comida

g2 = 0.8 * (((0.2/10)*serv) + 0.05) + 0.2 * (((0.2/10)*com) + 0.05);
surf(serv,com,g2), grid, title('gorjeta'), ylabel('teste')


%considerando agora que a gorjeta seja de 15% caso a nota do serviço seja
%entre 3 e 7 e evolua linearmente nos outros intervalos
gor3 = zeros(size(s));
gor3(s < 3) = (0.1/3)*s(s < 3) + 0.05;
gor3(s >= 3 & s <= 7) = 0.15;
gor3(s > 7 & s <= 10) = (0.1/3)*(s(s > 7 & s <= 10) - 7) + 0.15;

plot(s, gor3), grid, xlabel('serviço'), ylabel('gorjeta')

%Caso 4 com duas dimensões e peso de 80% para o serviço 
gor4(serv<3)=0.8*((0.1/3)serv(serv<3)+0.05)+0.2((0.2/10)*com(serv<3)+0.05);
gor4(serv>=3 & serv<7)=0.8*0.15+0.2*((0.2/10)*com(serv>=3 & serv<7)+0.05);
gor4(serv>=7 & serv<=10)=0.8*((0.1/3)(serv(serv>=7 & serv<=10)-7)+0.15)+0.2((0.2/10)*com(serv>=7 & serv<=10)+0.05);

surf(serv,com,gor4),grid,title('Gorjeta')


