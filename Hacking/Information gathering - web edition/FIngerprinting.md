El **Fingerprinting** es lo que te permite dejar de disparar a ciegas y empezar a usar exploits específicos para la versión de software que tiene la víctima.

Aquí tienes el resumen estructurado con los enlaces para que vayas creando tus notas de herramientas:

---

### 🕵️ Web Fingerprinting: El ADN Digital
El **Fingerprinting** consiste en extraer detalles técnicos de las tecnologías que impulsan un sitio web. Al igual que una huella dactilar humana, las firmas digitales de servidores, sistemas operativos y componentes de software revelan la infraestructura del objetivo y sus debilidad
#### **Importancia en el Reconocimiento**

- **Ataques Dirigidos:** Permite centrar esfuerzos en exploits específicos para las tecnologías identificadas, aumentando la probabilidad de éxito.
    
- **Identificación de Malas Configuraciones:** Expone software desactualizado, configuraciones por defecto y debilidades que otros métodos no detectan.
    
- **Priorización de Objetivos:** Ayuda a decidir qué sistemas atacar primero basándose en su vulnerabilidad o en el valor de la información que contienen.
    
- **Perfil Integral:** La combinación de estos datos crea una visión holística de la infraestructura y sus posibles vectores de ataque.

---

### 🚀 Técnicas Manuales (Banner Grabbing)  [[curl]]

La forma más discreta de obtener información es analizando los encabezados HTTP con `curl`.

Nuestro primer paso es recopilar información directamente del propio servidor web. Podemos hacer esto usando el `curl` comando con el `-I` bandera (o `--head`) para recuperar solo los encabezados HTTP, no todo el contenido de la página.

**Comando:**

```bash
curl -I https://www.inlanefreight.com

```

**Qué buscar en la respuesta:**

* **Server:** (Ej: `Apache/2.4.41`) -> Te da la versión exacta.
* **X-Powered-By / X-Redirect-By:** Revela lenguajes o CMS (Ej: `WordPress`).
* **Rutas comunes:** `/wp-json/` o `/wp-login.php` confirman la tecnología base.

---

### 🛡️ Detección de [[Wafw00f]])

Los **Web Application Firewalls (WAFs)** son soluciones de seguridad diseñadas para proteger las aplicaciones web de diversos ataques.

Es fundamental determinar si el objetivo emplea un WAF antes de continuar con la identificación de tecnologías, debido a que este componente puede:

- **Interferir con las sondas:** Alterar los resultados de los escaneos técnicos.
    
- **Bloquear solicitudes:** Detectar y restringir potencialmente nuestras peticiones de reconocimiento.
Antes de escanear agresivamente, debes saber si hay un firewall protegiendo el sitio.

**Comando:**

```bash
wafw00f inlanefreight.com

```

*Si el resultado dice `Wordfence (Defiant)`, sabes que debes ser más cuidadoso o tus peticiones serán bloqueadas.*
```
❯ wafw00f inlanefreight.com  
  
               ______  
              /      \  
             (  W00f! )  
              \  ____/  
              ,,    __            404 Hack Not Found  
          |`-.__   / /                      __     __  
          /"  _/  /_/                       \ \   / /  
         *===*    /                          \ \_/ /  405 Not Allowed  
        /     )__//                           \   /  
   /|  /     /---`                        403 Forbidden  
   \\/`   \ |                                 / _ \  
   `\    /_\\_              502 Bad Gateway  / / \ \  500 Internal Error  
     `_____``-`                             /_/   \_\\  
  
                       ~ WAFW00F : v2.3.2 ~  
       The Web Application Firewall Fingerprinting Toolkit  
      
[*] Checking https://inlanefreight.com  
[+] The site https://inlanefreight.com is behind Wordfence (Defiant) WAF.  
[~] Number of requests: 2'

---
```
### 🧪 Escaneo con [[Nikto]](Software ID)

Para identificar software específico y configuraciones inseguras sin hacer un escaneo completo de vulnerabilidades.

**Comando:**
```
```shell-session
fluttershy222@htb[/htb]$ nikto -h inlanefreight.com -Tuning b

- Nikto v2.5.0
---------------------------------------------------------------------------
+ Multiple IPs found: 134.209.24.248, 2a03:b0c0:1:e0::32c:b001
+ Target IP:          134.209.24.248
+ Target Hostname:    www.inlanefreight.com
+ Target Port:        443
---------------------------------------------------------------------------
+ SSL Info:        Subject:  /CN=inlanefreight.com
                   Altnames: inlanefreight.com, www.inlanefreight.com
                   Ciphers:  TLS_AES_256_GCM_SHA384
                   Issuer:   /C=US/O=Let's Encrypt/CN=R3
