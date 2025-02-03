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