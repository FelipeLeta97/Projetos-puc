lista = ['fernando', 'adriano', 'gustavo', 'felipe', 'ronaldo', 'henrico']


def omaiusculo(lista):
    nova_lista = []
    for item in lista:
        novastring = ''
        for char in item:
         if char == 'o':
            novastring += 'O'
         else:
            novastring += char
        nova_lista.append(novastring)
    return nova_lista

print(omaiusculo(lista))