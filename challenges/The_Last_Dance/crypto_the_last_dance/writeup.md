# HTB Writeup: The Last Dance

**Categoría:** Criptografía

**Dificultad:** Fácil

**Vulnerabilidad:** Reutilización de Nonce (Nonce Reuse) en Cifrado de Flujo

**Flag:** `HTB{und3r57AnD1n9_57R3aM_C1PH3R5_15_51mPl3_a5_7Ha7}`

---

## 1. Análisis del Reto

Al descomprimir el archivo del reto, encontramos dos archivos principales:

1. **`source.py`**: El código fuente en Python que describe el proceso de cifrado.
2. **`out.txt`**: Los datos de salida interceptados que contienen el Nonce (IV) y dos textos cifrados en formato hexadecimal.

### El Código Fuente (`source.py`)

El punto crítico del script es cómo se utiliza el algoritmo **ChaCha20**:

```python
def encryptMessage(message, key, nonce):
    cipher = ChaCha20.new(key=key, nonce=iv) # 'iv' se pasa como nonce
    ciphertext = cipher.encrypt(message)
    return ciphertext

# ... 

# Se generan una clave y un IV una sola vez
key, iv = os.urandom(32), os.urandom(12)

# Se cifran DOS mensajes distintos con el MISMO par (key, iv)
encrypted_message = encryptMessage(message, key, iv)
encrypted_flag = encryptMessage(FLAG, key, iv)

```

## 2. La Vulnerabilidad: Nonce Reuse

ChaCha20 es un **cifrado de flujo** (stream cipher). Estos algoritmos funcionan generando una secuencia de bits pseudoaleatorios llamada **keystream** ($K$), la cual se combina con el texto plano ($P$) mediante la operación **XOR** ($\oplus$) para producir el texto cifrado ($C$).

La seguridad de estos sistemas depende de que el par **(Clave, Nonce)** nunca se repita. Si se repite, el keystream generado es **idéntico** para ambos mensajes.

Matemáticamente:

1. $C_{mensaje} = P_{mensaje} \oplus K$
2. $C_{flag} = P_{flag} \oplus K$

Como conocemos el texto plano del primer mensaje ($P_{mensaje}$) y su correspondiente texto cifrado ($C_{mensaje}$), podemos despejar el keystream:


$$K = C_{mensaje} \oplus P_{mensaje}$$

Una vez obtenido $K$, podemos recuperar la Flag:


$$P_{flag} = C_{flag} \oplus K$$

## 3. Explotación (Script de Resolución)

Para obtener la bandera, desarrollamos un script que realiza las operaciones XOR sobre los datos de `out.txt`.

```python
# Datos extraídos de out.txt
c1_hex = "7aa34395a258f5893e3db1822139b8c1f04cfab9d757b9b9cca57e1df33d093f07c7f06e06bb6293676f9060a838ea138b6bc9f20b08afeb73120506e2ce7b9b9dcd9e4a421584cfaba2481132dfbdf4216e98e3facec9ba199ca3a97641e9ca9782868d0222a1d7c0d3119b867edaf2e72e2a6f7d344df39a14edc39cb6f960944ddac2aaef324827c36cba67dcb76b22119b43881a3f1262752990"
c2_hex = "7d8273ceb459e4d4386df4e32e1aecc1aa7aaafda50cb982f6c62623cf6b29693d86b15457aa76ac7e2eef6cf814ae3a8d39c7"

# Texto plano conocido (extraído de source.py)
p1 = b"Our counter agencies have intercepted your messages and a lot "
p1 += b"of your agent's identities have been exposed. In a matter of "
p1 += b"days all of them will be captured"

c1 = bytes.fromhex(c1_hex)
c2 = bytes.fromhex(c2_hex)

def xor(a, b):
    return bytes(x ^ y for x, y in zip(a, b))

# Paso 1: Recuperar el Keystream
keystream = xor(c1, p1)

# Paso 2: Descifrar la Flag usando el mismo Keystream
flag = xor(c2, keystream)

print(f"Flag: {flag.decode()}")

```

## 4. Conclusión

El reto "The Last Dance" ilustra por qué el **Nonce** (Number used ONCE) debe ser único para cada operación de cifrado. La reutilización del estado interno del cifrado anula por completo la confidencialidad, permitiendo a un atacante recuperar información sensible sin necesidad de conocer la clave secreta.

---

