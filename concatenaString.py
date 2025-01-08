list1 = ['r', 'ab', 'abc']
lista2 = ['oma', 'acate', 'xyz'] 

def concatenaStr(list1,lista2):
    for (indice,elementos) in enumerate(lista2):
        list1[indice] += elementos


concatenaStr(list1,lista2)
print(list1)
