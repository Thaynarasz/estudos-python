valor = int(input("Digite o valor de uma casa: "))
salario = int(input("O salario do comprador: "))
anos = int(input("Em quantos anos será pago: "))
prestacao = valor/(anos*12)
porcentagem = salario*0.3
if prestacao <= porcentagem:
    print("Empréstimo aprovado!")
    print(f"A valor das parcelas será de {prestacao}")
else:
    print("Emprestimo não aprovado!")    