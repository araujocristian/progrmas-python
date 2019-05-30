import random
lis=[]
while len(lis)<15:
    x=random.randint(10,100) #escolhe um numero aleatorio entre (x,y)
    if x not in lis:
        lis.append(x) #add x a lista
lis.sort() #poe em ordem crescente
print(lis)
