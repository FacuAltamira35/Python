print("Bienvenido al juego de piedras, papel y tijeras, gana el mejor de 3")

nombre1 = input("Introduce el nombre del jugador1: ")
nombre2 = input("Introduce el nombre del jugador2: ")

can_max_turnos = 3
can_turnos = 0

victorias_jugador1 = 0
victorias_jugador2 = 0

while can_turnos < can_max_turnos:
    jugador1 = input('Hola '+ nombre1 +' ¿Que elijes?: ').lower()
    jugador2 = input('Hola '+ nombre2 +' ¿Que elijes?: ').lower()

    condicion1 = jugador1 == "piedra" and jugador2 == "tijeras"
    condicion2 = jugador1 == "papel" and jugador2 == "piedra"
    condicion3 = jugador1 == "tijeras" and jugador2 == "papel"

    if jugador1 == jugador2:
        print("Fue empate")
    elif condicion1 or condicion2 or condicion3:
        print("Felicitaciones",nombre1,"ganaste la ronda")
        victorias_jugador1 += 1
    else:
        print("Felicitaciones",nombre2,"ganaste la ronda")
        victorias_jugador2 += 1

    if victorias_jugador1 == 2:
        print("Felicitaciones ",nombre1," Ganaste el juego")
        break
    elif victorias_jugador2 == 2:
        print("Felicitaciones",nombre2,"Ganaste el juego")
        break

    if victorias_jugador1 == victorias_jugador2:
        print("Se empato la partida, se debe jugar la ultima para definir")