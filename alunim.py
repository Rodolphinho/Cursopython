alunos = {}

aluno = ''
media = 0

aluno = 'Aluno1:'
media = 5.6

alunos[aluno] = media


aluno = input ("nome do aluno\n")
media = float(input('Digite a media\n'))

alunos[aluno] = media
print (alunos)


while True :
    aluno = input("Digite o nome do aluno ou sair para sair").upper()
    if aluno =='SAIR':
        break



        
