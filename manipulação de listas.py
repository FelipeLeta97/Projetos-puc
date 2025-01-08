def retirar(C1,C2):
    listavazia = []
    for numero in C2:
        if numero in C1:
            listavazia
        else:
            listavazia.append(numero)
    return listavazia

def interseasjdb(C1,C3):
    listavazia1 = []
    for numero in C1:
        if numero in C3:
            listavazia1.append(numero)
        else:
            listavazia1
    return listavazia1

def uniao(C2,C3):
    listavazia2 = []
    for numero in C3:
        listavazia2.append(numero)
    for numero1 in C2:
        listavazia2.append(numero1)
    return listavazia2
    


C1= [5,1,6,3,9,7,4]	
C2 = [4,8,1,6,10,2]
C3= [9,1,8,3,7,6,2]    
C4 = [5,7] 
print(interseasjdb(C1,C3))
print(retirar(C1,C2))
print(uniao(C2,C3))