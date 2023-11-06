import math

def rq():
    x = float(input("Primeiro numero"))
    print(math.sqrt(x))
def soma():
    x = float(input("Primeiro numero: "))
    y = float(input("Segundo numero: "))
    print("Soma: ",x+y)
def multi():
    x = float(input("Primeiro numero"))
    y = float(input("Segundo Numero"))
    print("A Multi: ",xy)
def div():
    x = float(input("Primeiro numero"))
    y = float(input("Segundo Numero"))
    print("A Multi: ",x//y)
def sub():
    x = float(input("Primeiro numero: "))
    y = float(input("Segundo numero: "))
    print("Sub: ",x-y)
def fat():
    n = 5
    fat = 1
    i = 2
    while i <= n:
        fat = fat*i
        i = i + 1
        print("O valor de %d! eh =" %n, fat)

num1 = ('')
num2 = ('')
num3 = ('')
x = ((''))
y = ((''))
n = ('')
i = ('')


operacao = (input(str("Escolha qual operacao usar\n"),))
if operacao == ("sub"):
    print (sub())
elif operacao == ("soma"):
    print (soma())
elif operacao == ("fat"):
    print (fat())
elif operacao == ("div"):
    print (div())