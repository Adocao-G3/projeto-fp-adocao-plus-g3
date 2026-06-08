import src.menus as ui
from datetime import datetime, date
import os 
import random

funcionarios = ["Mateus Davi","Lucas Calixto","João Vitor","João Souza","Maria Giulia", "Jullya Medeiros"]
rodada = []

especies = {
    "1": "cachorro",
    "2": "gato",
    "3": "pássaro",
    "4": "réptil"
}

estados_saude = {
    "1": "bom",
    "2": "médio",
    "3": "ruim"
}

comportamentos = {
    "1": "agitado",
    "2": "calmo",
    "3": "neutro"
}

def cadastro_animal(escolha):
    if escolha == 1: 
        os.system("cls" if os.name == "nt" else "clear")   
        print(ui.TITULO_CADASTRAR_ANIMAL)
        nome_animal = input("Digite o nome do animal: ").title()
        os.system("cls" if os.name == "nt" else "clear")
        
        while True:
            escolha_especie = input(ui.MENU_ESPECIE_ANIMAL)
            if not escolha_especie in especies:
                os.system("cls" if os.name == "nt" else "clear")
                print("\nOpção inválida, digite novamente!")
                continue
            else:
                break
        
        especie_animal = especies[escolha_especie]
        os.system("cls" if os.name == "nt" else "clear")
        raca_animal = input("\nDigite a raça do animal: ").lower()
        os.system("cls" if os.name == "nt" else "clear")

        while True:
            try:
                idade_animal = int(input("\nDigite a idade do animal: "))
                break
            except ValueError:
                os.system("cls" if os.name == "nt" else "clear")
                print("Valor inválido, digite novamente.")
                continue
            
        os.system("cls" if os.name == "nt" else "clear")
        while True:
            escolha_estado_saude = input(ui.MENU_ESTADO_SAUDE)
            if not escolha_estado_saude in estados_saude:
                os.system("cls" if os.name == "nt" else "clear")
                print("\nOpção inválida!")
                continue
            else:
                os.system("cls" if os.name == "nt" else "clear")
                break
            
        estado_saude_animal = estados_saude[escolha_estado_saude]
        
        while True:      
            escolha_comportamento = input(ui.MENU_COMPORTAMENTO)
            if not escolha_comportamento in comportamentos:
                os.system("cls" if os.name == "nt" else "clear")
                print("\nOpção inválida!")
                continue
            else:
                os.system("cls" if os.name == "nt" else "clear")
                break
        
        comportamento_animal = comportamentos[escolha_comportamento]

        while True:
            chegada_animal = int(input(ui.MENU_DATA_CHEGADA))
            if chegada_animal == 1:
                os.system("cls" if os.name == "nt" else "clear")
                data_hoje = date.today()
                data_chegada = data_hoje.strftime("%Y-%m-%d")
                id_animal = datetime.now().strftime("%d%m%Y%H%M%S")
                os.system("cls" if os.name == "nt" else "clear")
                break

            elif chegada_animal == 2:
                os.system("cls" if os.name == "nt" else "clear")

                while True:
                    data_final = input("Digite a data (DD/MM/AAAA): ").strip()
                    if data_final.isdigit() or len(data_final) != 10:
                        os.system("cls" if os.name == "nt" else "clear")
                        print("\nFormato da data inválido.\n")
                        continue
                    dia,mes,ano = data_final.split("/")
                    if not dia.isdigit() or mes.isdigit() or ano.isdigit():
                        os.system("cls" if os.name == "nt" else "clear")
                        print("Formato da data inválido.\n")
                        continue
                    data_chegada = f"{ano}-{mes}-{dia}"
                    id_animal = datetime.now().strftime("%d%m%Y%H%M%S")
                    break
                break

            else:
                os.system("cls" if os.name == "nt" else "clear")
                print("\033[1;31mOpção inválida\033[m") 
        
        with open ("data/animais.csv", "a", encoding = "utf-8") as arquivo:
                arquivo.write(f"{id_animal},{nome_animal},{especie_animal},{raca_animal},{idade_animal},{estado_saude_animal},{comportamento_animal},{data_chegada}\n")
                print("\n\033[1;32mCadastro realizado com sucesso!\033[m")

        return

