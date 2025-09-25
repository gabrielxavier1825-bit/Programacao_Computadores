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

# Desenvolva um programa em Python que solicite ao usuário os valores da base maior, base menor e altura de um trapézio e, em seguida, calcule e exiba a sua área.
# Utilize a fórmula da área do trapézio.

#Desenvolva um programa em Python que solicite ao usuário dois valores inteiros e em seguida calcule a média aritmética entre eles.

valorA = int(input('Informe o primeiro valor: '))
valorB = int(input('Informe o segundo valor: '))
media = (valorA + valorB) /2
print(f'A média entre {valorA} e {valorB} é {media}')
