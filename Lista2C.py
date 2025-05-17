funcionario = input()
 
salario_base = float(input())
 
total_vendas = float(input())
 
salario_c_bonus = salario_base + (total_vendas * 15/100)
 
print('{}\nR$ {:.2f}'.format(funcionario, salario_c_bonus))
