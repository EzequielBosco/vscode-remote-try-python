#-----------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See LICENSE in the project root for license information.
#-----------------------------------------------------------------------------------------

from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return app.send_static_file("index.html")

# write 'hello world' to the console
# print("hello world")

# create game logic piedra papel o tijera, with input to add name of user, player selects option and computer selects random option, compare options and print winner
def game_logic():
    victorias = 0
    rondas = 0
    
    while True:
        print("Juego piedra papel o tijera")
        print("Introduce tu nombre")
        player = input()
        print("Hola " + player + " ¿Que eliges? piedra, papel o tijera?")
        option = input().lower()

        if option not in ["piedra", "papel", "tijera"]:
            print("Opción no válida. Introduce piedra, papel o tijera.")
            continue
        
        print("Tu elegiste: " + option)
        import random
        computer = random.choice(["piedra", "papel", "tijera"])
        print("La computadora eligio: " + computer)

        if option == computer:
            print("Empate")
        elif option == "piedra":
            if computer == "papel":
                print("Gana la computadora")
            else:
                print("Ganaste")
        elif option == "papel":
            if computer == "tijera":
                print("Gana la computadora")
            else:
                print("Ganaste")
        elif option == "tijera":
            if computer == "piedra":
                print("Gana la computadora")
            else:
                print("Ganaste")
        else:
            print("Introduce una opcion correcta")
            victorias += 1

        rondas += 1 
        print("¿Quieres volver a jugar? si o no")
        option = input().lower()
        if option != "si":
            print("Gracias por jugar")
            break

    print(f"Has jugado {rondas} rondas y has ganado {victorias} veces.")

game_logic()