
# 🗺️ [[Nmap]] – Network Mapper

**[[Nmap]]** es una herramienta de **auditoría de seguridad y análisis de redes** de código abierto, escrita en **C, C++, Python y Lua**.  
Está diseñada para **escanear redes**, identificar **hosts activos**, **servicios**, **puertos**, **versiones**, **sistemas operativos** y evaluar la **postura de seguridad** de un objetivo.

Es una de las herramientas **fundamentales en enumeración** y el primer paso en casi cualquier **pentest o CTF**.

---

## 🎯 Funcionalidades principales

- Descubrir **hosts activos** en una red
    
- Identificar **puertos abiertos**
    
- Detectar **servicios y versiones**
    
- Identificar **sistemas operativos**
    
- Evaluar **firewalls**, **IDS** y filtros de paquetes
    
- Facilitar **enumeración avanzada**
    
- Apoyar **evaluación de vulnerabilidades**
    

---

## 🧑‍💻 Casos de uso

[[Nmap]] es ampliamente utilizado por:

- Administradores de red
    
- Pentesters
    
- Analistas de seguridad
    

Se usa para:

- Auditar la **seguridad de redes**
    
- Simular **pruebas de penetración**
    
- Verificar configuraciones de **firewall** e **IDS**
    
- Mapeo de redes
    
- Análisis de respuestas de servicios
    
- Identificación de superficies de ataque
    

---

## 🏗️ Arquitectura de Nmap

[[Nmap]] puede dividirse en las siguientes **fases / técnicas de escaneo**:

- [[Host Discovery]] (Descubrimiento de hosts)
    
- [[Port Scanning]] (Escaneo de puertos)
    
- [[Service Enumeration]] y detección de versiones
    
- [[OS Detection]] (Detección de sistema operativo)
    
- [[Nmap Scripting Engine]] (NSE) – interacción programable
    

---

## 🧾 Sintaxis básica

```bash
nmap <scan types> <options> <target>
```

Ejemplo:

```bash
nmap -sS -sV -p- 10.10.10.10
```

---

## 🧪 Técnicas de escaneo en Nmap

Para ver todas las técnicas disponibles:

```bash
nmap --help
```

### Principales técnicas:

- `-sS` → [[TCP SYN Scan]]
    
- `-sT` → TCP Connect Scan
    
- `-sA` → ACK Scan
    
- `-sW` → Window Scan
    
- `-sM` → Maimon Scan
    
- `-sU` → [[UDP Scan]]
    
- `-sN` → TCP Null Scan
    
- `-sF` → TCP FIN Scan
    
- `-sX` → TCP Xmas Scan
    
- `-sI` → [[Idle Scan]]
    
- `-sO` → IP Protocol Scan
    
- `-b` → FTP Bounce Scan
    
- `--scanflags` → Escaneo TCP personalizado
    

---

## 🔑 [[TCP SYN Scan]] (`-sS`)

Es uno de los **métodos más populares y rápidos**.  
Envía paquetes **SYN** sin completar el **three-way handshake**, lo que lo hace **más sigiloso**.

### Interpretación de respuestas:

- **SYN-ACK** → Puerto **open**
    
- **RST** → Puerto **closed**
    
- **Sin respuesta** → Puerto **filtered**
    

📌 El estado _filtered_ suele indicar:

- Firewall activo
    
- Paquetes descartados
    
- Reglas de filtrado
    

---

## 📌 Ejemplo práctico

```bash
sudo nmap -sS localhost
```

Salida:

```text
PORT     STATE SERVICE
22/tcp   open  ssh
80/tcp   open  http
5432/tcp open  postgresql
5901/tcp open  vnc-1
```

### Interpretación:

- **PORT** → Número de puerto
    
- **STATE** → Estado del puerto
    
- **SERVICE** → Servicio detectado
    

👉 Cada puerto abierto es un **posible vector de ataque**.

---

## 🧠 Notas clave

- [[Nmap]] no solo escanea, **enumera**
    
- La información útil viene de:
    
    - Servicios mal configurados
        
    - Versiones vulnerables
        
    - Respuestas inesperadas
        
- Saber **leer la salida** es más importante que correr flags
    
