#Talita está simulando o custo de frete de sua loja virtual. o valor depende da distância:

#Até 50km: R$ 5,00
#De 51 a 150 km: R$ 15,00
#Acima de 150 km: R$ 25,00

distancia = float(input("Por gentileza, digite a distância da nossa loja até sua residência"))

if distancia <= 50:
    print("O valor do frete é R$5,00")
elif distancia <= 150:
    print("O valor do frete é R$15,00")

else:
    print("O valor é R$25,00")