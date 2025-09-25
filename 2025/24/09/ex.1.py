# Atividade

#Desenvolva um programa em Python que solicite ao usuário o valor do raio de um círculo e, em seguida, calcule e exiba a área do círculo.
#Utilize a fórmula da área do círculo. Considere o valor de pi = 3.1416

raio = float(input('Informe o raio: '))
area = 3.1416 * raio ** 2
print(f'A área do círculo de raio = {raio} é {area}')
n1 = int(input('Base maior:'))
n2 = int(input('Base menor:'))
n3 = int(input('Altura:'))
s = n1+n2
h = s*n3/2
print(f'O resultado é:{h}')
print(f'A área do círculo de raio = {raio} é {area:.2f}')
