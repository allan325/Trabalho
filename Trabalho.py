carrinho = []
total_venda = 0

catalogo = {
    101: ["Arroz 5kg", 25.00],
    102: ["Feijão 1kg", 9.50],
    103: ["Leite 1L", 5.19],
    104: ["Café 500g", 15.00]
}
for codigo in catalogo: # mostras os produtos de forma mais facil de entender
 print(f"Codigo {codigo} do produto {catalogo[codigo][0]} preço {catalogo[codigo][1]}")

while True:
 carrinho1 = int(input("Coloque os codigos dos produtos que você quer (0 para terminar):"))
 if carrinho1 == 0:
  print("Você terminou de escolher os produtos.")
  break
 elif 101 <= carrinho1 <= 104 :
  carrinho.append(carrinho1) #colocar no carrinho os codigo que a pessoa 
  print(f"Você adicionado produto {catalogo[carrinho1][0]} no carrinho")
 else:
   print("Esse codigo não existe")

for codigo in carrinho: # fazer a soma dos prodotos
 total_venda += catalogo [codigo][1]

if total_venda == 0:# saber se a pessoa escolheu algum produto
 print("você não escolheu nenhum produto.")
else:
 print(f"Total da compra:{total_venda}")
        