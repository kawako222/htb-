El **Crawling** es el proceso automatizado y sistemático de navegar por la World Wide Web. Funciona mediante bots (rastreadores) que utilizan algoritmos para descubrir e indexar páginas, siguiendo enlaces de una página a otra como una araña en su red.

#### **Funcionamiento Básico**

1. **URL Inicial (Seed):** El rastreador comienza en una página web específica.
    
2. **Extracción:** Recupera la página, analiza el contenido y extrae todos los enlaces disponibles.
    
3. **Cola (Queue):** Agrega los nuevos enlaces a una lista de tareas pendientes.
    
4. **Iteración:** Repite el proceso sistemáticamente para explorar el sitio completo o una gran parte de la web.
    

#### **Ejemplo de Flujo**

- **Página de inicio:** Contiene `link1`, `link2` y `link3`.
    
- **Visita a link1:** Revela nuevos enlaces como `link4` y `link5`, además de volver a la página de inicio.
    
- **Continuación:** El bot sigue expandiendo el mapa del sitio visitando cada nuevo enlace descubierto.
- ---

![[Pasted image 20260209164523.png]]

El **Breadth-first crawling** prioriza explorar el ancho de un sitio web antes de profundizar en sus niveles.

#### **Metodología**

1. **Nivel 1:** Rastrea todos los enlaces directos de la página inicial (Home).
    
2. **Nivel 2:** Pasa a los enlaces encontrados en las páginas del Nivel 1.
    
3. **Nivel 3:** Continúa con los enlaces de las páginas del Nivel 2, y así sucesivamente.
    

#### **Utilidad**

Es la técnica ideal para obtener una **descripción general amplia** de la estructura y el contenido de un sitio web de manera organizada por niveles de profundidad.

---
### Arrastre en profundidad primero
![Diagrama de flujo que muestra una URL inicial que conduce a la página 1 y luego a la página 2. La página 2 se conecta a la página 3, que se ramifica a la página 4 y la página 5.](https://mermaid.ink/svg/pako:eNo9zz0PgjAQBuC_0twsg18LgwlfGyYG4uQ5VHoC0RZS2sEQ_rsnTezU98mlvXeGZlAEMbRWjp0oKzSTf4RQEylxrUo0gk9yu8iWxPaOhoxCk4goOok06I41XSELsGfIVsgDHBjyFYoAR4YivCEEGtiAJqtlr3iZ-fclgutIE0LMVyXtCwHNwnPSu6H-mAZiZz1twA6-7SB-yvfEyY9KOsp7ySX0X0n1brDn0HWtvHwB2SFOww)

El **Depth-first crawling** prioriza la profundidad sobre la amplitud. Sigue una única ruta de enlaces hasta llegar al final antes de retroceder para explorar caminos alternativos.

#### **Metodología**

1. **Exploración Vertical:** Sigue el primer enlace encontrado, luego el primer enlace de esa nueva página, y así sucesivamente hacia lo más profundo de la estructura.
    
2. **Retroceso (Backtracking):** Una vez que no encuentra más enlaces en esa rama, retrocede un nivel para seguir la siguiente ruta disponible.
    

#### **Utilidad**

Es útil para:

- Encontrar **contenido específico** oculto en niveles profundos.
    
- Analizar a fondo una sección o rama particular de la estructura de un sitio web.

---
### Extracción de Información Valiosa

El rastreo no solo mapea rutas, sino que extrae datos críticos que definen la superficie de ataque. Cada pieza de información cumple un propósito en el reconocimiento web.

#### **Datos Extraídos y su Utilidad**

- **Enlaces (Internos y Externos):** Permiten trazar la estructura del sitio, descubrir páginas ocultas e identificar conexiones con recursos externos.
    
- **Comentarios:** Los desarrolladores o usuarios suelen revelar inadvertidamente procesos internos, nombres de usuarios o pistas sobre vulnerabilidades.
    
- **Metadatos:** Incluyen títulos, descripciones, autores y fechas. Aportan contexto sobre el propósito de la página y la relevancia del contenido.
    
- **Archivos Sensibles:** Configuraciones de búsqueda para localizar:
    
    - **Backups:** `.bak`, `.old`, `.zip`.
        
    - **Configuración:** `web.config`, `settings.php`, `config.php`.
        
    - **Logs:** `error_log`, `access_log`.
        
    - **Contenido:** Credenciales de bases de datos, llaves de API o fragmentos de código fuente.
        

---

#### **🧠 La Importancia del Contexto ("Conectar los Puntos")**

El valor real de los datos no está en encontrarlos aislados, sino en su correlación.

> **Ejemplo de Correlación:**
> 
> 1. Encuentras un **Metadato** que indica una versión antigua de un CMS.
>     
> 2. Ves un **Comentario** que menciona problemas con el "servidor de archivos".
>     
> 3. Identificas un patrón de **Enlaces** que apuntan a `/files/`.
>     
> 4. **Resultado:** Al visitar `/files/`, descubres que la navegación de directorios está activa, exponiendo los backups que sospechabas por el comentario.
>     

#### **Análisis Holístico**

Es esencial considerar las relaciones entre diferentes puntos de datos. Un hallazgo mundano (como una lista de enlaces) puede convertirse en una vulnerabilidad crítica (como un Directorio Expuesto) si se analiza bajo la sospecha generada por otros indicadores.

[[web pentesting]]