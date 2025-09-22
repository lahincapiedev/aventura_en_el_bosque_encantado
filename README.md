
# Aventura en el Bosque 🧙‍♂️🌲

## ¿Qué hace este programa?

Este programa simula una mini-aventura por consola en la que el jugador puede:

- Elegir en un **menú principal**:
  - Entrar al bosque
  - Buscar un objeto mágico
  - Salir del juego

### Detalles de las opciones:

- **Entrar al bosque**:
  - Camino iluminado: posibilidad de **descansar** y recuperar energía.
  - Camino oscuro: decidir si **luchar** (pierdes energía) o **negociar** (obtienes un objeto al azar).

- **Buscar un objeto mágico**:
  - Escoger entre tres objetos: **Espada**, **Escudo**, **Poción**.
  - Cada objeto tiene un beneficio que se muestra al seleccionarlo.

- **Inventario**:
  - Guarda los objetos recolectados con sus cantidades.
  - Si se repite un objeto, se muestra como `Objeto (2)`.

- **Energía**:
  - El jugador comienza con una energía inicial que puede aumentar o disminuir según sus acciones.

- **Validación de entradas**:
  - Se evitan errores típicos al ingresar opciones no válidas.

---



## 🔍 Explicación por secciones (resumen)

### Imports

- `random`: Para elegir un objeto al azar al negociar con criaturas.
- `sys`: Para configurar la codificación en UTF-8 y evitar errores con acentos/emojis en Windows.

### Constantes (configuración del juego)

- `ENERGIA_INICIAL`: Energía inicial del jugador.
- `RECUPERO_DESCANSO`: Energía que se recupera al descansar.
- `COSTO_LUCHAR`: Energía que se pierde al luchar.
- `OBJETOS_MAGICOS`: Diccionario con objetos mágicos y sus beneficios.

### Estado del jugador

- `energia`: Variable que cambia durante el juego.
- `inventario`: Diccionario `{nombre_objeto: cantidad}` que almacena objetos recolectados.

### Funciones auxiliares

- `separador()`: Imprime una línea divisoria para mayor legibilidad.
- `leer_opcion_int(mensaje, minimo, maximo)`: Valida que la entrada sea un número válido dentro de un rango.
- `agregar_objeto(nombre)`: Añade un objeto al inventario o incrementa su cantidad.
- `mostrar_inventario()`: Muestra los objetos recolectados en formato `"Nombre (cantidad)"` o `"Inventario vacío"`.

### Flujo principal del juego

- `menu_principal()`: Muestra las tres opciones principales y devuelve la elección.
- `entrar_bosque()`: Gestiona el camino iluminado (descanso) y el oscuro (lucha o negociación).
- `buscar_objeto_magico()`: Permite escoger un objeto y muestra su beneficio.
- `despedida()`: Muestra un mensaje final al salir del juego.
- `main()`: Bucle que mantiene activo el juego hasta que el jugador decide salir.

### Punto de entrada

```python
if __name__ == "__main__":
    main()
```

Esto asegura que el juego se ejecute solo si se corre directamente el archivo.

---

## ✅ Buenas prácticas utilizadas

- **Validación de entradas**: A través de `leer_opcion_int`, se evita que el programa crashee por errores de entrada.
- **Uso de constantes**: Permiten modificar fácilmente las reglas del juego.
- **Funciones pequeñas y claras**: Facilitan la lectura y el mantenimiento del código.
- **Inventario con diccionario**: Control eficiente de objetos y cantidades.
- **Soporte UTF-8 en consola de Windows**: Asegura correcta visualización de acentos y emojis.
