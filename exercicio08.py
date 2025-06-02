# Talita está simulando o custo de frete para sua loja virtual. O valor depende da distância:

# Até 50 km: R$ 5,00
# De 51 a 150 km: R$ 15,00
# Acima de 150 km: R$ 25,00
distancia_km= int(input("Por gentileza, digite a distância da nossa loja até sua residência"))

if distancia_km <= 50:
    print("O valor do frete é R$5,00")
elif distancia_km > 150:
    print("o valor do frete é R$15,00")
elif: distancia_km > 150:
    print("o valor do frete é R$25,00")
else:
    print("Essa informação não se encaixa no sistema.")