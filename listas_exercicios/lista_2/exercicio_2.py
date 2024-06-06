#2. Faça um programa que solicite ao usuário o nome de um arquivo de texto e então calcule e apresente o
#seu tamanho em bytes e o número de linhas do arquivo.

def main():
    nomeArq = input("Informe o nome do arquivo: ")
    tam_bytes, num_linhas = get_informacoes(nomeArq)
    print(f"Tamanho do arquivo em bytes: {tam_bytes}")
    print(f"Número de linhas do arquivo: {num_linhas}")


def get_informacoes(nomeArq):
    return get_tamanho_bytes(nomeArq), get_numero_linhas(nomeArq) 

def get_tamanho_bytes(nomeArq):
    import os
    return os.path.getsize(nomeArq)

def get_numero_linhas(nomeArq):
    with open(nomeArq, 'r') as arq:
        numero_linhas = 0
        for x in arq:
            numero_linhas += 1
    return numero_linhas

if __name__ == '__main__':
    main()