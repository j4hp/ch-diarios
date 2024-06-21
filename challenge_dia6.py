import random


jugador=input("piedra, papel o tijeras: ")

def ppt(jugador,computadora):
    if jugador == 'piedra' and computadora == 'piedra':
        print("empate")
    elif jugador == 'papel' and computadora == 'papel':
        print('empate')
    elif jugador == "tijeras" and computadora == 'tijeras':
        print('empate')

    elif jugador== 'piedra'and computadora == 'papel':
        print('gana la computadora')

    elif jugador=='piedra' and computadora == 'tijeras':
        print('gana el jugador')

    elif jugador == 'papel' and computadora == 'piedra':
        print('gana el jugador')

    elif jugador == 'papel' and computadora == 'tijeras':
        print('gana la computadota')

    elif jugador == 'tijeras' and computadora == "piedra":
        print('gana la computadora')
    
    elif jugador =="tijeras" and computadora == "papel":
        print("gana el jugador")

computadora=['piedra','papel','tijeras']

computadora_movimiento= random.choice(computadora)

print(f'la computadora eligio {computadora_movimiento} y el jugador eligio {jugador}')

ppt(jugador,computadora_movimiento)