#Faça um programa que leia a largura e a altura de uma parede em metros, 
#calcule a sua área e a quantidade de tinta necessária para pintá-la, 
#sabendo que cada litro de tinta pinta uma área de 2 metros quadrados

largura = float(input('Largura da parede:'))
altura  = float(input('Altura da parede: '))
área = largura * altura

print('Sua parede tem a dimensão de {} x {} e sua área é de {}m²'.format(largura, altura, área))

tinta = área / 2
print('Para pintar essa parede, você precisará de {}l de tinta'.format(tinta))

