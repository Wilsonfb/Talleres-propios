#Mostrar la table de multiplicar de 1 al 10 segun el usuario.

num=int(input("Digita el numero de la taba que quieras ver: "))
for i in range(1,11):
    print(f"{num} X {i} = {num*i}.")