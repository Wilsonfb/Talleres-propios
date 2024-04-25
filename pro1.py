#Imprimir todos los numeros o los numeros impares segun el usuraio de 1 a 100.

print('''
      MENU:
      1.Imprimir todos los numeros.
      2.Sacar numeros impares.
      ''')
num=int(input())
if num==1:
    for i in range(1,101):
        print(i) 
elif num==2:
    for i in range(1,101):
        if i % 1 == 0:
            print(i)
else:
    print("Digite un numero valido.")