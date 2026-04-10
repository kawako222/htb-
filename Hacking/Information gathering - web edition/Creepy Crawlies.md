### 🕷️ Herramientas de Rastreo (Crawlers)

El rastreo web puede ser una tarea vasta e intrincada, pero existen herramientas diseñadas para automatizar este proceso. Estas herramientas permiten mapear sitios de manera rápida y eficiente para que el analista pueda concentrarse en los datos extraídos.

#### **Rastreadores Web Populares**

|**Herramienta**|**Tipo**|**Fortaleza Principal**|
|---|---|---|
|**Burp Suite Spider**|Profesional / Pago|Excelente para mapear aplicaciones web complejas e identificar contenido oculto y vulnerabilidades.|
|**OWASP ZAP**|Gratuito / Open Source|Incluye una "araña" (spider) tanto automática como manual para descubrir la estructura del sitio.|
|**Scrapy**|Framework (Python)|Versátil y escalable. Ideal para construir rastreadores personalizados que extraen datos estructurados específicos.|
|**Apache Nutch**|Escalable (Java)|Diseñado para rastreos masivos a gran escala (toda la web o dominios inmensos). Requiere alta experiencia técnica.|

---

### ⚖️ Ética y Responsabilidad en el Rastreo

Sin importar la herramienta que utilices, es fundamental seguir prácticas de reconocimiento responsables:

1. **Obtener Permiso:** Siempre asegúrate de tener autorización antes de realizar escaneos extensos o intrusivos.
    
2. **Cuidar los Recursos:** No sobrecargues el servidor del objetivo con demasiadas solicitudes (ajusta el _rate limit_).
    
3. **Respetar los Límites:** Revisa el archivo `robots.txt` para entender qué áreas prefiere el dueño que no sean indexadas.
    
---
### 🕷️ Scrapy y ReconSpider

Scrapy es un framework de Python potente y flexible diseñado para el rastreo web. En este módulo, se utiliza una araña personalizada llamada **ReconSpider** para automatizar la recolección de inteligencia sobre un dominio objetivo.
[[scrapy]]

```shell-session
fluttershy222@htb[/htb]$ pip3 install scrapy
```

Este comando descargará e instalará Scrapy junto con sus dependencias, preparando su entorno para construir nuestra araña.
### ReconSpider

Primero, ejecute este comando en su terminal para descargar la araña scrapy personalizada `ReconSpider`, y extraerlo al directorio de trabajo actual.

```shell-session
fluttershy222@htb[/htb]$ wget -O ReconSpider.zip https://academy.hackthebox.com/storage/modules/144/ReconSpider.v1.2.zip
fluttershy222@htb[/htb]$ unzip ReconSpider.zip 
```

Con los archivos extraídos, puedes ejecutar `ReconSpider.py` usando el siguiente comando:
[[ReconSpider.py]]


```shell-session
fluttershy222@htb[/htb]$ python3 ReconSpider.py http://inlanefreight.com
```

Reemplazar `inlanefreight.com` con el dominio que quieres explorar. La araña rastreará el objetivo y recopilará información valiosa.

### resultados.json

Después de correr `ReconSpider.py`, los datos se guardarán en un archivo JSON, `results.json`. Este archivo se puede explorar utilizando cualquier editor de texto. A continuación se muestra la estructura del archivo JSON producido:

Cod: json

```json
{
    "emails": [
        "lily.floid@inlanefreight.com",
        "cvs@inlanefreight.com",
        ...
    ],
    "links": [
        "https://www.themeansar.com",
        "https://www.inlanefreight.com/index.php/offices/",
        ...
    ],
    "external_files": [
        "https://www.inlanefreight.com/wp-content/uploads/2020/09/goals.pdf",
        ...
    ],
    "js_files": [
        "https://www.inlanefreight.com/wp-includes/js/jquery/jquery-migrate.min.js?ver=3.3.2",
        ...
    ],
    "form_fields": [],
    "images": [
        "https://www.inlanefreight.com/wp-content/uploads/2021/03/AboutUs_01-1024x810.png",
        ...
    ],
    "videos": [],
    "audio": [],
    "comments": [
        "<!-- #masthead -->",
        ...
    ]
}
```

Cada clave en el archivo JSON representa un tipo diferente de datos extraídos del sitio web de destino:

