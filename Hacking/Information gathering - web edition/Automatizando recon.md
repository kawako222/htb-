### ⚡ Automatización de Recon

El reconocimiento manual es valioso pero lento y propenso a errores. La **automatización** transforma este proceso al permitir recopilar información a escala, con mayor precisión y rapidez, liberando tiempo para el análisis crítico.

---

#### **Ventajas de Automatizar**

- **Eficiencia y Escalabilidad:** Realiza tareas repetitivas en segundos y permite atacar cientos de dominios simultáneamente.
    
- **Consistencia:** Las herramientas siguen reglas predefinidas, garantizando que no se pase por alto ningún paso y que los resultados sean reproducibles.
    
- **Cobertura Integral:** Un solo script puede orquestar enumeración de DNS, descubrimiento de subdominios, rastreo y escaneo de puertos.
    
- **Integración:** Los resultados pueden alimentar automáticamente otras etapas del pentesting (como la explotación).
    

---

#### **Marcos de Reconocimiento (Frameworks)**

Existen plataformas diseñadas para centralizar todas las herramientas de reconocimiento en un solo ecosistema:

|**Herramienta**|**Tipo**|**Especialidad**|
|---|---|---|
|**FinalRecon**|Modular (Python)|Verificación de SSL, Whois, análisis de encabezados y crawling.|
|**Recon-ng**|Framework completo|Interfaz similar a Metasploit. Realiza desde DNS hasta explotación de vulnerabilidades conocidas.|
|**theHarvester**|Recolector OSINT|Excelente para extraer correos, nombres de empleados y subdominios de fuentes públicas (Google, Shodan, PGP).|
|**SpiderFoot**|Automatización OSINT|Se integra con cientos de fuentes de datos para mapear IPs, dominios y redes sociales automáticamente.|
|**OSINT Framework**|Repositorio de recursos|No es una herramienta "per se", sino una guía web exhaustiva con todas las herramientas disponibles para cada tipo de dato.|

---

### 💡 Tip para tu Obsidian

Crea una nota llamada `[[Herramientas de Automatización]]` y organiza tus comandos favoritos. Por ejemplo, para **theHarvester**, que es un clásico en los exámenes de certificación:

Bash

```
# Ejemplo para buscar correos y subdominios en Google
theHarvester -d inlanefreight.com -l 500 -b google
```

###  final recon

`FinalRecon`ofrece una gran cantidad de información de reconocimiento:
[[FinalRecon]]
- `Header Information`: Revela detalles del servidor, tecnologías utilizadas y posibles configuraciones incorrectas de seguridad.
- `Whois Lookup`: Descubre detalles de registro de dominio, incluida información del registrante y datos de contacto.
- `SSL Certificate Information`: Examina el certificado SSL/TLS para determinar su validez, emisor y otros detalles relevantes.
- `Crawler`:
    - HTML, CSS, JavaScript: extrae enlaces, recursos y posibles vulnerabilidades de estos archivos.
    - Enlaces internos/externos: mapea la estructura del sitio web e identifica conexiones con otros dominios.
    - Imágenes, robots.txt, sitemap.xml: recopila información sobre rutas de rastreo permitidas/no permitidas y la estructura del sitio web.
    - Enlaces en JavaScript, Wayback Machine: descubre enlaces ocultos y datos históricos del sitio web.
- `DNS Enumeration`: Consulta más de 40 tipos de registros DNS, incluidos registros DMARC para la evaluación de la seguridad del correo electrónico.
- `Subdomain Enumeration`: Aprovecha múltiples fuentes de datos (crt.sh, AnubisDB, ThreatMiner, CertSpotter, API de Facebook, API de VirusTotal, API de Shodan, API de BeVigil) para descubrir subdominios.
- `Directory Enumeration`: Admite listas de palabras personalizadas y extensiones de archivos para descubrir directorios y archivos ocultos.
- `Wayback Machine`: Recupera URL de los últimos cinco años para analizar cambios en el sitio web y posibles vulnerabilidades.

La instalación es rápida y sencilla:

