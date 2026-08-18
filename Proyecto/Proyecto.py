
def analizar_password():

    password = input("Ingrese una contraseña: ")

    puntos = 0
    observaciones = []

    if len(password) >= 8:
        puntos += 1
    else:
        observaciones.append("Menos de 8 caracteres")

    tiene_mayuscula = False
    tiene_minuscula = False
    tiene_numero = False
    tiene_simbolo = False

    simbolos = "!@#$%^&*()-_=+."

    for c in password:

        if c.isupper():
            tiene_mayuscula = True

        elif c.islower():
            tiene_minuscula = True

        elif c.isdigit():
            tiene_numero = True

        elif c in simbolos:
            tiene_simbolo = True

    if tiene_mayuscula:
        puntos += 1
    else:
        observaciones.append("No tiene mayúsculas")

    if tiene_minuscula:
        puntos += 1
    else:
        observaciones.append("No tiene minúsculas")

    if tiene_numero:
        puntos += 1
    else:
        observaciones.append("No tiene números")

    if tiene_simbolo:
        puntos += 1
    else:
        observaciones.append("No tiene símbolos")

    if puntos <= 2:
        nivel = "DEBIL"

    elif puntos <= 4:
        nivel = "MEDIA"

    else:
        nivel = "FUERTE"

    print("Resultado:", nivel)

    if len(observaciones) > 0:

        print("Problemas encontrados:")

        for problema in observaciones:
            print("-", problema)


def analizar_url():

    url = input("Ingrese una URL: ")

    riesgo = 0
    alertas = []

    if not url.startswith("https://"):
        riesgo += 1
        alertas.append("No utiliza HTTPS")

    dominios_sospechosos = [
        ".xyz",
        ".top",
        ".click",
        ".info",
        ".biz"
    ]

    for dominio in dominios_sospechosos:

        if dominio in url:
            riesgo += 1
            alertas.append(
                "Dominio sospechoso: " + dominio
            )

    palabras_riesgo = [
        "login",
        "verify",
        "update",
        "secure",
        "bank"
    ]

    for palabra in palabras_riesgo:

        if palabra.lower() in url.lower():
            riesgo += 1
            alertas.append(
                "Palabra sospechosa: " + palabra
            )

    print()

    if riesgo == 0:
        nivel = "BAJO"

    elif riesgo <= 2:
        nivel = "MEDIO"

    else:
        nivel = "ALTO"

    print("Nivel de riesgo:", nivel)

    if len(alertas) > 0:

        print("Alertas detectadas:")

        for alerta in alertas:
            print("-", alerta)

    else:
        print("No se detectaron riesgos evidentes.")

def menu():

    opcion = ""

    while opcion != "3":
        
        print("========== MENU PRINCIPAL ==========")
        
        print("\nAnalisis de seguridad para contraseñas y URLs \n")
        
        print("1. Analizar contraseña")
        print("2. Analizar URL")
        print("3. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            analizar_password()

        elif opcion == "2":
            analizar_url()

        elif opcion == "3":
            print("Gracias por utilizar el programa.")

        else:
            print("Opción incorrecta.")

menu()
