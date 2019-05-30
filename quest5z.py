p=int(input('Preço: '))
d=int(input('% de desconto: '))

print('Valor do desconto: %d' %(p*(d/100)))
print('Novo Preço: %d' %(p-(p*(d/100))))
