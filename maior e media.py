lista = [1,2,3,4,5,6,7,8,9,10]


def detmaior(lista):
    maior = max(lista)
    return maior

def mediaOutros(lista):
    maior = detmaior(lista)
    resultado = [valor for valor in lista if valor != maior]  
    calculo = sum(resultado) // len(resultado)
    return calculo





print(detmaior(lista))
print(mediaOutros(lista))