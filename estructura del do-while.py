#   Jeison Teobaldo Garcia Arreaga
# Uso de la estructura del do-while

# Definir el número secreto
numero_secreto = 6  # El número secreto es fijo y es 6
intentos_maximos = 5  # Límite de intentos
intentos = 0  # Contador de intentos

print("🎉 ¡Bienvenido al juego de adivinanza! 🎉")
print("Debes adivinar el número secreto.")
print(f"Tienes {intentos_maximos} intentos para ganar un increíble premio.")

while intentos < intentos_maximos:  # Uso de do-while con intentos limitados
    intento = int(input(" Ingresa un número: "))
    intentos += 1  # Aumenta el contador de intentos

    if intento == numero_secreto:
        print("🎊 ¡Increíble! Has adivinado el número  6  🎉")
        print("🚗 ¡Felicidades! Has ganado un carro 4x4 de ultima generación. 🚗")
        break  # Termina el juego si acierta
    elif intento < numero_secreto:
        print("Muy bajo. Inténtalo de nuevo.")
    else:
        print("Muy alto. Inténtalo de nuevo.")

    # Dar una pista en el tercer intento, dependiendo de la diferencia con el número secreto
    if intentos == 3:
        diferencia = abs(numero_secreto - intento)

        if diferencia == 1:
            print("💡 Pista: Estás a 1 número de acertar.")
        elif diferencia == 2:
            print("💡 Pista: Estás a 2 números de acertar.")
        elif diferencia == 3:
            print("💡 Pista: Estás a 3 números de acertar.")
        elif diferencia == 4:
            print("💡 Pista: Estás a 4 números de acertar.")
        else:
            print("💡 Pista: Estás muy lejos del número secreto.")
        # Si el jugador no adivina en los intentos dados
