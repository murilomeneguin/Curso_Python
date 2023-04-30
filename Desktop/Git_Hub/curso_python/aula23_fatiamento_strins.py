'''
Fatiamento de strings
012345678
olá mundo
-987654321----Indice negativo
Fatiamento [i:f:p] inicio : fim : passo
Obs.: a função len retorna a qtd de caracteres da str
'''
variavel = 'olá mundo'
print(variavel[-4])
print(variavel[4:8])
print(variavel[0:5])
print(len(variavel))
print(variavel[0:len(variavel):-1])