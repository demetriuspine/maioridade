idade = int(input('Qual a sua idade?'))
if idade >= 18:
	print('Você é maior de idade')
elif idade >= 13 and idade < 18:
	print('Você é um adolescente')
else:
	print('Você é uma criança')
