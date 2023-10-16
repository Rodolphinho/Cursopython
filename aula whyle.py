

##VOCE DESEJA VERDADE OU DESAFIO?
#UTILIZAR WHILE SE DIGITAR VERDADE PERGUNTAR ALGO QUE PODE SER VERDADE >>>TRUE<<<
# SE ACERTAR SAI DO LOOP E ESCREVE GANHOU >>>SE<<< ERRAR CONTINUA NO WHILE EQT NAO ACERTAR



bandeira = 27
print('>> ESTOU TENTANDO DESENHAR A BANDEIRA DO BRASIL MAS NAO LEMBRO QUANTAS ESTRELAS SÃO')
print ('>> CONSEGUE ME FALAR QUANTAS SÃO? ')

acertou = False
while not acertou:
       jogador = int(input('Quantas estrelas são na bandeira?'))     
       if jogador == bandeira:
              acertou = True
              print ( 'acertou parabens')



