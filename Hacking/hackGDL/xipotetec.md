
Aquí tienes el **Writeup Técnico** de la sesión actual:

---

# 🛡️ Writeup de Intrusión: Xipe Totec (10.0.5.4)

**Estado:** Post-Explotación Inicial / Acceso Administrativo

**Objetivo:** Exfiltración de Flags (Env, System, Root)

---

## 1. Fase de Reconocimiento

- **Servicios Activos:** * `Port 22`: SSH (OpenSSH 9.2p1)
    
    - `Port 80`: HTTP (Nginx 1.22.1)
        
- **CMS Detectado:** GasMark Agency System (PHP) por Mayuri K.
    
- **Entorno:** Probable contenedor **Docker** (detectado directorio `/app` y pista de "boxes of sand").
    

## 2. Acceso Inicial (Vulnerabilidad: SQL Injection)

- **Vector:** Bypass de autenticación en `login.php`.
    
- **Payload:** `admin' OR '1'='1'-- -`
    
- **Resultado:** Acceso exitoso al panel de administración.
    
- **Sesión Actual:** `PHPSESSID=i8uikiifa44isdj2ig9onjlknr`
    

## 3. Superficie de Ataque y Hallazgos

- **Arbitrary File Upload:** * Localizado en `manage_website.php`.
    
    - Se subió con éxito una Web Shell PHP (`logo.php`) con cabecera **Polyglot** (`GIF89a`) para evadir filtros de _Magic Bytes_.
        
    - **Ruta física confirmada:** `/assets/uploadImage/Logo/logo.php`.
        
- **Local File Inclusion (LFI):**
    
    - Vector potencial en `index.php?page=`.
        
- **Inyección en Reportes:**
    
    - Endpoint: `php_action/getOrderReport.php` y `print.php`.
        
    - Vulnerable a manipulación de parámetros, aunque la ejecución de comandos (`system`) ha sido bloqueada por el servidor web.
        

## 4. El Bloqueo (The Sandbox)

Actualmente, **Nginx** devuelve un `404 Not Found` al intentar acceder directamente a cualquier archivo `.php` dentro de la carpeta `/assets`.

> **Nota:** Esto confirma la pista de las "cajas de arena": el directorio de recursos estáticos tiene prohibida la ejecución de scripts.

## 5. Pendientes para la nueva máquina

Para obtener los **3,100 puntos**, la estrategia debe ser:

1. **Exfiltrar la Flag `env` (1,300 pts):**
    
    - Usar el LFI para leer `/proc/self/environ` o el archivo `.env` en la raíz.
        
    - Payload sugerido: `index.php?page=php://filter/convert.base64-encode/resource=../.env`
        
2. **RCE (Remote Code Execution):**
    
    - Forzar la inclusión de la shell subida a través del LFI: `index.php?page=assets/uploadImage/Logo/logo&cmd=id`.
        
3. **Escalada de Privilegios (1,800 pts):**
    
    - Una vez dentro del contenedor, enumerar capacidades (`capsh`) y buscar el escape de Docker para llegar al sistema host (Root).
        

---

### 🛠️ Herramientas listas:

- `ffuf` con el diccionario `common.txt` ya filtró los directorios críticos.
    
- `curl` con la sesión activa para evitar el login.
    

¿Te gustaría que te genere un **script de Python** que puedas correr en la nueva máquina para automatizar la búsqueda de la flag de `env` mientras terminas de configurar todo?