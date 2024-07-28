#9. Faça um programa que abra o arquivo criado no exercício anterior e então leia e apresente as strings
#armazenadas nele. Lembre-se que cada string é precedida por um campo de 2 bytes que armazena o seu
#tamanho. Utilize a informação do tamanho para ler cada string com uma única chamada da função read.

def main():
    nomeArq = input("Informe o nome do arquivo: ")

    try:
        arq = open(nomeArq, 'rb')
        registro = ler_registro(arq) 
        while registro != "":
            print(registro)
            registro = ler_registro(arq) 

    except FileNotFoundError:
        print("Error")

def ler_registro(arq):
    tam = arq.read(2)
    tam_int = int.from_bytes(tam)

    if tam_int > 0:
        buffer = arq.read(tam_int)
        buffer_string = buffer.decode()

        return buffer_string
    else:
        return ""

main()