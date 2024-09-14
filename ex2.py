stringUser = "Teste de Frase AlternaDA" 

countAWords = stringUser.upper().count("A")

if countAWords > 0: 
    print(f"A frase '{stringUser} tem {countAWords} letras `A`")
else :
    print(f"A frase '{stringUser} nao tem letras `A`")