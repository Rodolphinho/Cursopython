#aula eif elif else



#entrada = input ('voce quer entrar ou sair?')

#if entrada == 'entrar':
    #print('voce entrou no sistema')


#elif entrada == 'sair':
    #print ('voce saiu')
#else:
    #print('vc nao entrou nem saiu bobao')
    #




nome = 'Rodolpho'
sobrenome = 'Souza'
idade= 22
ano_nascimento = 2023 - idade
peso = 65
altura_metros = 1.67

maior_idade = idade >= 18

imc = peso // altura_metros ** 2 



print ( 'nome:', nome)
print ('sobrenome:', sobrenome)
print ('idade', idade)
print ('ano de nascimento', ano_nascimento)
print ('altura em metros', altura_metros)
print ('seu imc é', imc)
print ('é de maior?', maior_idade)

entrada = input ('voce quer entrar ou sair?')
if entrada == 'entrar':
    print('Você acabou de adentrar o programa.',)
elif entrada == 'sair':
    print('você desligou o programa.',)

   