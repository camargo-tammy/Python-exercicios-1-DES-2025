# Diego está acompanhando seu consumo de internet mensal, que tem um limite de 100 GB.
# O programa deve receber o total consumido e avisar se ele ultrapassou o limite.

consumointernet = int(input("Digite o valor de consumo mensal de internet"))

if consumointernet < 100:
    print("O consumo está dentro limite")
else:
    print("você ultrapassou o limite excedido")