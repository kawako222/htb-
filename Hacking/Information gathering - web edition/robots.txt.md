El archivo `robots.txt` actúa como una "guía de etiqueta" virtual para los bots. Es un archivo de texto simple ubicado en el directorio raíz de un sitio web (ej. `www.dominio.com/robots.txt`) que indica a los rastreadores qué áreas pueden visitar y cuáles están fuera de sus límites.

---

#### **Estructura y Componentes**

El archivo se organiza en bloques de instrucciones llamados "registros", separados por una línea en blanco. Cada registro tiene dos partes:

1. **User-agent:** Especifica a qué bot se aplican las reglas.
    
    - `User-agent: *` (Afecta a todos los bots).
        
    - `User-agent: Googlebot` (Afecta solo al rastreador de Google).
        
2. **Directivas:** Las instrucciones específicas de acceso.
    

---

#### **Directivas Comunes**

|**Directiva**|**Descripción**|**Ejemplo**|
|---|---|---|
|**Disallow**|Rutas o patrones que el bot **no** debe rastrear.|`Disallow: /admin/`|
|**Allow**|Permite el acceso a rutas específicas, incluso dentro de un `Disallow`.|`Allow: /public/`|
|**Crawl-delay**|Segundos de espera entre peticiones para no saturar el servidor.|`Crawl-delay: 10`|
|**Sitemap**|Indica la ubicación del mapa del sitio en formato XML.|`Sitemap: https://.../sitemap.xml`|

---

#### **⚠️ Importancia en Reconocimiento (Pentesting)**

Para un atacante, el `robots.txt` es una **lista de rutas interesantes**. Si un administrador prohíbe a los bots entrar en `/backup/`, `/dev/` o `/config/`, está confirmando que esos directorios existen y contienen información que prefiere mantener oculta, convirtiéndolos en objetivos inmediatos para la inspección manual.

---
### 🛡️ ¿Por qué respetar el `robots.txt`?

Aunque el archivo no es un mecanismo de seguridad técnico (un bot malicioso puede ignorarlo), los rastreadores legítimos lo respetan por:

- **Estabilidad del Servidor:** Evita que el tráfico masivo de bots sature o tire el servidor.
    
- **Privacidad:** Impide que motores de búsqueda (Google, Bing) indexen información que el dueño prefiere mantener privada.
    
- **Cumplimiento Legal/Ético:** Ignorarlo puede violar los términos de servicio del sitio o derivar en problemas legales si se accede a datos protegidos.
    

---

### 🔍 El `robots.txt` en el Reconocimiento Web (Pentesting)

Para un profesional de seguridad, este archivo es una fuente de inteligencia pasiva. Al analizarlo, se obtienen pistas clave sin siquiera tocar el servidor:

- **Directorios Ocultos:** Las rutas en `Disallow` suelen ser carpetas que el dueño considera "sensibles". Pueden contener paneles de administración, archivos de respaldo o bases de datos.
    
- **Mapeo de Estructura:** Permite identificar secciones del sitio que no están en el menú principal o la navegación pública.
    
- **Detección de "Trampas" (Honeypots):** Algunos sitios ponen directorios falsos en `robots.txt` para identificar y bloquear bots que intentan acceder a ellos.
    

---

### 📊 Ejemplo de Análisis

Plaintext

```
User-agent: *
Disallow: /admin/
Disallow: /private/
Allow: /public/

User-agent: Googlebot
Crawl-delay: 10

Sitemap: https://www.example.com/sitemap.xml
```

**Deducciones técnicas:**

1. **Objetivos Críticos:** Existen directorios `/admin/` y `/private/`. Son los primeros puntos a investigar manualmente.
    
2. **Configuración Específica:** El administrador tiene especial cuidado con Google (Googlebot), pidiéndole que espere 10 segundos entre cada petición (`Crawl-delay`). Esto sugiere que el servidor podría ser sensible a la carga de tráfico.
    
3. **Mapa Completo:** El `Sitemap` nos da la URL exacta de un archivo XML que contiene todas las páginas legítimas del sitio, lo cual ahorra tiempo de rastreo.

[[web pentesting]]
