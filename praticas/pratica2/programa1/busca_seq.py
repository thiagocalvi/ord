def main():
    nomeArq = input("Informe o nome do arquivo: ")
    try:
        ENTRADA = open(nomeArq, 'rb')
        CHAVE = input("Informe o sobrenome a ser buscado: ")
        reg = busca_reg(ENTRADA, CHAVE)
        print(reg)
        if reg != "":
            i = 1
            for x in reg:
                print(f"Campo {i}: {x}")
                i += 1
        else:
            print("Dado não encontrado!")

        ENTRADA.close()
    except FileNotFoundError:
        print("Error")
    

def busca_reg(entrada, chave):
    reg_encontradado = False

    while reg_encontradado != True:
        tam = entrada.read(2)
        tam_int = int.from_bytes(tam)

        if tam_int > 0:
            buffer = entrada.read(tam_int)
            buffer_string = buffer.decode()
            buffer_string = buffer_string.split("|")
            if buffer_string[0] == chave:
                return buffer_string
        else:
            return ""
        
main()