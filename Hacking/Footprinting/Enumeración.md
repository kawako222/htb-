La **enumeración** es el proceso cíclico de recopilación de información mediante métodos activos (escaneos) y pasivos (proveedores externos). Se diferencia de [[OSINT]] en que este último es un procedimiento independiente basado exclusivamente en la obtención de información pasiva sin interactuar con el objetivo.

#### **Conceptos Clave**

- **Propósito:** Comprender cómo está configurada la infraestructura y qué servicios son necesarios para ofrecer una función específica, en lugar de intentar forzar la entrada a los sistemas.
    
- **Riesgos de la Fuerza Bruta:** Intentar ataques ruidosos contra [[SSH]], [[RDP]] o [[WinRM]] sin conocer las medidas defensivas puede causar la inclusión en listas negras.
    
- **Visión Estratégica:** El objetivo no es simplemente acceder a los sistemas, sino encontrar todas las rutas posibles para llegar a ellos.
    

#### **Metodología de Análisis (Preguntas de Investigación)**

|**Perspectiva de lo Visible**|**Perspectiva de lo Oculto**|
|---|---|
|¿Qué podemos ver?|¿Qué no podemos ver?|
|¿Qué razones podemos tener para verlo?|¿Qué razones puede haber para no verlo?|
|¿Qué imagen crea lo que vemos?|¿Qué imagen resulta de lo que no vemos?|
|¿Qué ganamos con ello y cómo lo usamos?||

#### **Principios de Enumeración**

1. **Hay más de lo que parece:** Considerar todos los puntos de vista de la infraestructura.
    
2. **Distinción:** Diferenciar entre lo que es visible y lo que permanece oculto.
    
3. **Comprensión:** Siempre existen formas de obtener más información si se comprende técnicamente el objetivo.