# Operadores in e not in
# Strigs são iteráveis
# 0 1 2 3 4 5 6 7 8 9
# O t á v i o
# -6 -5 -4 -2 -1 -0 

nome = 'Murilo'
print(nome[2])
print('o' in nome)
print('MAMA' in nome)

nome = input ('Digite seu nome:')
encontrar = input('Digite o que deseja encontrar:')

if encontrar in nome:
    print(f'{encontrar} está em {nome}')
else:
    print(f'{encontrar} não está em {nome}')