funcionario = input()
numero_horas = int(input())
valor_pago_h = float(input())
print(funcionario)
salario = (numero_horas * valor_pago_h)
print('R$ {:.2f}'.format(salario))
