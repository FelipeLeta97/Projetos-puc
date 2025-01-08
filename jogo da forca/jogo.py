import random

def  jogodavelha():
    arqE = open('palavras.txt','rt')
    newlista = []
    tentativas = 0
    acertos = 0
    for linha in arqE:
        linhas = linha.strip()
        newlista.append(linhas)
    palavraaleatoria = random.choice(newlista)
    leitura = len(palavraaleatoria)
    palavra = ['_'] * leitura
    print(f'palvra:{palavra}')
    while tentativas < 6 and acertos < leitura:
            n = input('Digite uma letra:')
            if n in palavraaleatoria:
                for i in range(leitura):
                    if palavraaleatoria[i] == n:
                        palavra[i] = n
                        acertos += 1
                print(f'A palavra:{palavra}')
            else:
                print(f'voce errou,a palavra ainda é:{palavra}')
                tentativas += 1
            if acertos == leitura:
                print(f'Voce acertou:{palavraaleatoria}')
    if tentativas == 6 or acertos < leitura:
            print(f'Voce errou,a palavra correta é:{palavraaleatoria} ')
    arqE.close()



jogodavelha()