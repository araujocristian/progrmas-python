n=int(input("N: "))
k=1
a,b=1,1
while k<=n-2:
    a,b=b,a+b
    k+=1
print("F(%d)= %d" %(n,b))
    
    