```shell-session
fluttershy222@htb[/htb]$ git clone https://github.com/thewhiteh4t/FinalRecon.git
fluttershy222@htb[/htb]$ cd FinalRecon
fluttershy222@htb[/htb]$ pip3 install -r requirements.txt
fluttershy222@htb[/htb]$ chmod +x ./finalrecon.py
fluttershy222@htb[/htb]$ ./finalrecon.py --help

usage: finalrecon.py [-h] [--url URL] [--headers] [--sslinfo] [--whois]
                     [--crawl] [--dns] [--sub] [--dir] [--wayback] [--ps]
                     [--full] [-nb] [-dt DT] [-pt PT] [-T T] [-w W] [-r] [-s]
                     [-sp SP] [-d D] [-e E] [-o O] [-cd CD] [-k K]

FinalRecon - All in One Web Recon | v1.1.6

optional arguments:
  -h, --help  show this help message and exit
  --url URL   Target URL
  --headers   Header Information
  --sslinfo   SSL Certificate Information
  --whois     Whois Lookup
  --crawl     Crawl Target
  --dns       DNS Enumeration
  --sub       Sub-Domain Enumeration
  --dir       Directory Search
  --wayback   Wayback URLs
  --ps        Fast Port Scan
  --full      Full Recon

Extra Options:
  -nb         Hide Banner
  -dt DT      Number of threads for directory enum [ Default : 30 ]
  -pt PT      Number of threads for port scan [ Default : 50 ]
  -T T        Request Timeout [ Default : 30.0 ]
  -w W        Path to Wordlist [ Default : wordlists/dirb_common.txt ]
  -r          Allow Redirect [ Default : False ]
  -s          Toggle SSL Verification [ Default : True ]
  -sp SP      Specify SSL Port [ Default : 443 ]
  -d D        Custom DNS Servers [ Default : 1.1.1.1 ]
  -e E        File Extensions [ Example : txt, xml, php ]
  -o O        Export Format [ Default : txt ]
  -cd CD      Change export directory [ Default : ~/.local/share/finalrecon ]
  -k K        Add API key [ Example : shodan@key ]
```

Para comenzar, primero clonarás el `FinalRecon` repositorio de GitHub usando `git clone https://github.com/thewhiteh4t/FinalRecon.git`. Esto creará un nuevo directorio llamado "FinalRecon" que contendrá todos los archivos necesarios.

A continuación, navegue hasta el directorio recién creado con `cd FinalRecon`. Una vez dentro, instalará las dependencias de Python requeridas usando `pip3 install -r requirements.txt`. Esto garantiza que `FinalRecon` tiene todas las bibliotecas y módulos que necesita para funcionar correctamente.

Para asegurarse de que el script principal sea ejecutable, deberá cambiar los permisos del archivo usando `chmod +x ./finalrecon.py`. Esto le permite ejecutar el script directamente desde su terminal.

Finalmente, puedes comprobarlo `FinalRecon` se instala correctamente y obtenga una descripción general de sus opciones disponibles ejecutando `./finalrecon.py --help`. Esto mostrará un mensaje de ayuda con detalles sobre cómo utilizar la herramienta, incluidos los distintos módulos y sus respectivas opciones:

| Opción         | Argumento | Descripción                                                     |
| -------------- | --------- | --------------------------------------------------------------- |
| `-h`, `--help` |           | Muestra el mensaje de ayuda y sal.                              |
| `--url`        | URL       | Especifique la URL de destino.                                  |
| `--headers`    |           | Recupere información del encabezado para la URL de destino.     |
| `--sslinfo`    |           | Obtenga información del certificado SSL para la URL de destino. |
| `--whois`      |           | Realice una búsqueda Whois del dominio de destino.              |
| `--crawl`      |           | Rastrear el sitio web de destino.                               |
| `--dns`        |           | Realice la enumeración de DNS en el dominio de destino.         |
| `--sub`        |           | Enumerar subdominios para el dominio de destino.                |
| `--dir`        |           | Busque directorios en el sitio web de destino.                  |
| `--wayback`    |           | Recupere URL de Wayback para el destino.                        |
| `--ps`         |           | Realice un escaneo rápido del puerto en el objetivo.            |
| `--full`       |           | Realice un escaneo de reconocimiento completo del objetivo.     |
