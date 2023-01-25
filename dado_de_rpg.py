import random

# aqui estão os dados, e os números aleatorios que serão gerados

d4 = random.randrange(1, 4)

d6 = random.randrange(1, 6)

d8 = random.randrange(1, 8)

d10 = random.randrange(1, 10)

d12 = random.randrange(1, 12)

d20 = random.randrange(1, 20)

d100 = random.randrange(1, 100)


resultado_dado = "o dado foi jogado, e o resultado foi {}."
# acima esta uma mensagem que será exibida quando o dado for "jogado"'.


print("Escolha um dos dados, d4, d6, d8, d10, d12, d20 ou d100.")

print("Digite 4 para d4, 6 para d6, 8 para d8, 10 para d10, 12 para d12, 20 para d20, 100 para d100.")

dado_escolhido = int(input("Qual irá escolher?"))

if dado_escolhido == 4:
	print(resultado_dado.format(d4))
	
elif dado_escolhido == 6:
	print(resultado_dado.format(d6))
	
elif dado_escolhido == 8:
	print(resultado_dado.format(d8))
	
elif dado_escolhido == 10:
	print(resultado_dado.format(d10))
	
elif dado_escolhido == 12:
	print(resultado_dado.format(d12))
	
elif dado_escolhido == 20:
	print(resultado_dado.format(d20))
	
elif dado_escolhido == 100:
	print(resultado_dado.format(d100))
# aqui esta o que será exibido quando o usuario escolher um dado
	
else:
	print("Dado não encontrado.")
# mensagem caso o usuario digite um numero que nao seja para escolher um dado.