|Clave JSON|Descripción|
|---|---|
|`emails`|Enumera las direcciones de correo electrónico que se encuentran en el dominio.|
|`links`|Enumera las URL de los enlaces que se encuentran dentro del dominio.|
|`external_files`|Enumera las URL de archivos externos, como archivos PDF.|
|`js_files`|Enumera las URL de los archivos JavaScript utilizados por el sitio web.|
|`form_fields`|Las listas forman campos que se encuentran en el dominio (vacío en este ejemplo).|
|`images`|Enumera las URL de las imágenes encontradas en el dominio.|
|`videos`|Enumera las URL de los vídeos que se encuentran en el dominio (vacías en este ejemplo).|
|`audio`|Enumera las URL de los archivos de audio que se encuentran en el dominio (vacío en este ejemplo).|
|`comments`|Enumera los comentarios HTML que se encuentran en el código fuente.|

Al explorar esta estructura JSON, puede obtener información valiosa sobre la arquitectura, el contenido y los posibles puntos de interés de la aplicación web para una mayor investigación.

[[web pentesting]]

### Preguntas

 After spidering inlanefreight.com, identify the location where future reports will be stored. Respond with the full domain, e.g., files.inlanefreight.com.
 
axmi222 …/htb   main ?   v8.4.16   17:31     
❯ python3 ReconSpider.py http://inlanefreight.com  
2026-02-10 17:31:40 [scrapy.utils.log] INFO: Scrapy 2.14.1 started (bot: scrapybot)  
2026-02-10 17:31:40 [scrapy.utils.log] INFO: Versions:  
{'lxml': '6.0.2',  
'libxml2': '2.15.1',  
'cssselect': '1.4.0',  
'parsel': '1.11.0',  
'w3lib': '2.4.0',  
'Twisted': '25.5.0',  
'Python': '3.13.11 (main, Dec  8 2025, 11:43:54) [GCC 15.2.0]',  
'pyOpenSSL': '25.3.0 (OpenSSL 3.5.4 30 Sep 2025)',  
'cryptography': '46.0.1',  
'Platform': 'Linux-6.16.8+kali-amd64-x86_64-with-glibc2.42'}  
2026-02-10 17:31:40 [scrapy.addons] INFO: Enabled addons:  
[]  
2026-02-10 17:31:40 [scrapy.extensions.telnet] INFO: Telnet Password: 64080abfff30f1dd  
2026-02-10 17:31:40 [scrapy.middleware] INFO: Enabled extensions:  
['scrapy.extensions.corestats.CoreStats',  
'scrapy.extensions.logcount.LogCount',  
'scrapy.extensions.telnet.TelnetConsole',  
'scrapy.extensions.memusage.MemoryUsage',  
'scrapy.extensions.logstats.LogStats']  
2026-02-10 17:31:40 [scrapy.crawler] INFO: Overridden settings:  
{'LOG_LEVEL': 'INFO'}  
2026-02-10 17:31:40 [py.warnings] WARNING: /usr/lib/python3/dist-packages/scrapy/downloadermiddlewares/httpcompressi  
on.py:45: UserWarning: You have brotli installed. But 'br' encoding support now requires brotli's or brotlicffi's ve  
rsion >= 1.2.0. Please upgrade brotli/brotlicffi to make Scrapy decode 'br' encoded responses.  
 warnings.warn(  
  
2026-02-10 17:31:40 [scrapy.middleware] INFO: Enabled downloader middlewares:  
['scrapy.downloadermiddlewares.offsite.OffsiteMiddleware',  
'scrapy.downloadermiddlewares.httpauth.HttpAuthMiddleware',  
'scrapy.downloadermiddlewares.downloadtimeout.DownloadTimeoutMiddleware',  
'scrapy.downloadermiddlewares.defaultheaders.DefaultHeadersMiddleware',  
'scrapy.downloadermiddlewares.useragent.UserAgentMiddleware',  
'__main__.CustomOffsiteMiddleware',  
'scrapy.downloadermiddlewares.retry.RetryMiddleware',  
'scrapy.downloadermiddlewares.redirect.MetaRefreshMiddleware',  
'scrapy.downloadermiddlewares.httpcompression.HttpCompressionMiddleware',  
'scrapy.downloadermiddlewares.redirect.RedirectMiddleware',  
'scrapy.downloadermiddlewares.cookies.CookiesMiddleware',  
'scrapy.downloadermiddlewares.httpproxy.HttpProxyMiddleware',  
'scrapy.downloadermiddlewares.stats.DownloaderStats']  
2026-02-10 17:31:40 [scrapy.middleware] INFO: Enabled spider middlewares:  
['scrapy.spidermiddlewares.start.StartSpiderMiddleware',  
'scrapy.spidermiddlewares.httperror.HttpErrorMiddleware',  
'scrapy.spidermiddlewares.referer.RefererMiddleware',  
'scrapy.spidermiddlewares.urllength.UrlLengthMiddleware',  
'scrapy.spidermiddlewares.depth.DepthMiddleware']  
2026-02-10 17:31:40 [scrapy.middleware] INFO: Enabled item pipelines:  
[]  
2026-02-10 17:31:40 [scrapy.core.engine] INFO: Spider opened  
2026-02-10 17:31:40 [scrapy.extensions.logstats] INFO: Crawled 0 pages (at 0 pages/min), scraped 0 items (at 0 items  
/min)  
2026-02-10 17:31:40 [scrapy.extensions.telnet] INFO: Telnet console listening on 127.0.0.1:6023  
2026-02-10 17:31:48 [scrapy.core.engine] INFO: Closing spider (finished)  
2026-02-10 17:31:48 [scrapy.statscollectors] INFO: Dumping Scrapy stats:  
{'downloader/request_bytes': 2697,  
'downloader/request_count': 10,  
'downloader/request_method_count/GET': 10,  
'downloader/response_bytes': 93960,  
'downloader/response_count': 10,  
'downloader/response_status_count/200': 8,  
'downloader/response_status_count/301': 2,  
'dupefilter/filtered': 55,  
'elapsed_time_seconds': 7.375901,  
'finish_reason': 'finished',  
'finish_time': datetime.datetime(2026, 2, 10, 23, 31, 48, 1214, tzinfo=datetime.timezone.utc),  
'httpcompression/response_bytes': 162654,  
'httpcompression/response_count': 7,  
'items_per_minute': 0.0,  
'log_count/INFO': 3,  
'memusage/max': 68300800,  
'memusage/startup': 68300800,  
'request_depth_max': 2,  
'response_received_count': 8,  
'responses_per_minute': 68.57142857142857,  
'scheduler/dequeued': 10,  
'scheduler/dequeued/memory': 10,  
'scheduler/enqueued': 10,  
'scheduler/enqueued/memory': 10,  
'start_time': datetime.datetime(2026, 2, 10, 23, 31, 40, 625313, tzinfo=datetime.timezone.utc)}  
2026-02-10 17:31:48 [scrapy.core.engine] INFO: Spider closed (finished)  
                                                                                                                      
  
axmi222 …/htb   main ?   v8.4.16   17:31     
❯ ls  
cap               footprinting_easy_lab  image.php                                           prueba.txt  
conversorMachine  fries                  instantclient-basic-linux.x64-21.4.0.0.0dbru.zip    ReconSpider.py  
ctfs              hard_lab_footprinting  instantclient-sqlplus-linux.x64-21.4.0.0.0dbru.zip  results.json  
expressway        hashes.txt             ipmi                                                soulmate  
facts             htb.ctb                medium_lab_footprinting  
                                                                                                                      
  
axmi222 …/htb   main ?   v8.4.16   17:33     
❯ cat results.json  
{  
   "emails": [  
       "lily.floid@inlanefreight.com",  
       "enterprise-support@inlanefreight.com",  
       "support@inlanefreight.com",  
       "enterprise@inlanefreight.com",  
       "cvs@inlanefreight.com",  
       "david.jones@inlanefreight.com",  
       "freya.kartboom@inlanefreight.com",  
       "emma.williams@inlanefreight.com",  
       "jeremy-ceo@inlanefreight.com",  
       "hans.mueller@inlanefreight.com",  
       "samuel.dot@inlanefreight.com",  
       "manuel.pernilious@inlanefreight.com",  
       "info@themeansar.com",  
       "john.smith4@inlanefreight.com",  
       "info@inlanefreight.com",  
       "fiona.dante@inlanefreight.com"  
   ],  
   "links": [  
       "https://www.inlanefreight.com/index.php/career/",  
       "https://www.inlanefreight.com/index.php/news/#content",  
       "https://www.inlanefreight.com/index.php/contact/#content",  
       "https://www.inlanefreight.com/index.php/about-us/",  
       "https://www.inlanefreight.com/#content",  
       "https://www.inlanefreight.com/index.php/contact/",  
       "https://www.inlanefreight.com/index.php/about-us/#content",  
       "https://www.inlanefreight.com/",  
       "https://www.inlanefreight.com/index.php/career/#content",  
       "https://www.inlanefreight.com/wp-content/uploads/2020/09/goals.pdf",  
       "https://www.inlanefreight.com/index.php/offices/#content",  
       "https://www.inlanefreight.com",  
       "https://www.inlanefreight.com/index.php/offices/",  
       "https://www.inlanefreight.com/index.php/news/",  
       "https://www.themeansar.com"  
   ],  
   "external_files": [  
       "https://www.inlanefreight.com/wp-content/uploads/2020/09/goals.pdf",  
       "https://www.inlanefreight.com/index.php/news/pdf"  
   ],  
   "js_files": [  
       "https://www.inlanefreight.com/wp-includes/js/jquery/jquery-migrate.min.js?ver=3.3.2",  
       "https://www.inlanefreight.com/wp-content/themes/ben_theme/js/bootstrap.min.js?ver=5.6.16",  
       "https://www.inlanefreight.com/wp-content/themes/ben_theme/js/jquery.smartmenus.js?ver=5.6.16",  
       "https://www.inlanefreight.com/wp-content/themes/ben_theme/js/navigation.js?ver=5.6.16",  
       "https://www.inlanefreight.com/wp-content/themes/ben_theme/js/jquery.smartmenus.bootstrap.js?ver=5.6.16",  
       "https://www.inlanefreight.com/wp-includes/js/wp-embed.min.js?ver=5.6.16",  
       "https://www.inlanefreight.com/wp-includes/js/jquery/jquery.min.js?ver=3.5.1",  
       "https://www.inlanefreight.com/wp-content/themes/ben_theme/js/owl.carousel.min.js?ver=5.6.16"  
   ],  
   "form_fields": [],  
   "images": [  
       "https://www.inlanefreight.com/wp-content/uploads/2021/03/AboutUs_03-1024x810.png",  
       "https://www.inlanefreight.com/wp-content/uploads/2021/03/AboutUs_01-1024x810.png",  
       "https://www.inlanefreight.com/wp-content/uploads/2021/03/AboutUs_02-1024x810.png",  
       "https://www.inlanefreight.com/wp-content/uploads/2021/03/Career_01-300x235.jpg",  
       "https://www.inlanefreight.com/wp-content/uploads/2021/03/Career_02-300x235.jpg",  
       "https://www.inlanefreight.com/wp-content/uploads/2021/03/Offices_01-1024x359.png",  
       "https://www.inlanefreight.com/wp-content/uploads/2021/03/AboutUs_04-1024x810.png"  
   ],  
   "videos": [],  
   "audio": [],  
   "comments": [  
       "<!-- Logo -->",  
       "<!-- /Navigation -->",  
       "<!-- #masthead -->",  
       "<!-- /navbar-toggle -->",  
       "<!--\nSkip to content<div class=\"wrapper\">\n<header class=\"transportex-trhead\">\n\t<!--================  
==== Header ====================-->",  
       "<!-- Navigation -->",  
       "<!-- navbar-toggle -->",  
       "<!-- Blog Area -->",  
       "<!--Sidebar Area-->",  
       "<!--/overlay-->",  
       "<!-- Right nav -->",  
       "<!-- /Right nav -->",  
       "<!-- #secondary -->",  
       "<!-- change Jeremy's email to jeremy-ceo@inlanefreight.com -->",  
       "<!--==================== feature-product ====================-->",  
       "<!--==================== TOP BAR ====================-->",  
       "<!--==================== transportex-FOOTER AREA ====================-->",  
       "<!-- TO-DO: change the location of future reports to inlanefreight-comp133.s3.amazonaws.htb -->"  
   ]  
}