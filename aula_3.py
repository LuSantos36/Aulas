idade = 10
'''
if idade >=18:
    print("Você é maior de idade. ")
elif idade <18 and idade > 12:
    print("Você é adolescente. ")
else:
    print("Você é criança. ")


if idade >=18:
    print("Você é maior de idade.")
if idade < 18 and idade >= 12:
    print("Você é adolescente.")
if idade < 12:
    print("Você é criança.")



vendas = 1500
meta = 1300
if vendas >= meta:
    print("Vendedor ganhou bonus. ")
    print("Bateu a meta de vendas. ")
    bonus = 0.1 * vendas
    print(f"Bonus do vendedor: R${bonus:.2f}")
else:
    print("Vendedor não ganhou bonus.")
    print("Não bateu a meta de vendas. ")
print("Acabou o programa. ")

vendas = 1500
meta1 = 1300 # Ganha 10%
meta2 = 2000 # Ganha 13%

if vendas >= 2000:
    bonus = 0.13 * vendas
else:
    if vendas >= 1300:
        bonus = 0.1 * vendas
    else:
        bonus = 0
print("Bonus:" , bonus)

vendas = 2500
vendas_empresa = 10000
meta_empresa = 20000
meta1 = 1300 
meta2 = 1500 

if vendas >= 2000 and vendas_empresa >= meta_empresa:
    bonus = 0.13 * vendas
elif vendas >= 1300 and vendas_empresa >= meta_empresa:
    bonus = 0.1 * vendas
else:
    bonus = 0
print("Bonus:", bonus)
'''

lista_produtos = ["airpod", "ipad", "iphone", "macbook"]
produto_procurado = input ("Procure um produto: ")
produto_procurado = produto_procurado.lower()

if produto_procurado in lista_produtos:
    print("Produto em estoque. ")
else:
    print("Não temos esse produto em estoque. ")
