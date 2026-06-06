import src.menus as ui
import src.funcoes as fn
import os
os.system("cls" if os.name == "nt" else "clear")

fn.excluir_data_passada()

while True:
    escolha = int(input(ui.MENU_PRINCIPAL))
    if escolha == 1:
        fn.cadastro_animal(escolha)
    elif escolha == 2:
        fn.verificar_animal(escolha)
    elif escolha == 3:
        fn.atualizar_animal(escolha)
    elif escolha == 4:
        fn.deletar_animal(escolha)
    else:
        print("\033[1;31mOpção inválida\033[m")
    opcao = int(input(ui.MENU_SAIDA))
    if opcao == 1:
        os.system("cls" if os.name == "nt" else "clear")
        continue
    elif opcao == 2:
        os.system("cls" if os.name == "nt" else "clear")
        print("\n\033[1;31mProgama encerrado!\033[m")
        break
    else:
        print("\033[1;31mOpção inválida\033[m")