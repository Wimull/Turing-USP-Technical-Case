def conta_economia(emails):
    emailHandler = [];
    caracteresEconomizados = 0
    for conta in emails:
        conta = conta.split("@")[0]
        emailHandler.append(conta);
        if len(emailHandler) > 1:
            if conta[0] != emailHandler[0][0]: emailHandler.pop(0);
            else:
                for caracteres in emailHandler[0]:
                    if emailHandler[1][0] == caracteres:
                        emailHandler[0] = emailHandler[0].split(caracteres, 1)[1];
                        emailHandler[1] = emailHandler[1].split(caracteres, 1)[1];
                        caracteresEconomizados += 1
                emailHandler.clear()
                emailHandler.append(conta)
                
                    


    return caracteresEconomizados;








print(conta_economia(["aninha123@usp.br","aninhazinha000@usp.br","aninhazinhainha@usp.br","jerson331@usp.br","jersaopika@usp.br","aninhaeudnv@usp.br"]))