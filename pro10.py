class Empresa:
    def __init__(self, nombre, dias):
        self.nombre = nombre
        self.dias = dias
        self.salario_diario = 40000
    def calcular_salario(self):
        return self.dias * self.salario_diario
empleado1 = Empresa(nombre="Cristiano", dias=20)
empleado2 = Empresa(nombre="Falcao", dias=25)
print(f"Empleado 1 ({empleado1.nombre} los días trabajados son {empleado1.dias} y el salario final es de ${empleado1.calcular_salario():,.2f}.")
print(f"Empleado 2 ({empleado2.nombre} los días trabajados son {empleado2.dias} y el salario final es de ${empleado2.calcular_salario():,.2f}.")
print(f"La nomina total de la empresa es de ${empleado1.calcular_salario() + empleado2.calcular_salario():,.2f}")