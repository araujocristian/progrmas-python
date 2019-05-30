a = 80000
b = 200000
x = 0
while a < b :
    a = a + (a*3/100)
    b = b + (b*1.5/100)
    x = x + 1
print ("Sao necessarios %d anos" %x)