def verificar_animal(escolha):
    if escolha == 2:
        os.system("cls" if os.name == "nt" else "clear")
        try:
            with open("data/animais.csv", "r", encoding = "utf-8-sig") as arquivo:
                linhas = arquivo.readlines()
                
                nome_verificacao = input("\nQual o nome do animal: ").title()
                os.system("cls" if os.name == "nt" else "clear")

                animais_encontrados = []

                for linha in linhas:
                    if not linha.strip() or "id_animal" in linha:
                        continue
                        
                    dados = linha.split(",")
                    if nome_verificacao == dados[1]:
                        animais_encontrados.append(dados)

                while True:
                    if len(animais_encontrados) == 0:
                        print("Nenhum animal foi encontrado!")
                        break

                    elif len(animais_encontrados) == 1:
                        animal_selecionado = animais_encontrados[0]

                    else:
                        print("\nMais de um animal com o mesmo nome:\n")
                        for i, dados in enumerate(animais_encontrados):
                            print(f"[{i+1}] Nome: {dados[1]} | Espécie: {dados[2]} | Raça: {dados[3]} | Comportamento: {dados[6]}")

                        try:
                            selecao_animal = int(input(ui.MENU_ESCOLHA_ANIMAL))
                            if selecao_animal < 1 or selecao_animal > len(animais_encontrados):
                                os.system("cls" if os.name == "nt" else "clear")
                                print("\nOpção inválida")
                                continue
                            animal_selecionado = animais_encontrados[selecao_animal - 1]
                        except ValueError:
                            os.system("cls" if os.name == "nt" else "clear")
                            print("\nEscolha o animal pela sua numeração.")
                            continue

                    os.system("cls" if os.name == "nt" else "clear")
                    dados = animal_selecionado
                   
                    print(f"{"=" * 36}")
                    print(f"{dados[1].upper()} — {dados[2].upper()}")
                    print(f"{"=" * 36}")
                    print(f"{"Raça":<20} {dados[3].capitalize()}")
                    print(f"{"Idade":<20} {dados[4]} anos")
                    print(f"{"Estado de saúde":<20} {dados[5].capitalize()}")
                    print(f"{"Comportamento":<20} {dados[6].capitalize()}")
                    ano, mes, dia = dados[7].strip().split("-")
                    print(f"{"Data de chegada":<20} {dia}/{mes}/{ano}")
                    print("=" * 36)

                    while True:
                        gerenciar_animal = int(input(ui.MENU_GERENCIAR_ANIMAL))

                        if gerenciar_animal == 1:
                            try:
                                with open("data/agendamentos.csv", "r", encoding = "utf-8-sig") as arquivo:
                                    agendamentos = arquivo.readlines()
                                    agendamentos_encontrados = []

                                    for agendamento in agendamentos[1:]:
                                        if not agendamento.strip():
                                            continue
                                        dados_ag = agendamento.strip().split(",")
                                        if dados_ag[0].strip().lstrip("\ufeff") == animal_selecionado[0]:
                                            agendamentos_encontrados.append(dados_ag)

                                    os.system("cls" if os.name == "nt" else "clear")
                                    if agendamentos_encontrados:
                                        print('=' * 50)
                                        print(f"  AGENDAMENTOS — {animal_selecionado[1].upper()}")
                                        print('=' * 50)
                                        for ag in agendamentos_encontrados:
                                            dia, mes, ano = ag[3].split("/")
                                            dias_restantes = (date(int(ano), int(mes), int(dia)) - date.today()).days
                                            print(f"\n  {ag[2]} | {ag[3]} | {ag[4]}")
                                            if dias_restantes == 0:
                                                print(f"  🔔 HOJE é o dia do agendamento!")
                                            elif dias_restantes > 0:
                                                print(f"  🟢 Faltam {dias_restantes} dia(s).")
                                        print('=' * 50)
                                    else:
                                        print("Nenhum agendamento foi encontrado.")

                            except ValueError:
                                print("Digite um valor válido.")

                        elif gerenciar_animal == 2:
                            animal_tarefa = animal_selecionado[1]
                            id_tarefa = animal_selecionado[0]
                            os.system("cls" if os.name == "nt" else "clear")
                            menu_tarefa = int(input(ui.MENU_OPCOES_AGENDAMENTOS))
                            if menu_tarefa == 1:
                                tarefa = "Vacina"
                            elif menu_tarefa == 2:
                                tarefa = "Banho"
                            elif menu_tarefa == 3:
                                tarefa = "Consulta veterinária"
                            elif menu_tarefa == 4:
                                tarefa = "Treino"

                            while True:
                                data_verificacao = input("\nQual data você deseja, dia/mês/ano: ")
                                data_tarefa = data_verificacao.replace("/","")
                                if data_tarefa.isdigit() and len(data_tarefa) == 8:
                                    data_final = data_tarefa[0:2] + "/" + data_tarefa[2:4] + "/" + data_tarefa[4:8]
                                    break
                                else:
                                    print("\nA data deve seguir o padrão dia/mês/ano (XX/XX/XXXX): ")

                            global rodada
                            if not rodada:
                                rodada = funcionarios[:]
                                random.shuffle(rodada)
                            responsavel_tarefa = rodada.pop()
                            print(f"\nO funcionário responsável pela tarefa é {responsavel_tarefa}.")
                            with open("data/agendamentos.csv", "a", encoding = "utf-8") as arquivo:
                                arquivo.write(f"{id_tarefa},{animal_tarefa},{tarefa},{data_final},{responsavel_tarefa}\n")
                            break

                        else:
                            os.system("cls" if os.name == "nt" else "clear")
                            break 

                    break  

        except FileNotFoundError:
            os.system("cls" if os.name == "nt" else "clear")
            print("\n\033[1;31mNenhum animal cadastrado\033[m")

