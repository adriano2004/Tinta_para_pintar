l=float(input('Qual a largula da parede? '))
a=float(input('Qual a altura da parede? '))
m = l*a #Metros quadrados que a parede tem
q = 2.0 #Quantos metros quadrados 1L de tinta pinta

print (' A parede tem {}m de largura, {}m de altura e {}m² \n Você vai precisar de {}L de tinta'.format(l,a,m,m/q))