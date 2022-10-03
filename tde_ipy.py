# -*- coding: utf-8 -*-
"""TDE.ipy

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1w3IKNYtBE6EFUxF_bZsUwlHzhuV1YUtm

1 - Faça um programa para leitura de
três notas parciais de um aluno. O programa deve calcular a média alcançada por
aluno e apresentar:
a) A mensagem
"Aprovado", se a média for maior ou igual a 7, com a respectiva média
alcançada;
b) A mensagem
"Reprovado", se a média for menor do que 7, com a respectiva média
alcançada;
c) A mensagem "Aprovado com
Distinção", se a média for igual a 10.
"""

nota1 = float(input("Digite a 1º nota: "));
nota2 = float(input("Digite a 2° nota: "));
nota3 = float(input("Digite a 3° nota: "));


media = (nota1  + nota2 + nota3)/3;

if 10 > media >= 7: 
    print("Você foi aprovado, sua média foi: {:.1f}".format(media))

elif media < 7: 
    print("Você foi reprovado, sua média foi: {:.1f}".format(media))

if media == 10:
    print("Você foi aprovado com distinção, sua média foi: {:.1f}".format(media))

"""2- Faça um programa que peça uma
nota, entre zero e dez. Mostre uma mensagem caso o valor seja inválido e
continue pedindo até que o usuário informe um valor válido.
"""

from random import randint

numero = randint(0,10)

print("Pensei em um número entre 0 e 10, tente adivinhar")

acertou = False

while not acertou:
    tentativa = int(input("Digite um número: "))
    if tentativa == numero:
        acertou = True
    else:
        print("Voê erreu tente novamente")
print("Parabéns, você acertou!!!")

"""3- Faça
um Programa que peça a temperatura em graus Fahrenheit, transforme e mostre a
temperatura em graus Celsius. C = 5 * ((F-32) / 9).
"""

fahrenheit = float(input("Digite a temperatura em Fahrenheit: "))

celsius = 5 * ((fahrenheit - 32)/9)

print("A temperatura {:.1f} graus Fahrenheit corresponde a {:.1f} graus celsius".format(fahrenheit, celsius))]

"""4- Faça
um Programa que peça um número correspondente a um determinado ano e em seguida
informe se este ano é ou não bissexto.
"""

ano = int(input("Digite o número do ano: "))

if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print("O ano de {} é Bissexto".format(ano))

else:
    print("O  ano de {} não é Bissexto".format(ano))

"""5 - Faça
um programa que gera uma lista dos números primos existentes entre 1 e um
número inteiro informado pelo usuário.

"""

numero = int(input("Digite um número: "))
lista = []

for lista in range(1, numero +1):
    if lista % 2 == 1 and lista != 2 or lista ==2:
        print("Os números primos são {}".format(lista))

"""6 - Faça
um Programa que peça a idade e a altura de 5 pessoas, armazene cada informação
no seu respectivo vetor. Imprima a idade e a altura na ordem inversa a ordem
lida.

"""

idades = []
alturas = []

for i in range (0, 5):
    idade = int(input("Digite a idade da {}ª pessoa ".format(i+1)))
    idades.append(idade)
    altura = float(input("Digite a altura da pessoa "))
    alturas.append(altura)

print(idades[::-1])
print(alturas[::-1])

"""7- Reverso
do número. Faça uma função que retorne o reverso de um número inteiro
informado.
"""

def reverter(numero):
    return str(numero[::-1])

numero = str(input("Digite um número: ")).strip()

print(f"O número reverso é: {reverter(numero)}")