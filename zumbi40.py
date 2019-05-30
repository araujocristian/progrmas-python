mim= int(input('Quantos minutos foram gastos? '))
if mim < 200:
    val=(mim*0.20)
    print ('A conta custa %.2f.' %val)
else:
    if mim <=400:
        val=(mim*0.18)
        print ('A conta custa %.2f.' %val)
    else:
        if mim > 800:
            val=(mim*0.08)
            print ('A conta custa %.2f.' %val)
        else:
            val=(mim*0.15)
            print ('A conta custa %.2f.' %val)
        
           
