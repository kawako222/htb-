### 🔍 Descubrimiento de Motores de Búsqueda (OSINT)

El descubrimiento de motores de búsqueda, o **OSINT** (Inteligencia de Fuentes Abiertas), consiste en utilizar algoritmos de búsqueda para extraer datos que no son visibles directamente en la interfaz de un sitio web. Es una técnica poderosa para desenterrar información sobre organizaciones, empleados e infraestructura técnica.

#### **¿Por qué es fundamental?**

- **Fuentes Abiertas:** Es legal y ético, ya que solo se accede a información que ya es pública.
    
- **Amplitud de Datos:** Los motores de búsqueda indexan miles de millones de páginas, ofreciendo una base de datos global masiva.
    
- **Eficiencia:** No requiere habilidades técnicas complejas y es totalmente gratuito.
    

---

#### **Aplicaciones Prácticas**

|**Uso**|**Descripción**|
|---|---|
|**Evaluación de Seguridad**|Detectar datos expuestos, páginas de login ocultas y vectores de ataque.|
|**Inteligencia Competitiva**|Analizar productos, servicios y movimientos de la competencia.|
|**Periodismo de Investigación**|Revelar conexiones ocultas o prácticas poco éticas.|
|**Inteligencia de Amenazas**|Rastrear actores maliciosos y predecir posibles ataques.|

#### **¿Qué se puede encontrar?**

Mediante operadores especializados (Google Dorks), un investigador puede localizar:

- Información de contacto de empleados.
    
- Documentos confidenciales olvidados en el servidor.
    
- Credenciales expuestas en foros o repositorios.
    
- Subdominios de desarrollo o pruebas.
    

> **⚠️ Limitación:** No todo está en Google. Los motores de búsqueda no indexan la "Deep Web" ni bases de datos protegidas por contraseña o archivos `robots.txt` estrictos.

## Operadores de búsqueda

Los operadores de búsqueda son como los códigos secretos de los motores de búsqueda. Estos comandos y modificadores especiales desbloquean un nuevo nivel de precisión y control, permitiéndole identificar tipos específicos de información en medio de la inmensidad de la web indexada.

Si bien la sintaxis exacta puede variar ligeramente entre motores de búsqueda, los principios subyacentes siguen siendo consistentes. Profundicemos en algunos operadores de búsqueda esenciales y avanzados:

|Operador|Descripción del operador|Ejemplo|Descripción del ejemplo|
|:--|:--|:--|:--|
|`site:`|Limita los resultados a un sitio web o dominio específico.|`site:example.com`|Encuentre todas las páginas de acceso público en example.com.|
|`inurl:`|Encuentra páginas con un término específico en la URL.|`inurl:login`|Busque páginas de inicio de sesión en cualquier sitio web.|
|`filetype:`|Busca archivos de un tipo particular.|`filetype:pdf`|Encuentre documentos PDF descargables.|
|`intitle:`|Encuentra páginas con un término específico en el título.|`intitle:"confidential report"`|Busque documentos titulados "informe confidencial" o variaciones similares.|
|`intext:`o `inbody:`|Busca un término dentro del cuerpo del texto de las páginas.|`intext:"password reset"`|Identifique las páginas web que contienen el término “restablecimiento de contraseña”.|
|`cache:`|Muestra la versión en caché de una página web (si está disponible).|`cache:example.com`|Vea la versión en caché de example.com para ver su contenido anterior.|
|`link:`|Encuentra páginas que enlazan a una página web específica.|`link:example.com`|Identifique sitios web que enlazan a example.com.|
|`related:`|Encuentra sitios web relacionados con una página web específica.|`related:example.com`|Descubra sitios web similares a example.com.|
|`info:`|Proporciona un resumen de información sobre una página web.|`info:example.com`|Obtenga detalles básicos sobre example.com, como su título y descripción.|
|`define:`|Proporciona definiciones de una palabra o frase.|`define:phishing`|Obtenga una definición de "phishing" de varias fuentes.|
|`numrange:`|Busca números dentro de un rango específico.|`site:example.com numrange:1000-2000`|Encuentre páginas en example.com que contengan números entre 1000 y 2000.|
|`allintext:`|Encuentra páginas que contienen todas las palabras especificadas en el cuerpo del texto.|`allintext:admin password reset`|Busque páginas que contengan "administrador" y "restablecimiento de contraseña" en el cuerpo del texto.|
|`allinurl:`|Encuentra páginas que contienen todas las palabras especificadas en la URL.|`allinurl:admin panel`|Busque páginas con "admin" y "panel" en la URL.|
|`allintitle:`|Encuentra páginas que contienen todas las palabras especificadas en el título.|`allintitle:confidential report 2023`|Busque páginas con "confidencial", "informe" y "2023" en el título.|
|`AND`|Limita los resultados al exigir que todos los términos estén presentes.|`site:example.com AND (inurl:admin OR inurl:login)`|Encuentre páginas de administración o de inicio de sesión específicamente en example.com.|
|`OR`|Amplía los resultados al incluir páginas con cualquiera de los términos.|`"linux" OR "ubuntu" OR "debian"`|Busque páginas web que mencionen Linux, Ubuntu o Debian.|
|`NOT`|Excluye resultados que contienen el término especificado.|`site:bank.com NOT inurl:login`|Encuentre páginas en bank.com, excluidas las páginas de inicio de sesión.|
|`*`(comodín)|Representa cualquier carácter o palabra.|`site:socialnetwork.com filetype:pdf user* manual`|Busque manuales de usuario (guía de usuario, manual de usuario) en formato PDF en socialnetwork.com.|
|`..`(búsqueda de rango)|Encuentra resultados dentro de un rango numérico específico.|`site:ecommerce.com "price" 100..500`|Busque productos con precios entre 100 y 500 en un sitio web de comercio electrónico.|
|`" "`(comillas)|Busca frases exactas.|`"information security policy"`|Encuentre documentos que mencionen la frase exacta "política de seguridad de la información".|
|`-`(signo menos)|Excluye términos de los resultados de búsqueda.|`site:news.com -inurl:sports`|Busque artículos de noticias en news.com excluyendo contenido relacionado con deportes.|

### Google Dorking

Google Dorking, también conocido como Google Hacking, es una técnica que aprovecha el poder de los operadores de búsqueda para descubrir información confidencial, vulnerabilidades de seguridad o contenido oculto en sitios web mediante la Búsqueda de Google.

A continuación se muestran algunos ejemplos comunes de Google Dorks; para obtener más ejemplos, consulte [Base de datos de piratería de Google](https://www.exploit-db.com/google-hacking-database):

- Encontrar páginas de inicio de sesión:
    - `site:example.com inurl:login`
    - `site:example.com (inurl:login OR inurl:admin)`
- Identificación de archivos expuestos:
    - `site:example.com filetype:pdf`
    - `site:example.com (filetype:xls OR filetype:docx)`
- Descubriendo archivos de configuración:
    - `site:example.com inurl:config.php`
    - `site:example.com (ext:conf OR ext:cnf)`(busca extensiones comúnmente utilizadas para archivos de configuración)
- Localización de copias de seguridad de bases de datos:
    - `site:example.com inurl:backup`
    - `site:example.com filetype:sql`