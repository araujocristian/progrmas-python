s=int(input('Salario: '))
a=int(input('% de aumento: '))

print('Valor do aumento: %d' %(s*(a/100)))
print('Novo Salario: %d' %(s+(s*(a/100))))