def atualizar_animal(escolha):
    if escolha == 3:
        os.system("cls" if os.name == "nt" else "clear")
        nome_verificacao = input("\nNome do animal: ").capitalize()

        with open("data/animais.csv", "r", encoding="utf-8") as arquivo:
            linhas = arquivo.readlines()

        animais_nome_verificacao = []
        todas_linhas = []
        animal_escolhido = None

        for linha in linhas:
            todas_linhas.append(linha)

            if not linha.strip() or "id_animal" in linha:
                continue

            dados = linha.split(",")

            if nome_verificacao == dados[1]:
                animais_nome_verificacao.append(dados)
                animal_escolhido = dados

        if animal_escolhido is None or len(animais_nome_verificacao) == 0:
            print("\nAnimal não encontrado!")
            return

        if len(animais_nome_verificacao) != 1:
            for i in range(len(animais_nome_verificacao)):
                print(f"[{i+1}] " + " | ".join(animais_nome_verificacao[i]))

            try:
                escolha_mesmo_nome = int(input("---> Escolha: "))
                if not 1 <= escolha_mesmo_nome <= len(animais_nome_verificacao):
                    print("\nOpção inválida!")
                    return
            except ValueError:
                print("\nDigite um número válido!")
                return

            animal_escolhido = animais_nome_verificacao[escolha_mesmo_nome - 1]

        resultado = editar_info(animal_escolhido)
        if resultado == False:
            return False
        
        if resultado is not None:
            animal_escolhido = resultado

        with open("data/animais.csv", "w", encoding="utf-8") as arquivo:
            for linha in todas_linhas:
                if not linha.strip() or "id_animal" in linha:
                    arquivo.write(linha)
                    continue

                dados = linha.split(",")

                if dados[0] == animal_escolhido[0]:
                    arquivo.write(",".join(map(str, animal_escolhido)) + "\n")
                else:
                    arquivo.write(linha)

