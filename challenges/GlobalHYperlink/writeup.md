# Writeup: Global Hyperlink Zone (Hack The Box)

**Categoría:** Misc / Quantum Computing

**Herramientas:** Python 3, Qiskit, Netcat

## 1. Resumen del Reto

El reto nos sitúa frente al prototipo de internet cuántico de *Qubitrix*. Se nos proporciona un script en Python (`server.py`) que actúa como un simulador de circuitos cuánticos usando la librería **Qiskit**. El objetivo es enviar una cadena de instrucciones (compuertas cuánticas) que logre estabilizar 5 nodos (Qubits) bajo un patrón de autenticación muy específico para obtener la flag.

## 2. Análisis Estático (Ingeniería Inversa del Código)

Al revisar el código fuente de `server.py`, la clave se encuentra en la función `initialize_hyperlink`, la cual ejecuta nuestro circuito 256 veces (`shots = 256`) y evalúa los resultados guardados en el arreglo `shares`.

Para que la función retorne `True` y libere la flag, el circuito debe cumplir 4 condiciones estrictas:

* **Superposición Obligatoria:** `if any(set(share) in ({0}, {255}) for share in shares): return False`
Ningún Qubit puede arrojar el mismo valor (puros 0s o puros 1s) en las 256 mediciones. Todos deben estar en un estado de superposición probabilística.
* **Entrelazamiento del Grupo A:** `shares[0] == shares[1] and shares[1] == shares[3]`
Los Qubits 0, 1 y 3 deben colapsar siempre en el mismo resultado exacto.
* **Entrelazamiento del Grupo B:** `shares[2] == shares[4]`
Los Qubits 2 y 4 deben colapsar en el mismo resultado exacto.
* **Independencia de Grupos:** `shares[4] != shares[0]`
El estado del Grupo A y el Grupo B no pueden estar vinculados. Deben ser independientes.

## 3. Desarrollo del Exploit (El Circuito Cuántico)

Sabiendo que el sistema solo admite un set limitado de compuertas (H, S, T, X, CX, CY, CZ), utilizaremos las dos más fundamentales para manipular estados:

* **Compuerta de Hadamard (H):** Pone a un Qubit en superposición (50% de probabilidad de ser 0 o 1).
* **Control-NOT (CX):** Entrelaza dos Qubits (Target y Control).

**Armando el Grupo A:**
Aplicamos Hadamard al Qubit 0 para ponerlo en superposición y luego usamos compuertas CX para que los Qubits 1 y 3 copien su estado.

* `H:0`
* `CX:0,1`
* `CX:0,3`

**Armando el Grupo B:**
Hacemos exactamente lo mismo, pero empezando con el Qubit 2 (para mantener independencia del Grupo A) y entrelazando el Qubit 4.

* `H:2`
* `CX:2,4`

**Payload Final:**
El script requiere que las instrucciones estén separadas por punto y coma (`;`).
`H:0;CX:0,1;CX:0,3;H:2;CX:2,4`

## 4. Troubleshooting Local

Al intentar correr el script localmente para probar el payload, nos topamos con un par de obstáculos del entorno:

1. **Falta de dependencias:** El sistema requería Qiskit.
2. **Protección de entorno (PEP 668):** Las distribuciones modernas bloquean `pip install` global.

**Solución:** Se creó un entorno virtual aislado para instalar las librerías necesarias sin romper los paquetes del sistema gestionados por `apt`.

```bash
python3 -m venv venv
source venv/bin/activate
pip install qiskit qiskit-aer
python3 server.py

```

Al inyectar el payload en el entorno local, obtuvimos un error `FileNotFoundError: [Errno 2] No such file or directory: 'flag.txt'`. Lejos de ser un fallo, esto confirmó que el payload era **100% válido**, ya que el script pasó todas las validaciones lógicas e intentó leer la flag local que no existía.

## 5. Explotación Remota

Con la lógica validada localmente, el paso final fue conectarse a la instancia remota proporcionada por Hack The Box usando Netcat:

```bash
nc <IP_DE_HTB> <PUERTO>

```

Una vez que el banner de *Global Hyperlink Zone* cargó, se inyectó el payload final:

```text
Specify the instructions : H:0;CX:0,1;CX:0,3;H:2;CX:2,4
Hyperlink initialized successfully! Connection ID: HTB{...}

```

**¡Sistema vulnerado y flag obtenida!**
