def detmaior(L):
    maior = L[0]
    for numero in L:
        if numero > maior:
            maior = numero
    return maior

def maiornumero(L):
    soma = 0
    maior1 = detmaior(L)
    for numero in L:
        if numero != maior1:
            soma += numero
    return soma




L=[10,-10,3,89,34,-66,23,9,89,12,23,34,-11,20,31,89,20] 
print(detmaior(L))
print(maiornumero(L))