def editar_info(animal_escolhido):
    while True:
        os.system("cls" if os.name == "nt" else "clear")
        print(f"\nInformações de {animal_escolhido[1]}:")
        print(f"\n[1] Nome: {animal_escolhido[1]}")
        print(f"[2] Espécie: {animal_escolhido[2]}")
        print(f"[3] Raça: {animal_escolhido[3]}")
        print(f"[4] Idade: {animal_escolhido[4]}")
        print(f"[5] Estado de saúde: {animal_escolhido[5]}")
        print(f"[6] Comportamento: {animal_escolhido[6]}")
        print(f"[7] Data de chegada: {animal_escolhido[7]}")

        info_quer_editar = int(input("Digite o dado a ser editado: "))

        
        if info_quer_editar == 1:
            print(f"\nNome atual: {animal_escolhido[1]}")
            novo_nome = input("Novo nome: ").title().strip()
            animal_escolhido[1] = novo_nome
        
        elif info_quer_editar == 2:
            print(f"\nEspécie atual: {animal_escolhido[2]}")
            nova_especie = input(ui.MENU_ESPECIE_ANIMAL)
            if not nova_especie in especies:
                print("\nEdição falhou! Opção inválida!")
                return False
            animal_escolhido[2] = especies[nova_especie]
        
        elif info_quer_editar == 3:
            print(f"\nRaça atual: {animal_escolhido[3]}")
            nova_raca = input("Nova raça: ").strip().lower()
            animal_escolhido[3] = nova_raca
        
        elif info_quer_editar == 4:
            print(f"\nIdade atual: {animal_escolhido[4]}")
            try:
                nova_idade = int(input("Nova idade: "))
                animal_escolhido[4] = nova_idade
            except ValueError:
                print("\nEdição falhou! Valor de idade inválido")
                return False
        
        elif info_quer_editar == 5:
            print(f"\nEstado de saúde atual: {animal_escolhido[5]}")
            novo_estado_de_saude = input(ui.MENU_ESTADO_SAUDE)
            if not novo_estado_de_saude in estados_saude:
                print("\nEdição falhou! Opção inválida!")
                return False
            animal_escolhido[5] = estados_saude[novo_estado_de_saude]
        
        elif info_quer_editar == 6:
            print(f"\nComportamento atual: {animal_escolhido[6]}")
            novo_comportamento = input(ui.MENU_COMPORTAMENTO)
            if not novo_comportamento in comportamentos:
                print("\nOpção inválida!")
                return False
            animal_escolhido[6] = comportamentos[novo_comportamento]
        
        elif info_quer_editar == 7:
            print(f"\nData de chegada atual: {animal_escolhido[7]}")
            nova_data_chegada = input("Digite a nova data de chegada (DD/MM/AAAA): ")
            if len(nova_data_chegada) != 10:
                print("\nData inválida.")
                return False
            dia,mes,ano = nova_data_chegada.split("/")
            nova_data_formatada = f"{ano}-{mes}-{dia}"
            animal_escolhido[7] = nova_data_formatada

        escolha_quero_editar_mais = input("\n[1] Sim\n[2] Não\n\nVocê deseja editar mais algum dado? ")

        if escolha_quero_editar_mais == "1":
            continue
        elif escolha_quero_editar_mais == "2":
            break

def verificar_especie(escolha):
    
    if not escolha in especies:
        os.system("cls" if os.name == "nt" else "clear")
        print("\nOpção inválida, digite novamente!")
        return False

    especie = especies[escolha]

    especies_encontradas = []

    with open("data/animais.csv", "r", encoding="utf-8") as arquivo:
        linhas = arquivo.readlines()

    for linha in linhas:
        if not linha.strip() or "id_animal" in linha:
            continue

        dados = linha.split(",")

        if dados[2] == especie and dados[5] != "ruim":
            especies_encontradas.append(linha)

    if len(especies_encontradas) == 0:
        os.system("cls" if os.name == "nt" else "clear")
        print("\nInfelizmente não temos nenhum animal dessa especie no momento!")
        
        while True:
            pergunta = input("\n[1] Sim \n[2] Não \n\nVocê deseja buscar por outra espécie? ")

            if pergunta == "1":
                os.system("cls" if os.name == "nt" else "clear")
                return False
            elif pergunta == "2":
                os.system("cls" if os.name == "nt" else "clear")
                return None
            else:
                os.system("cls" if os.name == "nt" else "clear")
                print("\nOpção inválida, digite novamente!")
                continue
        
    else:
        os.system("cls" if os.name == "nt" else "clear")
        return especies_encontradas

