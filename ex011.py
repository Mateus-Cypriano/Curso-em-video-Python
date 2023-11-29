alt = float(input('Qual a altura da parede? '))
larg = float(input('Qual a largura da parede? '))
area = alt * larg
print('A dimensão da sua parede é de {}X{}. E a área da sua parede é de {}m²'.format(alt, larg, area))
print('Como sua parede tem {}m² de área, você precisará de {}l de tinta para pinta-la'.format(area, (area / 2)))
