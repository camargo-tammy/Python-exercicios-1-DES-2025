#  Juliana está coordenando entregas de projetos e precisa calcular o tempo total necessário 
# para finalizar três tarefas: X, Y e Z.
#  Se alguma tarefa estiver com o tempo de entrega negativo, deve-se exibir uma mensagem de 
# erro e não somar o total.
tempo01 = int(input("Digite o tempo necessário para entregar a atividade X"))
tempo02 = int(input("Digite o tempo necessário para entregar a atividade Y"))
tempo03 = int(input("Digite o tempo necessário para entregar a atividade Z"))

soma = tempo01 + tempo02 + tempo03
if tempo01 < 0:
    print("está dentro do prazo.")
elif tempo02 < 0:
    print("está dentro do prazo.")
elif tempo03 <0:
    print("está dentro do prazo.")
else:
    print("o tempo total foi " , soma)