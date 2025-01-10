#  Produtos, quantidades e o valor total sem desconto 

print("Bem-vindo(a)! Digite seu nome:")
nome = input()
print(f"Olá, {nome}! Vamos começar.")


valor_unitario = float(input("Digite o valor unitário do produto: "))
quantidade = int(input("Digite a quantidade: "))


valor_total = valor_unitario * quantidade
if valor_total < 2500:
    desconto = 0
elif valor_total >= 2500 and valor_total < 6000:
    desconto = 0.04
elif valor_total >= 6000 and valor_total < 10000:
    desconto = 0.07
else:
    desconto = 0.11

# Exigência de Código 4 de 6
valor_sem_desconto = valor_total
valor_com_desconto = valor_total * (1 - desconto)

print(f"\n Obrigado, {nome}! Até a próxima.")


if valor_total < 2500:
    print(f"Valor total da compra: R$ {valor_sem_desconto:.2f} (sem desconto)")
else:
    print(f"Valor total da compra: R$ {valor_sem_desconto:.2f}")
    print(f"Valor total com desconto: R$ {valor_com_desconto:.2f}")
