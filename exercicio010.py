# Renata quer solicitar um financiamento, mas precisa verificar se cumpre os critérios:

# Salário mensal acima de R$ 3.000,00
# A parcela não pode ser maior que 35% do salário
salario = float(input("Digite o salário mensal de Renata: R$ "))
parcela = float(input("Digite o valor da parcela do financiamento: R$ "))

if salario <= 3000:
    print("Financiamento negado, salário abaixo do minímo exigido.")
elif parcela > salario * 0.35:
    print("Financiamento negado, parcela acima de 35% do salário.")
else:
    print("Financiamento aprovado!")