def verificar_raca(animais, pergunta):
    os.system("cls" if os.name == "nt" else "clear")

    if pergunta == "1":
        
        racas_disponiveis = []
        cont = 1
        while True:
            for animal in animais:
                dados = animal.split(",")
                if not dados[3] in racas_disponiveis:
                    print(f"[{cont}] {dados[3]}")
                    racas_disponiveis.append(dados[3])
                    cont += 1
            try:
                raca = input("\nDigite a raça do animal desejada (digite N para nenhuma): ").strip().lower()

                if raca != "n" and raca.isdigit():
                    racas_encontradas = []
                    raca = racas_disponiveis[int(raca) - 1]

                    for animal in animais:
                        dados = animal.split(",")
                        if dados[3] == raca:
                            racas_encontradas.append(animal)
                    os.system("cls" if os.name == "nt" else "clear")
                    return racas_encontradas
                
                elif raca == "n":
                    while True:
                        os.system("cls" if os.name == "nt" else "clear")
                        print("\nInfelizmente não temos mais raças disponíveis no momento")
                        escolha = input("\n[1] Sim \n[2] Não \n\nVocê deseja buscar por outra raça? ")

                        if escolha == "1":
                            break
                        elif escolha == "2":
                            break
                        else:
                            os.system("cls" if os.name == "nt" else "clear")
                            print("\nOpção inválida, digite novamente!")
                            continue
                    
                    if escolha == "1":
                            os.system("cls" if os.name == "nt" else "clear")
                            racas_disponiveis = []
                            cont = 1
                            continue
                    elif escolha == "2":
                            os.system("cls" if os.name == "nt" else "clear")
                            return None
                
                else:
                    os.system("cls" if os.name == "nt" else "clear")
                    print("Digite um valor válido\n")
                    racas_disponiveis = []
                    cont = 1
                    continue

            except IndexError:
                os.system("cls" if os.name == "nt" else "clear")
                print("Digite um valor válido\n")
                racas_disponiveis = []
                cont = 1
                continue

    else:
        os.system("cls" if os.name == "nt" else "clear")
        return animais

def verificar_idade(animais, pergunta):
    os.system("cls" if os.name == "nt" else "clear")

    if pergunta == "1":
        try:
            idade_min = int(input("\nDigite a idade mínima do animal (digite -1 para sem idade mínima): "))
            idade_max = int(input("\nDigite a idade máxima do animal (digite -1 para sem idade máxima): "))
        except ValueError:
            print("\nDigite apenas números inteiros!")
            return False

        if idade_min != -1 and idade_max != -1 and idade_min > idade_max:
            print("\nA idade mínima não pode ser maior que a máxima!")
            return False

        if idade_min == -1 and idade_max == -1:
            os.system("cls" if os.name == "nt" else "clear")
            return animais

        idades_encontradas = []
        for animal in animais:

            dados = animal.split(",")
            idade_animal = int(dados[4])

            if idade_min == -1:
                if idade_animal <= idade_max:
                    idades_encontradas.append(animal)
            elif idade_max == -1:
                if idade_animal >= idade_min:
                    idades_encontradas.append(animal)
            else:
                if idade_min <= idade_animal <= idade_max:
                    idades_encontradas.append(animal)

        if len(idades_encontradas) == 0:
            print("\nInfelizmente não temos nenhum animal nessa faixa de idade no momento!")
            return False

        os.system("cls" if os.name == "nt" else "clear")
        return idades_encontradas

    else:
        return animais

