#Imprimir la table segun desea el usuario que sean la de 10, 50, 100, 150 y 200.

print('''
      1.Imprimir la table del 1 al 10.
      2.Imprimir la table del 1 al 50.
      3.Imprimir la table del 1 al 100.
      4.Imprimir la table del 1 al 150.
      5.Imprimir la table del 1 al 200.
    '''  )
menu=int(input("# "))
num=int(input("Digite la tabla que quiere ver: "))
if menu==1:
    for i in range(1,11):
        print(f"{num} X {i} = {num*i}.")
elif menu==2:
    for i in range(1,51):
        print(f"{num} X {i} = {num*i}.")
elif menu==3:
    for i in range(1,101):
        print(f"{num} X {i} = {num*i}.")
elif menu==4:
    for i in range(1,151):
        print(f"{num} X {i} = {num*i}.")
elif menu==5:
    for i in range(1,201):
        print(f"{num} X {i} = {num*i}.")
else:
    print("Hubo un error intente nuevamente.")