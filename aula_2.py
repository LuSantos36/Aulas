faturamento = 1200
custo = 700
lucro = faturamento - custo
margem_lucro = lucro / faturamento

#print("Faturamento da empresa: ", faturamento, "custo: ", custo, "lucro: ", lucro)
print(f"Faturamento da empresa: R${faturamento:.2f}, Custo: R${custo:.2f}, Lucro:  R${lucro:.2f}")

email_cliente = "email@gmail.com"
# Maiusculas
email_cliente = email_cliente.upper()
print(email_cliente)

# Minusculas
email_cliente = email_cliente.lower()
print(email_cliente)

# "@" encontrar o @ ou outro caracter qualquer
print(email_cliente.find("@")) # retorna -1 quando não encontrar o caracter procurado. 

# Tamanho do texto
print(len(email_cliente))



# Pegar um caractere
print(email_cliente[7])
'''
    Mostra o caracter da posição 4, contando que a primeira posição
    é a de número 0.
'''

print(email_cliente[-3])
'''
    Quando vou pegar um caracter de um grupo e coloco um valor negativo 
    o Python varre o grupo de trás para frente, iniciando do final da cole-
    ção de carcteres.
'''
# Pegar um pedaço do texto
print(email_cliente[:4]) # Neste caso pega os caracteres do inicio até a posição 4,
print(email_cliente[1:4])
print(email_cliente[6:])

# Trocar um pedaço do texto
novo_email = email_cliente.replace("gmail.com", "yahoo.com.br")
print(email_cliente)
print(novo_email)

nome = "josé eduardo soares de lima"

# Trabalhar com nomes
print(nome.capitalize()) # capitalize faz só a primeira letra da frase/nome maiuscula.
print(nome.title()) # title faz a primeira letra de cada palavra maiuscula. 
print(nome.upper()) # todas as letras maiusculas


# Pegar o servidor do email
posicao_arroba = email_cliente.find("@") + 1
servidor = email_cliente[posicao_arroba:]
print(servidor)

# Pegar o 1° nome
posicao_espaco = nome.find(" ")
primeiro_nome = nome[:posicao_espaco].title()
print(primeiro_nome)

# pegar o sobrenome
sobrenome = nome[posicao_espaco+1:].title()
print(sobrenome)

# Casos especiais
margem_lucro = round(margem_lucro, 2)
print(f"Faturamento da empresa: R${faturamento:.2f}, Custo: R${custo:.2f}, Lucro: R${lucro:.2f}, Margem: {margem_lucro: .0%}")
