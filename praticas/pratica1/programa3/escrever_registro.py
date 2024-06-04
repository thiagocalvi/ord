def escreve_registros():
    NOME_ARQ = input("Informe o nome do arquivo:")
    SAIDA = open(NOME_ARQ, 'wb')

    sobrenome_campo = input("Digite o sobrenome (ou deixe vazio para terminar): ")
    
    while sobrenome_campo != "":
        buffer = ""
        buffer += sobrenome_campo + "|"

        nome_campo = input("Digite o nome: ")
        buffer += nome_campo + "|"

        endereco_campo = input("Digite o endereço: ")
        buffer += endereco_campo + "|"
        
        cidade_campo = input("Digite a cidade: ")
        buffer += cidade_campo + "|"
        
        estado_campo = input("Digite o estado: ")
        buffer += estado_campo + "|"

        cep_campo = input("Digite o CEP: ")
        buffer += cep_campo + "|"


        buffer_binario = buffer.encode()
        tam = len(buffer_binario)
        tam_binario = tam.to_bytes(2)

        
        SAIDA.write(tam_binario)
        SAIDA.write(buffer_binario)

        sobrenome_campo = input("Digite o sobrenome (ou deixe vazio para terminar): ")
    
    SAIDA.close()

escreve_registros()