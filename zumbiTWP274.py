vetor = ['a','f','g','r','t','y','d','s','c','s']
i = 0
acc=0
while i<10:
    if vetor[i] not in ['a','e','i','o','u']:
        acc+=1
    i+=1
print ("Tem %d consoantes" %acc)
