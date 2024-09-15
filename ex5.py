"""
5) Você está em uma sala com três interruptores, cada um conectado a uma lâmpada em salas diferentes. 
Você não pode ver as lâmpadas da sala em que está, mas pode ligar e desligar os interruptores quantas 
vezes quiser. Seu objetivo é descobrir qual interruptor controla qual lâmpada. Como você faria para descobrir, 
usando apenas duas idas até uma das salas das lâmpadas, qual interruptor controla cada lâmpada?   

R: 
Ligo dois interruptores e depois vou verificar as salas das lâmpadas. 
As lâmpadas que estiverem acesas correspondem aos interruptores que foram ligados. 
A lâmpada que não acendeu está conectada ao interruptor que não foi ativado (já identificado).

Em seguida, volto à sala dos interruptores, desativo um dos interruptores que estava ligado e ligo o interruptor que já identifiquei. 
Vou novamente às salas das lâmpadas e observo. 
A lâmpada que está apagada corresponde ao interruptor que foi desativado, revelando qual interruptor controla aquela lâmpada. 
A lâmpada que permanece acesa é controlada pelo último interruptor que ainda não havia sido identificado.

"""