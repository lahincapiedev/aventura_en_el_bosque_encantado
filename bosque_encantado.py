import random
import sys
sys.stdout.reconfigure(encoding='utf-8')
sys.stdin.reconfigure(encoding='utf-8')

# ------------------------------
# Configuración
# ------------------------------
ENERGIA_INICIAL = 70
RECUPERO_DESCANSO = 20
COSTO_LUCHAR = 30

OBJETOS_MAGICOS = {
    "Espada mágica": "Aumenta tu poder de ataque en combate.",
    "Escudo encantado": "Reduce el daño recibido de enemigos o criaturas.",
    "Poción curativa": "Restaura parte de tu energía al consumirla."
}

# ------------------------------
# Estado del jugador
# ------------------------------
energia = ENERGIA_INICIAL
inventario = {}

# ------------------------------
# Auxiliares (validación, separadores, etc.)
# ------------------------------
def separador():
    print("-" * 55)

def leer_opcion_int(mensaje, minimo, maximo):
    """R3 / R3.1: Captura + Validación de rango."""
    while True:
        dato = input(mensaje).strip()
        if dato.isdigit():
            valor = int(dato)
            if minimo <= valor <= maximo:
                return valor
        print(f"Opción inválida. Ingresa un número entre {minimo} y {maximo}.")


def agregar_objeto(nombre):
    """Agrega un objeto al inventario con contador."""
    if nombre in inventario:
        inventario[nombre] += 1
    else:
        inventario[nombre] = 1


def mostrar_inventario():
    """Muestra el inventario con cantidades."""
    if not inventario:
        print("Inventario vacío.")
    else:
        print("🎒 Inventario:")
        for nombre, cantidad in inventario.items():
            print(f"- {nombre} ({cantidad})")

# ------------------------------
# Flujo principal
# ------------------------------
def menu_principal():
    separador()
    print("🌲🌲 BOSQUE ENCANTADO 🌲🌲")# R2
    print("1) Entrar al bosque")
    print("2) Buscar objeto mágico")
    print("3) Salir del juego")
    separador()
    return leer_opcion_int("Elige una opción (1, 2 o 3): ", 1, 3)# R3 / R3.1


def entrar_bosque():
    global energia
    separador()
    print("Has entrado al bosque. Hay dos caminos:")# R4
    print("1) Camino iluminado ✨")
    print("2) Camino oscuro 🌑")
    separador()
    opcion = leer_opcion_int("Elige un camino (1 o 2): ", 1, 2)# R5 / R5.1

    if opcion == 1:
        print("✨ Llegas a un hermoso lago.")# R6
        desc = leer_opcion_int("¿Descansar para recuperar energía? 1) Sí  2) No: ", 1, 2)# R6.1 / R6.2
        if desc == 1:
            energia += RECUPERO_DESCANSO # R6.3
            print(f"Descansas y recuperas {RECUPERO_DESCANSO} puntos de energía.")
        print(f"Energía actual: {energia}")
    else:
        print("🌑 Te rodean criaturas mágicas.")# R7
        accion = leer_opcion_int("¿Qué haces? 1) Luchar  2) Negociar: ", 1, 2)# R8 / R8.1
        if accion == 1:
            energia = max(0, energia - COSTO_LUCHAR)# R9
            print(f"Luchas y pierdes {COSTO_LUCHAR} de energía. Energía actual: {energia}")
        else:
            nombre_objeto = random.choice(list(OBJETOS_MAGICOS.keys()))# R10
            beneficio = OBJETOS_MAGICOS[nombre_objeto]
            agregar_objeto(nombre_objeto)
            print(f"🤝 Negocias con éxito y obtienes: {nombre_objeto} - {beneficio}")
            mostrar_inventario()


def buscar_objeto_magico():
    separador()
    print("🔎 Objetos disponibles (elige uno):")# R11
    nombres = list(OBJETOS_MAGICOS.keys())
    for i, nombre in enumerate(nombres, start=1):
        print(f"{i}) {nombre}")
    separador()

    eleccion = leer_opcion_int("Elige un objeto (1, 2 o 3): ", 1, len(nombres))# R12 / R12.1
    nombre = nombres[eleccion - 1]
    beneficio = OBJETOS_MAGICOS[nombre]

    agregar_objeto(nombre)# R13
    print(f"Has elegido: {nombre}")
    print(f"Beneficio: {beneficio}")
    mostrar_inventario()


def despedida():
    separador()
    print("Gracias por jugar. ¡Hasta la próxima aventura! 👋")# R14


def main():
    separador()
    print("🌟 Bienvenido a la Aventura en el Bosque Encantado 🌟")# R1
    print("Toma tus decisiones con sabiduría y disfruta del viaje.\n")
    separador()
    while True:
        opcion = menu_principal()
        if opcion == 1:
            entrar_bosque()
        elif opcion == 2:
            buscar_objeto_magico()
        else:
            despedida()
            break


if __name__ == "__main__":
    main()
