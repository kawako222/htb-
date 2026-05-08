# HTB Challenge Writeup: Primed for Action

**Categoría:** Coding / Cryptography

**Dificultad:** Fácil

**Plataforma:** Hack The Box

## 1. Descripción del Problema

Las unidades de inteligencia han interceptado una lista de números enviada por un adversario. La mayoría de los números en la lista son "ruido" o basura, pero dos de ellos son **números primos**. El objetivo es identificar estos dos números primos y calcular su **producto** para obtener la clave de acceso.

**Ejemplo de entrada:** `2 6 7 18 6`

**Ejemplo de salida:** `14` (Dado que 2 y 7 son los únicos primos; $2 \times 7 = 14$)

---

## 2. Análisis Técnico

### Identificación de Primalidad

Para resolver este reto, necesitamos un algoritmo que determine si un número es primo. Un número primo es aquel que solo es divisible por 1 y por sí mismo.

**Optimización:** En lugar de probar todos los divisores desde 2 hasta $n-1$, solo necesitamos probar hasta la **raíz cuadrada de $n$** ($\sqrt{n}$). Si no se encuentra un divisor en ese rango, el número es primo. Esto reduce drásticamente la complejidad computacional.

### Flujo del Algoritmo

1. **Leer la entrada:** Capturar la lista de números proporcionada por la unidad de inteligencia.
2. **Filtrar:** Iterar por cada número de la lista y verificar si es primo.
3. **Almacenar:** Guardar los números primos encontrados en una estructura de datos (lista/vector).
4. **Calcular:** Multiplicar los dos únicos números primos identificados.
5. **Entregar:** Imprimir el resultado.

---

## 3. Implementación (Python)

Elegimos Python por su capacidad para manejar la entrada de datos de forma dinámica y sencilla.

```python
import math
import sys

def es_primo(n):
    # Los números menores a 2 no son primos
    if n < 2:
        return False
    # Verificación optimizada hasta la raíz cuadrada
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def resolver():
    # Leer entrada de stdin
    datos = sys.stdin.read().split()
    if not datos:
        return

    # Convertir a enteros y filtrar los primos
    numeros = [int(x) for x in datos]
    primos_encontrados = [n for n in numeros if es_primo(n)]

    # El reto garantiza que hay exactamente dos
    if len(primos_encontrados) == 2:
        resultado = primos_encontrados[0] * primos_encontrados[1]
        print(resultado)

if __name__ == "__main__":
    resolver()

```

---

## 4. Validación del Caso de Prueba

Tomando la entrada del ejemplo: `2 6 7 18 6`

1. **2:** ¿Es primo? **Sí**. (Primer primo guardado).
2. **6:** ¿Es primo? No (divisible entre 2).
3. **7:** ¿Es primo? **Sí**. (Segundo primo guardado).
4. **18:** ¿Es primo? No (divisible entre 2).
5. **6:** ¿Es primo? No (divisible entre 3).

**Cálculo final:** $2 \times 7 = 14$.

---

## 5. Conclusión

Este desafío pone a prueba la capacidad de implementar lógica matemática básica dentro de un contexto de análisis de señales o inteligencia. La clave del éxito es la eficiencia en la función `es_primo` para manejar listas potencialmente largas sin agotar el tiempo de ejecución (Timeout) del servidor.

**Flag:** [El producto de los dos primos encontrados en tu instancia]
