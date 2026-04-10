Perfecto. Aquí tienes tu **apunte en formato Obsidian**, estructurado como **metodología paso a paso**, con `[[links]]` a herramientas y conceptos clave.

---

# 🕵️ Web Information Gathering – Metodología Paso a Paso

La enumeración web no es correr herramientas al azar.  
Es un **proceso estructurado** para descubrir:

- Superficie de ataque
    
- Servicios expuestos
    
- Subdominios
    
- Tecnologías
    
- Directorios ocultos
    
- Credenciales filtradas
    
- Artefactos sensibles
    

---

# 🧭 Fase 0 — Preparación

## 📌 1. Resolver dominio localmente

Editar:

```bash
/etc/hosts
```

Sirve para:

- Resolver dominios internos
    
- Probar vhosts en entornos de CTF / HTB
    

---

# 🌍 Fase 1 — Información de Dominio

## 🔎 [[whois]]

```bash
whois dominio.com
```

Sirve para:

- Ver registrador
    
- IANA ID
    
- Fechas de creación
    
- DNS autoritativos
    

---

## 🌐 [[dig]] / [[nslookup]]

```bash
dig dominio.com
```

Sirve para:

- Consultar registros DNS
    
- MX records
    
- TXT records
    
- Subdominios mal configurados
    

---

# 🛰️ Fase 2 — Descubrimiento de Subdominios

## 🧠 [[Subdomain Enumeration]]

### 🔹 [[gobuster]] (modo DNS)

```bash
gobuster dns -d dominio.com -w wordlist.txt
```

Sirve para:

- Fuerza bruta de subdominios
    

---

### 🔹 [[ffuf]]

```bash
ffuf -u http://FUZZ.dominio.com -w wordlist.txt -H "Host: FUZZ.dominio.com"
```

Sirve para:

- Descubrir subdominios
    
- Descubrir vhosts
    

---

### 🔹 [[amass]] (más avanzado)

Sirve para:

- Enumeración pasiva + activa
    
- OSINT
    
- Integración con múltiples fuentes
    

---

# 🖥️ Fase 3 — Identificación de Tecnologías

## 🔎 [[whatweb]]

```bash
whatweb http://dominio.com
```

Sirve para:

- Detectar CMS
    
- Frameworks
    
- Librerías
    
- Versiones expuestas
    

---

## 🌐 [[wappalyzer]]

Extensión del navegador.

Sirve para:

- Detectar stack tecnológico
    
- JS frameworks
    
- Analytics
    

---

## 📡 [[curl]]

```bash
curl -I http://dominio.com
```

Sirve para:

- Ver headers HTTP
    
- Detectar servidor (nginx, apache)
    
- Revisar cookies
    
- Ver redirecciones
    

---

# 📂 Fase 4 — Enumeración de Directorios

## 📁 [[gobuster]] (modo dir)

```bash
gobuster dir -u http://dominio.com -w wordlist.txt
```

Sirve para:

- Descubrir rutas ocultas
    
- Paneles admin
    
- APIs
    

---

## 🚀 [[dirsearch]]

Alternativa más agresiva.

Sirve para:

- Enumeración profunda de endpoints
    

---

## 🔥 [[ffuf]] (fuzzing)

```bash
ffuf -u http://dominio.com/FUZZ -w wordlist.txt
```

Sirve para:

- Fuzzing avanzado
    
- Filtrar por código de estado
    

---

# 🤖 Fase 5 — robots.txt & Archivos Públicos

## 📄 [[robots.txt]]

```bash
curl http://dominio.com/robots.txt
```

Sirve para:

- Encontrar rutas ocultas
    
- Directorios administrativos
    

---

## 📁 Archivos comunes

Buscar:

- `/sitemap.xml`
    
- `/backup.zip`
    
- `/config.php`
    
- `.git/`
    
- `.env`
    

---

# 🕷️ Fase 6 — Crawling

## 🧠 [[ReconSpider]]

```bash
python3 ReconSpider.py http://dominio.com
```

Sirve para:

- Extraer emails
    
- Encontrar comentarios ocultos
    
- Descubrir rutas internas
    

---

## 🕷️ [[Scrapy]]

Framework de crawling más avanzado.

Sirve para:

- Automatizar scraping
    
- Extraer datos estructurados
    

---

# 🔍 Fase 7 — Virtual Hosts

## 🌐 [[gobuster]] (vhost mode)

```bash
gobuster vhost -u http://dominio.com -w wordlist.txt --append-domain
```

Sirve para:

- Encontrar aplicaciones internas
    
- Ambientes dev/test
    

---

# 📡 Fase 8 — Escaneo de Puertos

## 🗺️ [[Nmap]]

```bash
nmap -sC -sV -p- dominio.com
```

Sirve para:

- Descubrir puertos abiertos
    
- Enumerar servicios
    
- Detectar versiones
    

---

# 🧠 Fase 9 — Análisis Manual

Aquí es donde muchos fallan.

Revisar:

- Código fuente HTML
    
- Comentarios
    
- JavaScript
    
- Endpoints ocultos
    
- Tokens expuestos
    
- API keys
    

Usar:

- DevTools (F12)
    
- Network tab
    
- Inspector
    

---

# 📦 Fase 10 — Artefactos Sensibles

Buscar:

- API Keys
    
- Emails internos
    
- Tokens JWT
    
- Credenciales hardcodeadas
    
- Rutas administrativas
    
- Entornos dev/staging
    

---

# 🧩 Checklist Rápido de Enumeración Web

-  Whois
    
-  DNS records
    
-  Subdomain brute force
    
-  Vhost fuzzing
    
-  Directory brute force
    
-  robots.txt
    
-  Sitemap
    
-  Crawl completo
    
-  Revisar JS
    
-  Analizar headers
    
-  Escanear puertos con Nmap
    
-  Buscar secretos expuestos
    

---

# 🧠 Regla de Oro

> Enumeración ≠ correr herramientas  
> Enumeración = entender el servicio + interpretar resultados

---

Si quieres, puedo ahora hacerte:

- 🔥 Una versión **ultra resumida tipo cheat sheet**
    
- 🧨 Una versión enfocada solo a **CTFs**
    
- 🏢 Una versión enfocada a **pentesting real / bug bounty**
    
- 📘 O dividirlo por **nivel básico → intermedio → avanzado**
    

Tú dime cómo quieres organizar tu vault en Obsidian.