ARQUIVO = "tarefas.txt"

def carregar_tarefas() -> list:
    try:
        with open(ARQUIVO, "r", encoding="utf-8") as f:
            return [linha.strip() for linha in f.readlines()]
    except FileNotFoundError:
        return []

def salvar_tarefas(tarefas: list):
    with open(ARQUIVO, "w", encoding="utf-8") as f:
        for t in tarefas:
            f.write(t + "\n")

while True:
    print("\n1. Adicionar | 2. Listar | 3. Remover | 4. Sair")
    opcao = input("Escolha: ")
    tarefas = carregar_tarefas()

    if opcao == "1":
        nova = input("Nova tarefa: ")
        tarefas.append(nova)
        salvar_tarefas(tarefas)
    elif opcao == "2":
        for i, t in enumerate(tarefas, 1):
            print(f"{i}. {t}")
    elif opcao == "3":
        idx = int(input("Número da tarefa para remover: ")) - 1
        if 0 <= idx < len(tarefas):
            tarefas.pop(idx)
            salvar_tarefas(tarefas)
    elif opcao == "4":
        break