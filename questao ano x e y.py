# Construa uma função para
# A-->Mostrar os 20 primeiros números da serie 1/2, 1/3,1/4,...
def mostraTermosA():
    numerador = 1 
    denominador = 1 
    while denominador <= 20:
        fração = numerador/(denominador + 1)
        print(f'Termos: {denominador}, resultado: {fração:.4f}')
        denominador += 1 
    return

# A1-->Mostrar a soma dos 20 primeiros números da serie 1/2, 1/3,1/4,...
def somtermos():
    numerador = 1
    denominador = 1
    soma = 0
    while denominador <= 20:
        fração = numerador/(denominador + 1)
        denominador += 1 
        soma += fração
    return soma



#B -->Mostrar do m-ésimo ao n-ésimo termos números da serie 1/2, 1/3,1/4,...
#    (m e n recebidos pela função)
def mostraTermosB(m,n):
   numerador = 1 
   denominador = m
   while denominador <= n:
       fração = numerador/(denominador + 1)
       print(f'Termos: {denominador}, resultado: {fração:.4f}')
       denominador += 1 
   return




#C--> exibir os n (recebido pela função) primeiros números da serie 1/2, 1/3,1/4, e 
#     retornar a soma dos termos
def mostraTermosESomaC():
    numerador = 1 
    denominador = 1
    soma = 0
    while denominador <= 4:
        fração = numerador /(denominador + 1)
        denominador += 1
        soma += fração
    return soma


#D --> Mostrar os termos da  serie 1/2, 1/3,1/4, 
# até que a soma seja >= 1.8
def mostraTermosAteSomaMaiorD():
    numerador = 1
    denominador = 1 
    soma = 0
    while soma <= 1.8:
        fração = numerador / (denominador + 1)
        print(f'Termos: {denominador}, resultado: {fração:.4f}')
        denominador += 1
        soma += fração
    return soma


#E --> Mostrar os termos da  serie 1/2, 1/3,1/4, 
# até que a diferença entre  dois termos consecutivos 
# seja < 0.001
def mostraTermosAteDiferencaE():
    numerador = 1
    denominador = 1 
    denominador1 = 2
    conta = 1
    while conta >= 0.001:
        fração1 = numerador/ (denominador + 1)
        fração2 =  numerador/ (denominador1 + 1)
        print(f'Termos: {denominador}, resultado: {fração1:.4f}')
        denominador += 1 
        denominador1 += 1
        conta = fração1 - fração2
    return 
    

#F--> Mostrar os termos da  serie 1/2, 1/3,1/4, 
# até que a soma seja >= 1.8
#retorne  quantos termos estão no intervalo de 0.25 a 0.28

def mostraTermosAteSomaMaiorF():
    numerador = 1
    denominador = 1  
    soma = 0
    quantidadedeintervalos = 0
    while soma < 1.8:
        fração = numerador/(denominador +1)
        if fração >= 0.25 and fração <= 0.28:
            quantidadedeintervalos += 1
        print(f'Termos:{denominador}, resulatdo: {fração:.4f}')
        denominador += 1 
        soma += fração            
    return quantidadedeintervalos

#G-> Mostrar os termos da  serie 1/2, 1/3,1/4, 
# até que a soma seja >= 1.8 a partir do n-ésimo termo
#retorne  quantos termos estão no intervalo de 0.25 a 0.28
def mostraTermosAteSomaMaiorG(n):
    numerado = 1
    denominador = n
    soma = 0
    quantidadeintervalos = 0
    while soma < 1.8:
        fração = numerado / (denominador + 1)
        if fração >= 0.25 and fração <= 0.28:
            quantidadeintervalos += 1
        print(f'Termos:{denominador}, resulatdo: {fração:.4f}')
        denominador += 1
        soma += fração
    return quantidadeintervalos

#BP
print("\nTeste da função A")
mostraTermosA()

print(somtermos())

print("\nTeste da função B")
mostraTermosB(5,10)
print("Como a função do item A")
mostraTermosB(1,20)

print("\nTeste da função C")
soma=mostraTermosESomaC()
print("Soma dos 5 primeiros termos da serie: %.4f"%(soma))

print("\nTeste da função D")
mostraTermosAteSomaMaiorD()

print("\nTeste da função E")
mostraTermosAteDiferencaE()

print("\nTeste da função F")
qtTermos=mostraTermosAteSomaMaiorF()
print(qtTermos)
# print("Qtade de termos entre 0.25 e 0.28: %d"%(qtTermos))

print("\nTeste da função G")
n=int(input("Qual o nºinicial do termo? "))
    
qtTermos=mostraTermosAteSomaMaiorG(n)
print("Qtade de termos entre 0.25 e 0.28: %d"%(qtTermos))
    
qtTermos=mostraTermosAteSomaMaiorG(8)
print("Qtade de termos entre 0.25 e 0.28: %d"%(qtTermos))
