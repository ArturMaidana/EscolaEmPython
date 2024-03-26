#Discentes: Artur Guilherme e Gustavo Lima
import datetime

while True:
    responsavel = input("Digite o nome do responsável:\n")
    nome = input("Digite o nome da criança:\n")
    idade = int(input("Digite o ano de nascimento da criança:\n"))
    mes_cont = int(input("Digite o mês de nascimento da criança:\n"))
    dia = int(input("Digite o dia do nascimento da criança:\n"))

    hoje = datetime.date.today()
    cont = 0

    while mes_cont != 1:
        mes_cont += 1
        cont += 1
        if mes_cont == 13:
            mes_cont = 1

    ano_atual = hoje.year
    mes_atual = hoje.month
    if mes_atual < 4:
        ano_atual -= 1

    if idade == 2024 or idade == 2023:
        if cont >= 6:
            turma = "Berçário I"
        else:
            print("Crianças com menos de 6 meses não são recebidas na escola")
            continue
    elif idade == 2022:
        cont += 14
        if cont >= 24:
            turma = "Berçário II"
        else:
            turma = "Berçário I"
    elif idade == 2021:
        cont += 26
        if cont >= 36:
            turma = "Maternal I"
        else:
            turma = "Berçário II"
    elif idade == 2020:
        cont += 38
        if cont >= 48:
            turma = "Maternal II"
        else:
            turma = "Maternal I"
    elif idade == 2019:
        cont += 50
        if cont >= 60:
            print("Crianças acima de 4 anos devem ser encaminhadas para outra escola")
        else:
            turma = "Maternal II"
    elif idade <= 2018:
        print("Crianças acima de 4 anos devem ser encaminhadas para outra escola")
        continue
    else:
        print("Inserção de dados inválida")
        continue

    print(f"\nPrezado sr(a), a criança {nome} será encaminhada para a turma {turma}")

    opcao = input("\nDigite:\n1.Cadastrar nova criança\n2.Sair\n")
    if opcao != '1':
        break

print("\nObrigado e até logo!")