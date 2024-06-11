import os
import struct

def main():
    nomeArq = input("Informe o nome do arquivo: ")
    opcao = menu()
    if opcao == "1":
        if os.path.exists(nomeArq):
            ENTRADA = nomeArq.open(nomeArq, 'wb')
            enserir_reg(ENTRADA)





def ler_dado_user():
    campos = ["Sobrenome", "Primeiro nome", "Endereco", "Cidade", "Estado", "CEP"]
    dado
    for compo in campos:
        dado = input(f"Informe o {compo}: ")
        dado += dado+"|"

    return dado

def enserir_reg(entrada):
    dados = ler_dado_user()
    entrada.seek(os.SEEK_END)





def menu():
    print('''
                SUA OPCOES SÃO:
                [1]. ENSERIR UM NOVO REGISTRO
                [2]. BUSCAR UM REGISTRO POR RRN PARA ALTERACOES''')
    
    opcao = input("Selecione sua opcao: ")
    return opcao