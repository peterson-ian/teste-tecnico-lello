stringUser = "Teste de Frase AlternaDA" # entrada de informacao

countAWords = stringUser.upper().count("A") # deixo tudo em caixa para facilitar a contagem

if countAWords > 0: # sei que tem A na frase
    print(f"A frase '{stringUser} tem {countAWords} letras `A`")
else : # caso nao tenha
    print(f"A frase '{stringUser} nao tem letras `A`")