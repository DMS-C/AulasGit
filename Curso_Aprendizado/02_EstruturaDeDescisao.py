"""
# 1. Faça um Programa que peça dois números e imprima o maior deles.
# 2. Faça um Programa que peça um valor e mostre na tela se o valor é positivo ou negativo.

nun1 = int(input("Digite o primeiro número: "))
nun2 = int(input("Digite o segundo número: "))
maior = max(nun1, nun2)

print("O maior número é: ", maior)

if nun2 > 0:
    print("O número é positivo.")
else:
    print("O número é negativo.")

# 3. Faça um Programa que verifique se uma letra digitada é "F" ou "M". Conforme a letra escrever: F - Feminino, M - Masculino, Sexo Inválido.

sexo = input("Digite o sexo (F ou M): ")
if sexo == "F":
    print("F - Feminino")
elif sexo == "M":
    print("M - Masculino")
else:
    print("Sexo Inválido")

# 4. Faça um Programa que verifique se uma letra digitada é vogal ou consoante.

vogais = ["a", "e", "i", "o", "u"]
letra = str(input("Digite uma letra: "))
if letra in vogais:
    print("A letra é uma vogal.")
else:
    print("A letra é uma consoante.")

# 5. Faça um programa para a leitura de duas notas parciais de um aluno. O programa deve calcular a média alcançada por aluno e apresentar:
# - A mensagem "Aprovado", se a média alcançada for maior ou igual a sete;
# - A mensagem "Reprovado", se a média for menor do que sete;
# - A mensagem "Aprovado com Distinção", se a média for igual a dez.

nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
media = (nota1 + nota2) / 2
if media == 10:
    print("Aprovado com Distinção")
elif media >= 7:
    print("Aprovado")
else:
    print("Reprovado")

# 6. Faça um Programa que leia três números e mostre o maior deles.
# 7.Faça um Programa que leia três números e mostre o maior e o menor deles.

nun1 = int(input("Digite o primeiro número: "))
nun2 = int(input("Digite o segundo número: "))  
nun3 = int(input("Digite o terceiro número: "))
maior = max(nun1, nun2, nun3)
menor = min(nun1, nun2, nun3)
print("O maior número é: ", maior)
print("O menor número é: ", menor, "o marior número é: ", maior)

# 8. Faça um programa que pergunte o preço de três produtos e informe qual produto você deve comprar, sabendo que a decisão é sempre pelo mais barato.

prod1 = float(input("Digite o preço do primeiro produto: "))
prod2 = float(input("Digite o preço do segundo produto: ")) 
prod3 = float(input("Digite o preço do terceiro produto: "))
menor = min(prod1, prod2, prod3)
print("O produto mais barato é: ", menor)

# 9. Faça um Programa que leia três números e mostre-os em ordem decrescente.

nun1 = int(input("Digite o primeiro número: "))
nun2 = int(input("Digite o segundo número: "))
nun3 = int(input("Digite o terceiro número: "))
lista = [nun1, nun2, nun3]
lista.sort(reverse=False)
print("Os números em ordem decrescente são: ", lista)

# 10. Faça um Programa que pergunte em que turno você estuda. Peça para digitar M-matutino ou V-Vespertino ou N- Noturno. Imprima a mensagem "Bom Dia!", "Boa Tarde!" ou "Boa Noite!" ou "Valor Inválido!", conforme o caso.

turno = input("Digite o turno em que você estuda (M-matutino ou V-Vespertino ou N- Noturno): ")    
if turno == "M":
    print("Bom Dia!")
elif turno == "V":
    print("Boa Tarde!")
elif turno == "N":
    print("Boa Noite!")
else:
    print("Valor Inválido!")

# 11. As Organizações Tabajara resolveram dar um aumento de salário aos seus colaboradores e lhe contraram para desenvolver o programa que calculará os reajustes.
#   Faça um programa que recebe o salário de um colaborador e o reajuste segundo o seguinte critério, baseado no salário atual:
#   salários até R$ 280,00 (incluindo) : aumento de 20%
#   salários entre R$ 280,00 e R$ 700,00 : aumento de 15%
#   salários entre R$ 700,00 e R$ 1500,00 : aumento de 10%
#   salários de R$ 1500,00 em diante : aumento de 5% Após o aumento ser realizado, informe na tela:
#   o salário antes do reajuste;
#   o percentual de aumento aplicado;
#   o valor do aumento;
#   o novo salário, após o aumento.

salario = float(input("Digite o salário do colaborador: "))
if salario <= 280:
    reajuste = 20
    aumento = salario * 0.20
elif salario <= 700:
    reajuste = 15
    aumento = salario * 0.15
elif salario <= 1500:
    reajuste = 10
    aumento = salario * 0.10
else:    
    reajuste = 5
    aumento = salario * 0.05
novo_salario = salario + aumento
print("Salário antes do reajuste: R$", salario)
print("Percentual de aumento aplicado: ", reajuste, "%")
print("Valor do aumento: R$", aumento)
print("Novo salário, após o aumento: R$", novo_salario)


# 12. Faça um programa para o cálculo de uma folha de pagamento, sabendo que os descontos são do Imposto de Renda, que depende do salário bruto (conforme tabela abaixo) e 3% para o Sindicato e que o FGTS corresponde a 11% do Salário Bruto, mas não é descontado (é a empresa que deposita). O Salário Líquido corresponde ao Salário Bruto menos os descontos. O programa deverá pedir ao usuário o valor da sua hora e a quantidade de horas trabalhadas no mês.
#   Desconto do IR:
#   Salário Bruto até 900 (inclusive) - isento
#   Salário Bruto até 1500 (inclusive) - desconto de 5%
#   Salário Bruto até 2500 (inclusive) - desconto de 10%
#   Salário Bruto acima de 2500 - desconto de 20% Imprima na tela as informações, dispostas conforme o exemplo abaixo. No exemplo o valor da hora é 5 e a quantidade de hora é 220.

valor_hora = float(input("Digite o valor da hora trabalhada: "))
horas_trabalhadas = float(input("Digite o número de horas trabalhadas no mês: "))
salario_bruto = valor_hora * horas_trabalhadas
fgts = salario_bruto * 0.11
sindicato = salario_bruto * 0.03
inss = salario_bruto * 0.10
if salario_bruto <= 900:
    ir = 0
elif salario_bruto <= 1500:
    ir = salario_bruto * 0.05   
elif salario_bruto <= 2500:
    ir = salario_bruto * 0.10
else:
    ir = salario_bruto * 0.20
salario_liquido = salario_bruto - ir - inss
print("+ Salário Bruto: R$", salario_bruto)
print("- IR: R$", ir)
print("- INSS: R$", inss)
print("- Sindicato: R$", sindicato)
print("+ FGTS: R$", fgts)
print("= Salário Líquido: R$", salario_liquido)

# 13. Faça um Programa que leia um número e exiba o dia correspondente da semana. (1-Domingo, 2- Segunda, etc.), se digitar outro valor deve aparecer valor inválido.

 # solução 1
dia = int(input("Digite um número correspondente ao dia da semana: "))
if dia == 1:
    print("Domingo")
elif dia == 2:
    print("Segunda")
elif dia == 3:
    print("Terça")
elif dia == 4:
    print("Quarta")
elif dia == 5:
    print("Quinta")
elif dia == 6:
    print("Sexta")
elif dia == 7:
    print("Sábado")
else:
    print("Valor Inválido")

# solução 2
dia = int(input("Digite um número correspondente ao dia da semana: "))
dias = {1: "Domingo", 2: "Segunda", 3: "Terça", 4: "Quarta", 5: "Quinta", 6: "Sexta", 7: "Sábado"}
if dia in dias:
    print(dias[dia])
else:
    print("Valor Inválido")

# 14. Faça um programa que lê as duas notas parciais obtidas por um aluno numa disciplina ao longo de um semestre, e calcule a sua média. A atribuição de conceitos obedece à tabela abaixo:
#   Média de Aproveitamento Conceito
#   Entre 9.0 e 10.0 A
#   Entre 7.5 e 9.0 B
#   Entre 6.0 e 7.5 C
#   Entre 4.0 e 6.0 D
#   Entre 4.0 e zero E
# O algoritmo deve mostrar na tela as notas, a média, o conceito correspondente e a mensagem “APROVADO” se o conceito for A, B ou C ou “REPROVADO” se o conceito for D ou E.

nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
media = (nota1 + nota2) / 2
if media >= 9:
    conceito = "A"  
elif media >= 7.5:
    conceito = "B"
elif media >= 6:
    conceito = "C"
elif media >= 4:
    conceito = "D"
else:
    conceito = "E"
if conceito in "ABC":
    situacao = "APROVADO"
else:
    situacao = "REPROVADO"
print("=> Nota 1: ", nota1)
print("=> Nota 2: ", nota2)
print("=> Média: ", media)
print("=> Conceito: ", conceito)
print("=> Situação: ", situacao)

"""