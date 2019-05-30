vetor = []
i = 1
acc = 0
while i<=4:
    n = float(input("Numero: "))
    vetor.append(n)
    acc +=n
    i+=1
print ("Notas :", vetor, "Média: %3.2f" %(acc/4))
    
