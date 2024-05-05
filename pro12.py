#Codigo para saber el año, mes, dia con la hora.
import datetime
now = datetime.datetime.now()
print(now.strftime("%Y-%m-%d %H:%M:%S"))

#Codigo para saber el año, mes y dia.
import datetime
now = datetime.datetime.now()
print(now.strftime("%Y-%m-%d"))