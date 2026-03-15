import statistics
import os
import datetime
agora = datetime.datetime.now() 
hora1 = agora.strftime(' %d/%m/%Y %H:%M:%S')
carrinho = []
total_venda = 0

catalogo = {
    101: ["Arroz 5kg", 25.00],
    102: ["Feijão 1kg", 9.50],
    103: ["Leite 1L", 3.79],
    104: ["Café 500g", 26.98],
    105: ["Açucar 5kg", 16.90],
    106: ["Óleo de Soja 900ml", 6.79],
    107: ["Pão De Forma 400g", 5.69],
    108: ["Manteiga 200g", 10.20],
    109: ["Cartela De Ovos 20un", 17.90],
    110: ["Sal Refinado 1kg", 3.79],
    111: ["Refrigerante Guaraná 2L", 8.79]
}

def limpar_tela(): #Comando Para Limpar a Tela
    os.system(cls if os.name == 'nt' else 'clear')

#Mostrar Lista De Produtos
def mostrar_catalogo():
    print("===== Catálogo De Produtos =====")
    for codigo, (nome, preco) in catalogo.items():
        print(f"Codigo: {codigo} | Produto: {nome} | Preço: R$ {preco:.2f}")
    print()

mostrar_catalogo()

pagamento = "N/A"
escolha_compra = None

while True:
   try:
       carrinho1 = int(input("\nEscolha Os Produtos De Acordo Com Os Códigos (Digite 0 P/ Finalizar| Negativo (-) Para Remover): "))
       #Definir Forma de Pagamento No Final Da Compra 
   except :
     print("\nOperação Inválida!")  #impede a pessoa de colocar letra e da erro
     continue
   if carrinho1 == 0:
      os.system('cls' if os.name == 'nt' else 'clear') #Limpa Tela Antes De Escolher A Forma De Pagamento
      while True:
        if len(carrinho) > 0:
            print("\nFORMAS DE PAGAMENTO:")
            print("\n1 - Dinheiro - (10% De Desconto No Valor Da Compra)")
            print("\n2 - Cartão de Crédito/Débito")
            print("\n3 - PIX - (10% De Desconto No Valor Da Compra)")
        try:
             escolha_compra = int(input("\nEscolha a forma de pagamento: "))
        except :
            print("Digite um número das opções: Escolha a forma de pagamento") #impede a pessoa de colocar letra e da erro
            continue
         
        opcoes_pagamento = {1: "Dinheiro", 2: "Cartão", 3: "PIX"}
        pagamento = opcoes_pagamento.get(escolha_compra, "Não Informado") 
        if pagamento == "Não Informado":
           print("Digite um número das opções: Escolha a forma de pagamento") # se não for  opcão de pagamento ele volta
           continue
        else: 
         print("Compra Finalizada.")
         break
      break
    #Remover Uma Unidade Do Produto Do Carrinho
   if carrinho1 < 0:
        codigo_para_remover = abs(carrinho1)
        if codigo_para_remover in carrinho:
            carrinho.remove(codigo_para_remover)
            print(f"\nREMOVIDO: {catalogo[codigo_para_remover][0]} Saiu Do Carrinho.")
        else:
            print("Este Produto Não Está No Seu Carrinho")

   elif 101 <= carrinho1 <= 111:
        carrinho.append(carrinho1)
        print(f"\nVocê Adicionou -- {catalogo[carrinho1][0]} No Carrinho")

   else:
        print("Código Inválido")

for codigo in carrinho:
    total_venda += catalogo[codigo][1]

lista_precos = [] #Lista Preços dos Itens Para Cálculo da Média

for codigo in carrinho:
    preco_item = catalogo[codigo][1]
    total_venda += preco_item
    lista_precos.append(preco_item)

# Aplicar 10% de desconto para Dinheiro ou PIX 
desconto = 0.0
if escolha_compra == 1 or escolha_compra == 3:
    desconto = total_venda * 0.10

total_final = total_venda - desconto

fim = datetime.datetime.now()
hora2 = fim.strftime('%d/%m/%Y %H:%M:%S')

os.system('cls' if os.name == 'nt' else 'clear') #Limpa Tela Antes De Mostrar Resumo Da Compra

if total_venda == 0:
    print("Você Não Escolheu Nenhum Produto.")
else:
    print(f"Inicio: {hora1}")
    print(f"Fim:    {hora2}")
    print("="*40)
    print(f"Subtotal: R$ {total_venda:.2f}")
    print("-"*40)
    media = statistics.mean(lista_precos)
    print(f"Média Dos Preços Por Produto: R${media:.2f}")
    print("-"*40)
    if desconto > 0:
        print(f"Desconto (10%): - R$ {desconto:.2f}")
        print("-"*40)
    print(f"Total da compra: R$ {total_final:.2f}")
    print("-"*40)
    if pagamento != "N/A":
        print(f"Forma de pagamento: {pagamento}")
