a = int(input('n1= '))
b = int(input('n2= '))

while a%b != 0:
    a,b = b,a%b

print ("MDC: %d" %b)
    