+ Start Time:         2024-05-31 13:35:54 (GMT0)
---------------------------------------------------------------------------
+ Server: Apache/2.4.41 (Ubuntu)
+ /: Link header found with value: ARRAY(0x558e78790248). See: https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Link
+ /: The site uses TLS and the Strict-Transport-Security HTTP header is not defined. See: https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Strict-Transport-Security
+ /: The X-Content-Type-Options header is not set. This could allow the user agent to render the content of the site in a different fashion to the MIME type. See: https://www.netsparker.com/web-vulnerability-scanner/vulnerabilities/missing-content-type-header/
+ /index.php?: Uncommon header 'x-redirect-by' found, with contents: WordPress.
+ No CGI Directories found (use '-C all' to force check all possible dirs)
+ /: The Content-Encoding header is set to "deflate" which may mean that the server is vulnerable to the BREACH attack. See: http://breachattack.com/
+ Apache/2.4.41 appears to be outdated (current is at least 2.4.59). Apache 2.2.34 is the EOL for the 2.x branch.
+ /: Web Server returns a valid response with junk HTTP methods which may cause false positives.
+ /license.txt: License file found may identify site software.
+ /: A Wordpress installation was found.
+ /wp-login.php?action=register: Cookie wordpress_test_cookie created without the httponly flag. See: https://developer.mozilla.org/en-US/docs/Web/HTTP/Cookies
+ /wp-login.php:X-Frame-Options header is deprecated and has been replaced with the Content-Security-Policy HTTP header with the frame-ancestors directive instead. See: https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/X-Frame-Options
+ /wp-login.php: Wordpress login found.
+ 1316 requests: 0 error(s) and 12 item(s) reported on remote host
+ End Time:           2024-05-31 13:47:27 (GMT0) (693 seconds)
---------------------------------------------------------------------------
+ 1 host(s) tested
``` 


El escaneo de reconocimiento en `inlanefreight.com` revela varios hallazgos clave:

- `IPs`: El sitio web se resuelve en ambos IPv4 (`134.209.24.248`) y IPv6 (`2a03:b0c0:1:e0::32c:b001`) direcciones.
- `Server Technology`: El sitio web sigue funcionando `Apache/2.4.41 (Ubuntu)`
- `WordPress Presence`: El escaneo identificó una instalación de WordPress, incluida la página de inicio de sesión (`/wp-login.php`). Esto sugiere que el sitio podría ser un objetivo potencial para exploits comunes relacionados con WordPress.
- `Information Disclosure`: La presencia de un `license.txt` El archivo podría revelar detalles adicionales sobre los componentes de software del sitio web.
- `Headers`: Se encontraron varios encabezados no estándar o inseguros, incluido uno faltante `Strict-Transport-Security` encabezado y un potencialmente inseguro `x-redirect-by` cabecera.

### Preguntas

*Determine la versión de Apache que se ejecuta en app.inlanefreight.local en el sistema de destino. (Formato: 0.0.0)*

curl -I -H "Host: app.inlanefreight.local" http://10.129.42.195  
  

```
HTTP/1.1 200 OK  
Date: Mon, 09 Feb 2026 21:46:33 GMT  
Server: Apache/2.4.41 (Ubuntu)  
Set-Cookie: 72af8f2b24261272e581a49f5c56de40=rum3188tk12vof8vjbm878uudg; path=/; HttpOnly  
Permissions-Policy: interest-cohort=()  
Expires: Wed, 17 Aug 2005 00:00:00 GMT  
Last-Modified: Mon, 09 Feb 2026 21:46:34 GMT  
Cache-Control: no-store, no-cache, must-revalidate, post-check=0, pre-check=0  
Pragma: no-cache  
Content-Type: text/html; charset=utf-8
```

*+¿Qué CMS se utiliza en app.inlanefreight.local en el sistema de destino? Responda únicamente con el nombre, por ejemplo, WordPress.*

```
axmi222 …/htb   main ?   v8.4.16   15:51     
❯ whatweb http://10.129.42.195 -H "Host: app.inlanefreight.local"  
http://10.129.42.195 [200 OK] Apache[2.4.41], Bootstrap, Cookies[72af8f2b24261272e581a49f5c56de40], Country[RESERVED  
][ZZ], HTML5, HTTPServer[Ubuntu Linux][Apache/2.4.41 (Ubuntu)], HttpOnly[72af8f2b24261272e581a49f5c56de40], IP[10.12  
9.42.195], JQuery, MetaGenerator[Joomla! - Open Source Content Management], OpenSearch[http://app.inlanefreight.loca  
l/index.php/component/search/?layout=blog&amp;id=9&amp;Itemid=101&amp;format=opensearch], Script, Title[Home], Uncom  
monHeaders[permissions-policy]
```

*¿En qué sistema operativo se ejecuta el servidor web dev.inlanefreight.local en el sistema de destino? Responda sólo con el nombre, por ejemplo, Debian.*

```
axmi222 …/htb   main ?   v8.4.16   15:46     
❯ curl -I -H "Host: dev.inlanefreight.local" http://10.129.42.195  
HTTP/1.1 200 OK  
Date: Mon, 09 Feb 2026 21:46:47 GMT  
Server: Apache/2.4.41 (Ubuntu)  
Set-Cookie: 02a93f6429c54209e06c64b77be2180d=0cq1k61ahh608sc5fpn5etpqn4; path=/; HttpOnly  
Expires: Wed, 17 Aug 2005 00:00:00 GMT  
Last-Modified: Mon, 09 Feb 2026 21:46:47 GMT  
Cache-Control: no-store, no-cache, must-revalidate, post-check=0, pre-check=0  
Pragma: no-cache  
Content-Type: text/html; charset=utf-8
```


[[web pentesting]]