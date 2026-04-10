
La enumeración es un proceso dinámico que requiere una metodología estandarizada para evitar omisiones por error. Esta se divide en **3 niveles** (Infrastructure-based, Host-based y OS-based) y se estructura en **6 capas** progresivas.

---
![[Pasted image 20260208212916.png]]
#### **Capas de la Metodología**

|**Capa**|**Nombre**|**Descripción**|**Categorías de Información**|
|---|---|---|---|
|**1**|**Internet Presence**|Identificación de presencia e infraestructura externa.|Dominios, Subdominios, vHosts, ASN, IPs, Cloud.|
|**2**|**Gateway**|Identificar medidas de seguridad y protección.|Firewalls, IDS/IPS, WAF (Cloudflare), VPN, Proxies.|
|**3**|**Accessible Services**|Identificar interfaces y servicios (externos/internos).|Tipo de servicio, Puerto, Versión, Interfaz.|
|**4**|**Processes**|Identificar procesos internos y tareas asociadas.|PID, Datos procesados, Origen, Destino.|
|**5**|**Privileges**|Identificación de permisos y privilegios de servicios.|Grupos, Usuarios, Permisos, Restricciones.|
|**6**|**OS Setup**|Identificación de componentes y configuración del SO.|Tipo de SO, Nivel de parche, Archivos de conf.|

---

#### **Objetivos por Capa**

- **Capa 1 (Presencia):** Identificar todos los sistemas y superficies de ataque posibles.
    
- **Capa 2 (Puerta de enlace):** Comprender con qué estamos lidiando y de qué debemos cuidarnos.
    
- **Capa 3 (Servicios):** Entender la funcionalidad del sistema para comunicarse con él y explotarlo.
    
- **Capa 4 (Procesos):** Identificar dependencias entre comandos, fuentes y destinos.
    
- **Capa 5 (Privilegios):** Identificar qué es posible hacer con los permisos del usuario/servicio.
    
- **Capa 6 (Configuración):** Evaluar la gestión administrativa y recolectar información sensible interna.
    

---

#### **Notas Metodológicas**

- **Dinamismo:** La metodología no es una guía paso a paso, sino un resumen de procedimientos sistemáticos. Las herramientas y comandos específicos pertenecen a una **"Hoja de trucos" (Cheat Sheet)**, no a la metodología en sí.
    
- **Límites:** Una prueba de penetración no garantiza la ausencia total de vulnerabilidades; siempre pueden existir brechas que requieren un análisis más profundo y prolongado.
    

¿Te gustaría que te ayude a crear la **"Hoja de trucos"** de comandos para la **Capa 1** (DNS, vHosts e IPs) y así tenerla vinculada a esta nota?