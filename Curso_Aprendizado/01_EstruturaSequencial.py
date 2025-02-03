# site: https://wiki.python.org.br/ListaDeExercicios

# 01. Faça um Programa que mostre a mensagem "Alo mundo" na tela.

mensagem = "Olá mundo"
print(mensagem)

# 02. Faça um Programa que peça um número e então mostre a mensagem O número informado foi [número].

numero = input("Digite um número: ")
print("O número informado foi: ", numero)

# 03. Faça um Programa que peça dois números e imprima a soma.

numero1 = int(input("Digite o primeiro número: "))
numero2 = int(input("Digite o segundo número: "))
soma = numero1 + numero2
print("A soma dos números é: ", soma)

# 04. Faça um Programa que peça as 4 notas bimestrais e mostre a média.

nota_1 = float(input("Digite a primeira nota: "))
nota_2 = float(input("Digite a segunda nota: "))
nota_3 = float(input("Digite a terceira nota: "))
nota_4 = float(input("Digite a quarta nota: "))
media = (nota_1 + nota_2 + nota_3 + nota_4) / 4
print("A média das notas é: ", media)

# 05. Faça um Programa que converta metros para centímetros.

mentro = float(input("Digite o valor em metros: "))
centimetro = mentro * 100
print("O valor em centímetros é: ", centimetro)

# 06. Faça um Programa que peça o raio de um círculo, calcule e mostre sua área.

raio = float(input("Digite o raio do círculo: "))
area = 3.14 * (raio ** 2)
print("A área do círculo é: ", area)

# 07. Faça um Programa que calcule a área de um quadrado, em seguida mostre o dobro desta área para o usuário.

lado = float(input("Digite o valor do lado do quadrado: "))
area = lado ** 2
print("A área do quadrado é: ", area)
print("O dobro da área do quadrado é: ", area * 2)

# 08. Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês.

valor_hora = float(input("Digite o valor da hora trabalhada: "))
horas_trabalhadas = float(input("Digite o número de horas trabalhadas no mês: "))
salario = valor_hora * horas_trabalhadas
print("O salário no referido mês é: ", salario)

# 09. Faça um Programa que peça a temperatura em graus Fahrenheit, transforme e mostre a temperatura em graus Celsius. C = 5 * ((F-32) / 9).

fahrenheit = float(input("Digite a temperatura em Fahrenheit: "))
celsius = 5 * ((fahrenheit - 32) / 9)
print("A temperatura em Celsius é: ", celsius)

# 10. Faça um Programa que peça a temperatura em graus Celsius, transforme e mostre em graus Fahrenheit.

celsius = float(input("Digite a temperatura em Celsius: "))
fahrenheit = (celsius * 9/5) + 32
print("A temperatura em Fahrenheit é: ", fahrenheit)

# 11. Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
    # a. o produto do dobro do primeiro com metade do segundo .
    # b. a soma do triplo do primeiro com o terceiro.
    # c. o terceiro elevado ao cubo.

numero1 = int(input("Digite o primeiro número inteiro: "))
numero2 = int(input("Digite o segundo número inteiro: "))
numero3 = float(input("Digite o número real: "))
a = (numero1 * 2) * (numero2 / 2)
b = (numero1 * 3) + numero3
c = numero3 ** 3
print("O produto do dobro do primeiro com metade do segundo é: ", a)
print("A soma do triplo do primeiro com o terceiro é: ", b)
print("O terceiro elevado ao cubo é: ", c)

# 12. Tendo como dados de entrada a altura de uma pessoa, construa um algoritmo que calcule seu peso ideal, usando a seguinte fórmula: (72.7*altura) - 58

altura = float(input("Digite a altura da pessoa: "))
peso_ideal = (72.7 * altura) - 58
print("O peso ideal da pessoa é: ", peso_ideal)

# 13. Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule seu peso ideal, utilizando as seguintes fórmulas:
    # a. Para homens: (72.7*h) - 58
    # b. Para mulheres: (62.1*h) - 44.7

altura = float(input("Digite a altura da pessoa: "))
peso_ideal_homem = (72.7 * altura) - 58
peso_ideal_mulher = (62.1 * altura) - 44.7
print("O peso ideal para homens é: ", peso_ideal_homem)
print("O peso ideal para mulheres é: ", peso_ideal_mulher)

