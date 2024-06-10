relatorios = []


#função que cria um dicionário com os dados do relatório e adiciona o o relatório à lista de relatórios
def armazenar_relatorio(nomeCompleto, data, cordenadas, temperatura, nivelDoMar):
    relatorio = {
        "Nome Completo": nomeCompleto,
        "Data da Análise": data,
        "Coordenadas": cordenadas,
        "Temperatura do Mar": temperatura,
        "Nível do Mar": nivelDoMar
    }
    relatorios.append(relatorio)
    print("\nRelatório armazenado com sucesso!\n")


#função que verifica se o relatório existe
def verificar_indice():
    while True:
        indice = int(input("\nDigite o índice do relatório que deseja.\nÍndice: "))
        if 0 <= indice and indice < len(relatorios):
            print("Relatório encontrado!")
            return indice
        else:
            print("O índice fornecido não existe. Tente novamente.")


#função que verifica se o CPF do usuário está cadastrado
def CPFs(cpf):
    cpfs = [12345678901, 98765432101, 74108529637, 71472583690]
    if cpf in cpfs:
        return "\nCPF encontrado. Você possui permissão!"
    else:
        return "\nCPF não encontrado. Você não possui perimissão!"


#função para pegar o CPF do usuário para saber se ele possui permissão para adicionar informações no app
def permissao():
    cpf = int(input("Digite seu CPF sem pontos ou traços: "))
    resultado = CPFs(cpf)
    print(resultado)
    if "não encontrado" in resultado:
        print("Voltando ao menu. Permissão negada.")
        return menu()


#função para coletar as informações que vão para o relatório
def relatar():
    print("\nOk, já que você deseja relatar as condições da água do mar temos que seguir alguns passos para saber se você tem permissão")
    permissao()

    nomeCompleto = input("""Enão vamos começar!
    Digite seu nome completo?
    Nome: """)

    data = input("""
    Digite a data que foi realizada a análise
    Data: """)

    cordenadas = input("""
    Digite as cordenadas do local que foi feita a análise?
    Cordenadas: """)

    temperatura = float(input("""
    Qual era a temperatura do mar quando medida?
    Temperatura: """))

    nivelDoMar = float(input("""
    Qual era o nível do mar quando medido?
    Nível do mar: """))

    armazenar_relatorio(nomeCompleto, data, cordenadas, temperatura, nivelDoMar)
    return menu()


#função que exibe os relatorios existentes
def exibir_relatorios():
    if not relatorios:
        print("\nNenhum relatório armazenado.")
        return menu()

    print("\nRelatórios Armazenados:")
    for idx, relatorio in enumerate(relatorios):
        print(f"""\nÍndice do Relatório: {idx}
Nome Completo: {relatorio['Nome Completo']}
Data da Análise: {relatorio['Data da Análise']}
Coordenadas: {relatorio['Coordenadas']}
Temperatura do Mar: {relatorio['Temperatura do Mar']}
Nível do Mar: {relatorio['Nível do Mar']}""")
        print("-" * 30)
    return menu()


#função para deletar relatórios
def deletar_relatorio():
    print("\nOk, já que você deseja deletar um relatório temos que seguir alguns passos para saber se você tem permissão")
    permissao()
    indiceDel = verificar_indice()
    relatorios.pop(indiceDel)
    return menu()


#função para editar o relatório desejado
def editar_relatorio():
    print("\nOk, já que você deseja editar um relatório temos que seguir alguns passos para saber se você tem permissão")
    permissao()
    indiceEdit = verificar_indice()
    novo_nome = input("\nDigite o novo nome (ou pressione Enter para manter o atual): ")
    if novo_nome:
        relatorios[indiceEdit]["Nome Completo"] = novo_nome

    nova_data = input("\nDigite a nova data que foi feita a análise (ou pressione Enter para manter o atual): ")
    if nova_data:
        relatorios[indiceEdit]["Data da Análise"] = nova_data
    
    novas_coordenadas = input("\nDigite as novas coordenadas (ou pressione Enter para manter o atual): ")
    if novas_coordenadas:
        relatorios[indiceEdit]["Coordenadas"] = novas_coordenadas
    
    nova_temperatura = input("\nDigite a nova temperatura do mar (ou pressione Enter para manter a atual): ")
    if nova_temperatura:
        relatorios[indiceEdit]["Temperatura do Mar"] = float(nova_temperatura)
    
    novo_nivel = input("\nDigite o novo nível do mar (ou pressione Enter para manter o atual): ")
    if novo_nivel:
        relatorios[indiceEdit]["Nível do Mar"] = float(novo_nivel)

    print(f"Dados do relatório índice {indiceEdit} alterados com sucesso!")
    return menu()




#menu para escolher a opção desejada
def menu():
    print()
    opcaoMenu = input("""Olá, Escolha uma opção:
            1- Relatar condições da água do mar;
            2- Consultar histórico de condições do mar relatadas;
            3- Deletar relatório;
            4- Editar relatório;
            5- Sair.
            OPÇÃO: """)

    if opcaoMenu == "1":
        relatar()
    elif opcaoMenu == "2":
        exibir_relatorios()
    elif opcaoMenu == "3":
        deletar_relatorio()
    elif opcaoMenu == "4":
        editar_relatorio()
    elif opcaoMenu == "5":
        print("\nPrograma encerrado.")
        quit()
    else:
        print("\nOpção inválida.")

menu()