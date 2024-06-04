def leia_reg(ENTRADA):
    tam = ENTRADA.read(2)
    tam_int = int.from_bytes(tam)

    if tam_int > 0:
        buffer = ENTRADA.read(tam_int)
        buffer_string = buffer.decode()

        return buffer_string
    else:
        return ""


def le_registros():
    NOME_ARQ = input("Informe o nome do arquivo: ")
    contador = 1
    try:
        ENTRADA = open(NOME_ARQ, 'rb')
        buffer = leia_reg(ENTRADA)

        while buffer != "":
            lista_campos = buffer.split("|")

            for campo in lista_campos:
                print(f"Campo #{contador}: {campo}")
                contador += 1

            buffer = leia_reg(ENTRADA)

        ENTRADA.close()
    
    except FileNotFoundError:
        print("Erro: Arquivo não encontrado")
    except Exception as e:
        print(f"Erro: {e}")

    
le_registros()