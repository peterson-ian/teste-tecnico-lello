# Nao sabia se era para fazer teste de mesa, decidi fazer um programa que se comporta como um e exibe tudo que foi calculado

INDICE = 12
SOMA = 0
K = 1

while K < INDICE:
    K += 1 # altera o valor antes de atribuir a variavel SOMA
    print (f'K = {K}')
    SOMA += K # soma o valor de SOMA junto a K
    print (f'SOMA = {SOMA}')
    
print(f'\nRESULTADO FINAL = {SOMA}') # valor final