def verificar_comportamento(animais, pergunta):
    os.system("cls" if os.name == "nt" else "clear")

    comportamentos = {"1": "agitado", "2": "calmo", "3": "neutro", "4": "sem preferência"}

    animais_encontrados = []

    if pergunta not in comportamentos:
        print("\nOpção inválida!")
        return False

    elif int(pergunta) > 0 and int(pergunta) < 4:
        comportamento = comportamentos[pergunta]
        
        for animal in animais:
            dados = animal.split(",")
            if dados[6] == comportamento:
                animais_encontrados.append(animal)
    
    else:
        for animal in animais:
            animais_encontrados.append(animal)

    if len(animais_encontrados) == 0:
        print("\nInfelizmente não temos nenhum animal com essas características no momento!")
        return False
    elif len(animais_encontrados) == 1:
        dados = animais_encontrados[0].split(",")
        print("\nEncontramos um animal que combina com as características informadas!")
        print(f"\nNome: {dados[1]} \t\tID:{dados[0]}")
    else:
        print("\nEncontramos animais que combinam com as características informadas!")
        for animal in animais_encontrados:
            dados = animal.split(",")
            print(f"\nNome: {dados[1]} \t\tID:{dados[0]}")

    return animais_encontrados

def deletar_animal(escolha):
    if escolha == 4:
        try:
            os.system("cls" if os.name == "nt" else "clear")
            nome_verificacao = input("\nNome do animal: ").title().strip()

            with open("data/animais.csv", "r", encoding="utf-8") as arquivo:
                linhas = arquivo.readlines()

            animais_nome_verificacao = []
            
            for linha in linhas:
                if not linha.strip() or "id_animal" in linha:
                    continue
                
                dados = linha.split(",")
                if nome_verificacao == dados[1]:
                    animais_nome_verificacao.append(linha)

            if len(animais_nome_verificacao) == 0:
                print("\nAnimal não encontrado!")
                return

            elif len(animais_nome_verificacao) == 1:
                animal_escolhido = animais_nome_verificacao[0]

            else:
                for i, animal in enumerate(animais_nome_verificacao, start=1):
                    print(f"\n[{i}]  {animal.strip()}")

                try:
                    escolha_mesmo_nome = int(input("\n---> Escolha: "))
                    os.system("cls" if os.name == "nt" else "clear")
                    if not 1 <= escolha_mesmo_nome <= len(animais_nome_verificacao):
                        print("\nOpção inválida!")
                        return
                except ValueError:
                    print("\nDigite um número válido!")
                    return

                animal_escolhido = animais_nome_verificacao[escolha_mesmo_nome - 1]
                dados = animal_escolhido.strip().split(",")

            print(f"\nInformações de {dados[1]}:")
            print(f"\nEspécie: {dados[2]}")
            print(f"Raça: {dados[3]}")
            print(f"Idade: {dados[4]}")
            print(f"Estado de saúde: {dados[5]}")
            print(f"Comportamento: {dados[6]}")
            print(f"Data de chegada: {dados[7]}")

            try:
                confirmar = input("\n[1] Sim \n[2] Não\n\nTem certeza que deseja deletar este animal? ")
            except ValueError:
                print("\nEntrada inválida!")
                return

            if confirmar == "1":
                with open("data/animais.csv", "w", encoding="utf-8") as arquivo:
                    arquivo.write("id_animal,nome,especie,raca,idade,estado_saude,comportamento,data_chegada\n")
                    for linha in linhas:
                        if not linha.strip() or "id_animal" in linha:
                            continue
                        
                        dados_exclusao = linha.split(",")
                        if dados_exclusao[0] == dados[0]:
                            continue
                        arquivo.write(linha)
                print("\n\033[1;32mAnimal deletado com sucesso!\033[m")
            elif confirmar == "2":
                print("\nDeleção cancelada.")
            else:
                print("\nOpção inválida!")

        except FileNotFoundError:
            print("\033[1;31mNenhum animal cadastrado\033[m")

def excluir_data_passada():
    data_hoje = date.today()
    linhas_validas = []

    with open("data/agendamentos.csv", "r", encoding="utf-8-sig") as arquivo:
        linhas_validas.append(arquivo.readline())

        for linha in arquivo:
            linha = linha.strip()
            if not linha:
                continue

            dados = linha.split(",")
            if len(dados) < 4:
                continue

            try:
                data_formatada = datetime.strptime(dados[3], "%d/%m/%Y").date()
            except ValueError:
                continue

            if data_formatada >= data_hoje:
                linhas_validas.append(linha + "\n")

    with open("data/agendamentos.csv", "w", encoding="utf-8-sig") as arquivo:
        arquivo.writelines(linhas_validas)
