# Operadores lógicos 
# and (e) or (ou) not (nâo)
# and - Todas as condições preciasm ser verdadeiras
# Se qualquer valor for considerado falso, se
# a expressão inteira será avaliada naquele valor
# São considerados falsy
# 0 0.0 '' False
# Também existe o tipo NOne que é usado para representar um não valor

entrada = input('[E]ntrar: [S]air: ')
senha_digitada = input ('Senha: ')

senha_permitida = "123456"

if entrada == 'E' and senha_digitada == senha_permitida:
    print('Entrar')
else:
    print('Sair')
    