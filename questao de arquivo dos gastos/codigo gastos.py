def buscar(n,l):
    for pos,elemento in enumerate(l):
        if elemento[0] == n:
            return pos
    return None

arqE = open('Gastos.txt','rt')
def totalgastosdia(arqE):
    soma = 0
    for linha in arqE:
        linhas = linha.strip().split(',')
        if len(linhas) >= 2:
            soma += float(linhas[1])
    return soma
def gastospordia(arqE):
    gastos_dia = []
    for linha in arqE:
        linhas = linha.strip().split(',')
        if len(linhas) >= 3:
            dia = linhas[0]
            valor = float(linhas[1])
            tipo = linhas[2]
            indice = buscar(dia,gastos_dia)
            if indice != None:
               gastos_dia[indice][1].append((tipo, valor))
            else: 
                gastos_dia.append([dia, [(tipo, valor)]])
    for dia,gastos in gastos_dia:
        print(f'dia: {dia}')
        for tipo,valor in gastos:
            print(f'Tipo: {tipo}, Valor:{valor:.2f}')

(gastospordia(arqE))
print(totalgastosdia(arqE))
arqE.close()
