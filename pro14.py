class Jugadores_insanos:
    def __init__(self, nombre, edad, balones, mundiales, equipo, pais):
        self.nombre = nombre 
        self.edad = edad
        self.balones = balones
        self.mundiales = mundiales
        self.equipo = equipo
        self.pais = pais
cristiano = Jugadores_insanos ("Cristiano", 39, 5, 0, "Al-Nassr", "Portugal")
messi = Jugadores_insanos ("Messi", 36, 8, 1, "Inter_Miami", "Argentina")
pele = Jugadores_insanos ("Pele", "Muerto", 0, 3, "Retirado", "Brazil")
zidane = Jugadores_insanos ("Zidane", 51, 1, 1, "Retirado", "Francia")
cruyff = Jugadores_insanos ("Cruyff", "Muerto", 3, 0, "Retirado", "Paises Bajos")
maradona = Jugadores_insanos ("Maradona", "Muerto", 1, 1, "Retirado", "Argentina")
while True:
    jugador = input("Digite el jugador que quiere saber para mostrar la informacion: ")
    if jugador == "cristiano":
        print(f"El jugador se llama {cristiano.nombre} el mejor jugador del mundo no por talento si no por motivacion y esfuerzo con una edad de {cristiano.edad} en toda su carrera futbolistica a ganado {cristiano.balones} balones de oro y {cristiano.mundiales} mundiales actualmente juega en el equipo del {cristiano.equipo} nacido en {cristiano.pais} en un ambiente de pobresa.")   
    elif jugador == "messi":
        print(f"Este juagador se conoce como {messi.nombre} uno de los mejores jugadores del mundo ganando {messi.mundiales} mundial y con el mayor recoror de balones conseguidos por un jugador con {messi.balones} a la corta edad de {messi.edad} años nacio de el pais de {messi.pais} y actualmente jugando en el equipo de {messi.equipo}.")
    elif jugador == "pele":
        print(f"{pele.nombre} la gente dice que es el mejor jugador de todos los tiempos por lacnatidad de mundiales que gano siendo la unica persona persona en tener {pele.mundiales} mundiales actualmente se encuentra {pele.edad} y {pele.equipo} en su epoca gano {pele.balones} pero porque en su tiempo no se daba este garn premio y nacio en {pele.pais}.")
    elif jugador == "zidane":
        print(f"{zidane.nombre} uno de los mejores centro campistas que se han conocido con una edad de {zidane.edad} años se encuentra {zidane.equipo} en su vida gano {zidane.balones} balones y gano {zidane.mundiales} mundiales con su pais {zidane.pais} casi ganando otro mundial pero siendo expulsado en un partido haciendo quesu pais perdiera el poder levantar otro mundial.")
    elif jugador == "cruyff":
        print(f"Este jugador conocido como {cruyff.nombre} fue un antes y un despues en su {cruyff.pais} ya que gracias a este gran jugador en su tiempo casi ganando un mundial con el equipo llamado la naraja mecanica pero no pudiendo ganarlo teniendo {cruyff.mundiales} mundiales en toda su carrera pero con la gran cantidad de {cruyff.balones} balones siendo uno de los pocos jugadores en tener 3 balones actualemmente se encuentra {cruyff.equipo} y {cruyff.edad} pero siendo uno demoos mejore4s futbolistas conocidos.")
    elif jugador == "maradona":
        print(f"{maradona.nombre} alguien nacido en {maradona.pais} siendo uno de los mejores jugadores en su epoca y conocidos de su pais ganando en este {maradona.mundiales} mundial actualmente se encuntra {maradona.edad} y {maradona.equipo} y en toda su carrera ganado solo {maradona.balones} balon de oro.")
    elif jugador == "salir":
        break
    else:
        print("Vuelve a intentarlo.")