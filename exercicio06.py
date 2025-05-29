# Bianca está programando o controle de acesso a uma plataforma que só funciona entre 9h e 21h.
# O programa deve receber a hora atual (formato 24h) e informar se o acesso é permitido.
horariodefuncionamento = int(input("Digite o horário que você está acessando a plataforma"))

if horariodefuncionamento < 21:
    print("A plataforma está funcionando perfeitamente.")
else:
    print("A plataforma está fora do horário de funcionamento.")