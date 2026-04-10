# 🛡️ Writeup de Intrusión: Xochipilli (10.0.5.4)

**Dificultad:** Avanzada (Non-rootable)

**Objetivo:** Obtener el contenido de `/app/flag`

**Flag Capturada:** `ETSCTF_92e8197f821ed06a145a95228a10b93b`

---

## 1. Fase de Reconocimiento

El escaneo inicial con `nmap` fue bloqueado por un firewall agresivo que aplicaba _Rate Limiting_. Para evadir esta restricción, se utilizó un **escáner multihilo en Python** que detectó un puerto no estándar abierto:

- **Puerto Identificado:** `1337/tcp`
    
- **Servicio:** Ruby WEBrick 1.8.1
    

Al realizar una petición `GET` a la raíz (`/`), el servidor respondió revelando su propio **código fuente**. Esto expuso la lógica de dos endpoints: `/` (disclosure) y `/sdl` (procesamiento).

## 2. Análisis de Vulnerabilidad (Code Injection)

El endpoint `/sdl` aceptaba peticiones `POST` y procesaba el cuerpo del mensaje buscando bloques de tipo **GraphQL SDL (Schema Definition Language)** mediante expresiones regulares.

El código vulnerable identificado fue:

Ruby

```
sdl.scan(/enum\s+(\w+)\s*\{([^}]*)\}/m).each do |_, body|
  body.lines.each do |line|
    instance_eval(line) # <--- PUNTO DE INYECCIÓN
  end
end
```

### El Fallo:

La función `instance_eval` en Ruby toma una cadena y la ejecuta como código dentro del contexto del objeto actual. Al no sanitizar las líneas dentro del bloque `enum { ... }`, el servidor permite la **Ejecución Remota de Código (RCE)**.

---

## 3. Explotación y RCE

Para obtener la flag, se diseñó un payload que cumpliera con la estructura de un `enum` para engañar al `regex`, pero que inyectara una instrucción de lectura de archivos.

Se aprovechó que el servidor redirigía el `$stdout` a la respuesta HTTP (`res.body`), permitiendo ver el resultado de cualquier comando `puts` directamente en la terminal.

### Payload Final:

Bash

```
curl -X POST http://10.0.5.4:1337/sdl -d 'enum Exploit {
  puts(File.read("/app/flag"))
}'
```

### Ejecución paso a paso:

1. **`sdl.scan`** detecta el bloque `enum Exploit { ... }`.
    
2. El bucle extrae la línea `puts(File.read("/app/flag"))`.
    
3. **`instance_eval`** ejecuta la instrucción en el servidor.
    
4. El contenido de `/app/flag` es escrito en el objeto `out` y devuelto al atacante.
    

---

## 4. Resultados e Impacto

- **Nivel de Acceso:** Ejecución de código arbitrario con los privilegios del usuario que corre el servicio Ruby.
    
- **Flag:** `ETSCTF_92e8197f821ed06a145a95228a10b93b`
    
- **Puntos Obtenidos:** 600 pts.
    

> [!NOTE]
> 
> Aunque el reto era "Non-rootable", el RCE permitió el control total de la lógica de la aplicación y el acceso a secretos sensibles dentro del contenedor.

---

**¡Misión cumplida en Xochipilli!** ¿Te gustaría que usemos ese mismo RCE para intentar una **Reverse Shell** y explorar si hay otros contenedores en la misma red antes de cerrar la sesión?