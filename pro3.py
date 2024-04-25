#Imprimir segun lo que escoge el usuario de 1 a 10, 1 a 100, 1 a 1000 o 1 a 10000.

print('''
      MENU:
      1.Imprimir del 1 a 10.
      2.Imprimir del 1 a 100.
      3.Imprimir del 1 a 1000.
      4.Imprimir del 1 a 10000.
      ''')
escoger=int(input("# "))
if escoger==1:
    for i in range(1,11):
        print(i)
elif escoger==2:
    for i in range(1,101):
        print(i)
elif escoger==3:
    for i in range(1,1001):
        print(i)
elif escoger==4:
    for i in range(1,10001):
        print(i)
else:
    print("El programa no pudo funcionar intente nueva mente poniendo un numero segun indica el menu.")
