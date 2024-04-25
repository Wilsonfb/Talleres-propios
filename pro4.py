#Mostrar la table de multiplicar de 1 al 100 segun el usuario.

num=int(input("Digite la tabla que quiere ver: "))
for i in range(1,101):
    print(f"{num} X {i} = {num*i}.")