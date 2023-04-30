nome = 'Murilo'
altura = 2.0000
idade = 35
peso = 118
imc = peso / (altura * altura)
print (imc)

print (nome, 'tem', altura, 'de altura,','pesa', peso, 'quilos e seu IMC é ',imc )

linha_1 = f'{nome} tem {altura:.3f} de altura'
linha_2 = f',pesa {peso} quilos e seu imc é {imc}'
print(linha_1 + linha_2)