# 14. João Papo-de-Pescador, homem de bem, comprou um microcomputador para controlar o rendimento diário de seu trabalho. Toda vez que ele traz um peso de peixes maior que o estabelecido pelo regulamento de pesca do estado de São Paulo (50 quilos) deve pagar uma multa de R$ 4,00 por quilo excedente. João precisa que você faça um programa que leia a variável peso (peso de peixes) e calcule o excesso. Gravar na variável excesso a quantidade de quilos além do limite e na variável multa o valor da multa que João deverá pagar. Imprima os dados do programa com as mensagens adequadas.

peso_peixes = float(input("Digite o peso dos peixes: "))
excesso = peso_peixes - 50
multa = excesso * 4
print("O peso dos peixes é: ", peso_peixes)
print("O excesso de peso é: ", excesso)
print("O valor da multa é: ", multa)

# 15. Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês, sabendo-se que são descontados 11% para o Imposto de Renda, 8% para o INSS e 5% para o sindicato, faça um programa que nos dê:
    # a. salário bruto.
    # b. quanto pagou ao INSS.
    # c. quanto pagou ao sindicato.
    # d. o salário líquido.
    # e. calcule os descontos e o salário líquido, conforme a tabela abaixo:
        # + Salário Bruto : R$
        # - IR (11%) : R$
        # - INSS (8%) : R$
        # - Sindicato ( 5%) : R$
        # = Salário Liquido : R$
        
valor_hora = float(input("Digite o valor da hora trabalhada: "))
horas_trabalhadas = float(input("Digite o número de horas trabalhadas no mês: "))
salario_bruto = valor_hora * horas_trabalhadas
ir = salario_bruto * 0.11
inss = salario_bruto * 0.08
sindicato = salario_bruto * 0.05
salario_liquido = salario_bruto - ir - inss - sindicato
print("+ Salário Bruto: R$", salario_bruto)
print("- IR (11%): R$", ir)
print("- INSS (8%): R$", inss)
print("- Sindicato (5%): R$", sindicato)
print("= Salário Líquido: R$", salario_liquido)

# 16. Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00. Informe ao usuário a quantidades de latas de tinta a serem compradas e o preço total.

area = float(input("Digite o tamanho da área a ser pintada em metros quadrados: "))
litros = area / 3
latas = litros / 18
preco = latas * 80
print("A quantidade de latas de tinta a serem compradas é: ", latas)
print("O preço total é: R$", preco)

# 17. Faça um Programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00 ou em galões de 3,6 litros, que custam R$ 25,00.
    # Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços em 3 situações:
        # comprar apenas latas de 18 litros;
        # comprar apenas galões de 3,6 litros;
        # misturar latas e galões, de forma que o desperdício de tinta seja o menor possível. Acrescente 10% de folga e sempre arredonde os valores para cima, isto é, considere latas cheias.

area = float(input("Digite o tamanho da área a ser pintada em metros quadrados: "))
litros = area / 6
latas = litros / 18
preco_latas = latas * 80
galoes = litros / 3.6
preco_galoes = galoes * 25
latas_misturadas = int(latas)
if latas_misturadas < latas:
    latas_misturadas += 1   
preco_latas_misturadas = latas_misturadas * 80
galoes_misturados = int(galoes)
if galoes_misturados < galoes:
    galoes_misturados += 1
preco_galoes_misturados = galoes_misturados * 25
latas_misturadas = int(litros / 18)
litros_restantes = litros % 18
galoes_misturados = int(litros_restantes / 3.6)
if litros_restantes % 3.6 != 0:
    galoes_misturados += 1
preco_misturado = (latas_misturadas * 80) + (galoes_misturados * 25)
print("A quantidade de latas de tinta a serem compradas é: ", latas)
print("O preço total das latas é: R$", preco_latas)
print("A quantidade de galões de tinta a serem comprados é: ", galoes)
print("O preço total dos galões é: R$", preco_galoes)
print("A quantidade de latas de tinta a serem compradas é: ", latas_misturadas)
print("A quantidade de galões de tinta a serem comprados é: ", galoes_misturados)
print("O preço total da mistura é: R$", preco_misturado)

# 18. Faça um programa que peça o tamanho de um arquivo para download (em MB) e a velocidade de um link de Internet (em Mbps), calcule e informe o tempo aproximado de download do arquivo usando este link (em minutos).

tamanho = float(input("Digite o tamanho do arquivo em MB: "))
velocidade = float(input("Digite a velocidade do link de Internet em Mbps: "))
tempo = (tamanho * 8) / velocidade
print("O tempo aproximado de download do arquivo é: ", tempo, "minutos")

