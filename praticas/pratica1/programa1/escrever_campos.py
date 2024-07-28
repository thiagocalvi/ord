def escreve_campos():
    NOME_ARQ = input("Digite o nome do arquivo a ser criado: ")
    
    SAIDA = open(NOME_ARQ, 'w')
        
    # Receber sobrenome
    sobrenome = input("Digite o sobrenome (ou deixe vazio para terminar): ")
            
    while sobrenome != "":

        SAIDA.write(sobrenome + '|')
    
        nome = input("Digite o nome: ")
        SAIDA.write(nome + '|')
        
        endereco = input("Digite o endereço: ")
        SAIDA.write(endereco + '|')
        
        cidade = input("Digite a cidade: ")
        SAIDA.write(cidade + '|')
        
        estado = input("Digite o estado: ")
        SAIDA.write(estado + '|')
        
        cep = input("Digite o cep: ")
        SAIDA.write(cep + '|')

        sobrenome = input("Digite o sobrenome (ou deixe vazio para terminar): ")    
    
    SAIDA.close()

escreve_campos()