import math

_number = 6 # valor de entrada

fibonacciSequence = [0, 1] # um array com os valores iniciais ja inputados

def fibonacci(number): # funcao recursiva para calcular
    if number < 0: 
        return "ERRO: Não é possível calcular Fibonacci para números negativos." # tratativa de erros
        
    if number < len(fibonacciSequence): # checa se eh um dos numeros inciais:: 0 ou 1
        return fibonacciSequence[number] # por conta que as unicas possibidades aqui eh somente 0 e 1, se fizer fibonacciSequence[0] ele retorna 0, o mesmo com o 1 

    fibonacciSequence.append(fibonacci(number - 1) + fibonacci(number - 2)) # calcula o proximo numero e adiciona no array
    
    return fibonacciSequence[number] # retorna o valor, importante quando se fala em funcao recursiva


print(fibonacci(_number)) # exibe o resultado