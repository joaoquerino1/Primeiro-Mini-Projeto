import json
import os

ARQUIVO = 'lista_pessoas.json'

def carregar_lista():
    """Carrega a lista de pessoas do arquivo JSON. Cria vazio se não existir."""
    if os.path.exists(ARQUIVO):
        with open(ARQUIVO, 'r', encoding='utf-8') as f:
            return json.load(f)
    return []

def salvar_lista(lista):
    """Salva a lista de pessoas no arquivo JSON."""
    with open(ARQUIVO, 'w', encoding='utf-8') as f:
        json.dump(lista, f, ensure_ascii=False, indent=2)

def cadastrar_pessoa():
    """Cadastra uma nova pessoa."""
    lista = carregar_lista()
    nome = str(input('Nome: '))
    idade = int(input('Idade: '))
    lista.append({'nome': nome, 'idade': idade})
    salvar_lista(lista)
    print('Pessoa cadastrada com sucesso!')

def listar_pessoas():
    """Lista todas as pessoas."""
    lista = carregar_lista()
    if not lista:
        print('Nenhuma pessoa cadastrada.')
    else:
        print('\n--- Lista de Pessoas ---')
        for i, p in enumerate(lista, 1):
            print(f'{i}. {p["nome"]} - {p["idade"]} anos')
    print()

def main():
    print('=== Sistema de Cadastro de Pessoas ===')
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print('1 - Cadastrar Pessoa')
        print('2 - Listar Pessoas')
        print('3 - Sair')
        op = input('Escolha: ')
        if op == '1':
            cadastrar_pessoa()
        elif op == '2':
            listar_pessoas()
        elif op == '3':
            print('Saindo...')
    pessoas = []
    
    while True:
        mostrar_menu()
        opção = leiaInt("Escolha uma opção: ")
        
        if opção == 1:
            listar_pessoas(pessoas)
            input("\nPressione Enter para continuar...")
            
        elif opção == 2:
            cadastrar_pessoa(pessoas)
            input("\nPressione Enter para continuar...")
        elif opção == 3:
            print("Saindo do sistema...")
            break
        
        else:
            print("Opção inválida! Tente novamente.")
            input("\nPressione Enter para continuar...")