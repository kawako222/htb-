Primer escaneo:

axmi222 ~   10:22     
❯ nmap -sC -sV 10.129.25.43                                                
Starting Nmap 7.98 ( https://nmap.org ) at 2026-04-07 10:22 -0600  
Nmap scan report for 10.129.25.43  
Host is up (0.076s latency).  
Not shown: 997 closed tcp ports (reset)  
PORT    STATE SERVICE  VERSION  
22/tcp  open  ssh      OpenSSH 9.6p1 Ubuntu 3ubuntu13.15 (Ubuntu Linux; protocol 2.0)  
| ssh-hostkey:    
|   256 8c:45:12:36:03:61:de:0f:0b:2b:c3:9b:2a:92:59:a1 (ECDSA)  
|_  256 d2:3c:bf:ed:55:4a:52:13:b5:34:d2:fb:8f:e4:93:bd (ED25519)  
80/tcp  open  http     nginx 1.24.0 (Ubuntu)  
|_http-server-header: nginx/1.24.0 (Ubuntu)  
|_http-title: Did not follow redirect to https://kobold.htb/  
443/tcp open  ssl/http nginx 1.24.0 (Ubuntu)  
| ssl-cert: Subject: commonName=kobold.htb  
| Subject Alternative Name: DNS:kobold.htb, DNS:*.kobold.htb  
| Not valid before: 2026-03-15T15:08:55  
|_Not valid after:  2125-02-19T15:08:55  
|_http-title: Did not follow redirect to https://kobold.htb/  
| tls-alpn:    
|   http/1.1  
|   http/1.0  
|_  http/0.9  
|_ssl-date: TLS randomness does not represent time  
|_http-server-header: nginx/1.24.0 (Ubuntu)  
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel  
  
Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .  
Nmap done: 1 IP address (1 host up) scanned in 19.52 seconds

Modificar mi etc/hosts

axmi222 …/htb/Kobold   main !?   10:25     
❯ echo "10.129.25.43  kobold.htb" | sudo tee -a /etc/hosts  
[sudo] contraseña para axmi222:    
10.129.25.43  kobold.htb

Checar que ignorar en ffuf por los subdominios
se **`*.kobold.htb`** indica que la máquina está configurada para manejar subdominios

axmi222 …/htb/Kobold   main !?   10:28     
❯ curl -s -k -I -H "Host: no-existo.kobold.htb" https://kobold.htb | grep -i "Content-Length"                
Content-Length: 154


Buscar subdominios

  
axmi222 …/htb/Kobold   main !?   10:28     
❯ ffuf -w /usr/share/wordlists/dirb/common.txt -u https://kobold.htb -H "Host: FUZZ.kobold.htb" -fs 154     
  
       /'___\  /'___\           /'___\          
      /\ \__/ /\ \__/  __  __  /\ \__/          
      \ \ ,__\\ \ ,__\/\ \/\ \ \ \ ,__\         
       \ \ \_/ \ \ \_/\ \ \_\ \ \ \ \_/         
        \ \_\   \ \_\  \ \____/  \ \_\          
         \/_/    \/_/   \/___/    \/_/          
  
      v2.1.0-dev  
________________________________________________  
  
:: Method           : GET  
:: URL              : https://kobold.htb  
:: Wordlist         : FUZZ: /usr/share/wordlists/dirb/common.txt  
:: Header           : Host: FUZZ.kobold.htb  
:: Follow redirects : false  
:: Calibration      : false  
:: Timeout          : 10  
:: Threads          : 40  
:: Matcher          : Response status: 200-299,301,302,307,401,403,405,500  
:: Filter           : Response size: 154  
________________________________________________  
  
bin                     [Status: 200, Size: 24402, Words: 1218, Lines: 386, Duration: 212ms]  
mcp                     [Status: 200, Size: 466, Words: 57, Lines: 15, Duration: 155ms]  
:: Progress: [4614/4614] :: Job [1/1] :: 549 req/sec :: Duration: [0:00:09] :: Errors: 0 ::

volver a editar etc/hosts

127.0.0.1       localhost  
127.0.1.1       linux kali.axmi222      kali  
  
# The following lines are desirable for IPv6 capable hosts  
::1     localhost ip6-localhost ip6-loopback  
ff02::1 ip6-allnodes  
ff02::2 ip6-allrouters  
  
10.10.11.92 conversor.htb  
10.129.244.72 fries.htb  
10.129.15.37 soulmate.htb ftp.soulmate.htb  
10.129.2.85 facts.htb  
154.57.164.66 inlanefreight.htb web1337.inlanefreight.htb dev.web1337.inlanefreight.htb:32715  
10.0.5.4 xochipilli.local  
10.0.4.5 huehueteotl.hackgdl.ctf  
10.0.4.5 huehueteotl.hackgdl.ctf  
10.0.4.3 huehueteotl.hackgdl.ctf  
10.129.25.43  kobold.htb bin.kobold.htb mcp.kobold.htb

### Writeup Hack The Box: Kobold

**Fase de Reconocimiento**

- Se ejecutó un escaneo de puertos que reveló los servicios SSH (22), HTTP (80), HTTPS (443) y un servicio interno en el puerto 3552.
    
- A través de la enumeración de subdominios, se identificaron dos objetivos principales: `mcp.kobold.htb` y `bin.kobold.htb`.
    

**Acceso Inicial**

- Se identificó que `mcp.kobold.htb` ejecutaba MCPJam, un software vulnerable a Ejecución Remota de Comandos (CVE-2026-23744).
    
- La explotación inicial falló debido a un firewall de salida (egress filtering) que bloqueaba conexiones TCP en puertos comunes de reverse shell como el 4444 o el 9999.
    
- Se comprobó la conectividad externa obligando al servidor a realizar una petición HTTP GET al puerto 80 de la máquina atacante.
    
- Para evadir las restricciones de variables de entorno y el firewall, se inyectó un payload utilizando rutas absolutas que devolvió una reverse shell interactiva a través del puerto 80, logrando acceso como el usuario `ben`.
    

**Movimiento Lateral y Extracción de Credenciales**

- El segundo subdominio, `bin.kobold.htb`, alojaba una instancia de PrivateBin vulnerable a Inclusión de Archivos Locales o LFI (CVE-2025-64714).
    
- Desde la shell del usuario `ben`, se escribió un archivo PHP para ejecución de comandos dentro del directorio de datos de PrivateBin (`/privatebin-data/data/shell.php`).
    
- Explotando el LFI mediante la manipulación de la cookie `template`, se logró leer el archivo de configuración del sistema en `/srv/cfg/conf.php`.
    
- El archivo expuso credenciales en texto plano, revelando la contraseña `ComplexP@sswordAdmin1928`.
    

**Escalada de Privilegios (Root)**

- Se verificó que el puerto 3552 alojaba una interfaz de gestión de contenedores llamada Arcane, la cual estaba bloqueada para conexiones externas.
    
- Se estableció un túnel SSH autenticándose como `ben` para redirigir el tráfico del puerto 3552 local hacia la máquina atacante.
    
- Se accedió al panel web de Arcane a través de `127.0.0.1:3552` utilizando las credenciales recuperadas en el paso anterior.
    
- Se realizó un ataque de escape de contenedor (Docker Breakout) desplegando un nuevo contenedor basado en la imagen residente `privatebin/nginx-fpm-alpine:2.0.2`.
    
- La configuración crítica del ataque consistió en asignar el usuario de ejecución como `root` (UID 0) y establecer un montaje de volumen (bind mount) que enlazaba el directorio raíz absoluto del host (`/`) hacia un directorio interno del contenedor (`/hostfs`).
    
- Tras iniciar el contenedor y acceder a su terminal interactiva, se extrajo el flag del administrador leyendo directamente la ruta montada en `/hostfs/root/root.txt`.