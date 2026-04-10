## 🛡️ Diccionario de Vulnerabilidades: CVE y OVAL

### 1. CVE (Common Vulnerabilities and Exposures)

Es el **identificador universal** para una vulnerabilidad específica en un software.

- **Formato:** Siempre lo verás como `CVE-YYYY-XXXXX` (ej. el famoso _Log4Shell_ es `CVE-2021-44228`).
    
- **Función:** Sirve para que todo el mundo (hackers, empresas, herramientas como **Nmap**) hable el mismo idioma. Si tú encuentras una falla en el portal de tu academia, podrías reportarla para que le asignen un CVE.
    

### 2. OVAL (Open Vulnerability Assessment Language)

Si el CVE es el "nombre de la enfermedad", **OVAL es el "examen de laboratorio"** para detectarla. Es un estándar internacional que define un lenguaje técnico para:

- **Codificar atributos:** Cómo revisar archivos, registros y configuraciones del sistema.
    
- **Detallar el estado:** Determinar si un sistema es vulnerable o si cumple con las políticas de seguridad.
    
- **Ecosistema:** Cuenta con una librería de más de **7,000 definiciones** listas para usarse.
    
![[Pasted image 20260215195225.png]]
---
## 📑 El ABC del CVE (Common Vulnerabilities and Exposures)

El **CVE** no es solo una lista; es un sistema de **identificación universal** patrocinado por el Departamento de Seguridad Nacional (DHS) de EE. UU. Su objetivo es que, si un investigador en México y uno en Japón encuentran el mismo error, ambos lo llamen por el mismo nombre.

![[Pasted image 20260215195449.png]]

### 🆔 Anatomía de un Identificador

Cada vulnerabilidad recibe un número único asignado por una **CNA** (CVE Numbering Authority).

- **Propósito:** Crear un estándar para que los equipos de IT sepan exactamente a qué se enfrentan sin confusiones.
    
- **Contenido:** Incluye una descripción técnica, referencias (links a parches o pruebas de concepto) y el nivel de peligro.
    

---

## ⚖️ Reglas para obtener un código CVE

No cualquier error de programación califica para ser un CVE. Para que se asigne un ID, la vulnerabilidad debe cumplir tres requisitos estrictos:

1. **Independientemente reparable:** El fallo debe poder arreglarse de forma separada a otros errores.
    
2. **Afectar un solo código base:** Si el error está en el kernel de Linux, afecta a ese código; si está en Spotify, afecta solo a ese. Si afecta a muchos productos por una librería compartida, se trata de forma específica.
    
3. **Reconocimiento del Proveedor:** El fabricante (Vendor) debe reconocer que el problema existe y documentarlo.
### 3. SCAP (Security Content Automation Protocol)

OVAL es una pieza clave de **SCAP** (respaldado por el NIST). Este protocolo busca **automatizar** tres cosas:

1. Gestión de vulnerabilidades.
    
2. Medición de seguridad.
    
3. Cumplimiento de políticas (Policy Compliance).



## 🛤️ El Camino hacia un CVE (Las 9 Etapas)

El proceso está diseñado para evitar el caos y asegurar que los parches lleguen antes que los ataques.

1. **Validación:** ¿Es realmente una vulnerabilidad? Debe afectar la **Confidencialidad, Integridad o Disponibilidad** y requerir un cambio de código.
    
2. **Contacto (Buena Fe):** Intentar hablar con el dueño del software (el Vendor).
    
3. **Elección del CNA:** Contactar a la autoridad que asigna números (CNA). Puede ser la misma empresa (como Microsoft o Google) o un tercero.
    
4. **Solicitud Formal:** Usar los formularios oficiales de CVE si los pasos anteriores fallan.
    
5. **Confirmación y Revisión:** El equipo de CVE analiza tu hallazgo y pide más datos si es necesario.
    
6. **Asignación Privada:** Te dan el número (ej. CVE-2026-XXXX), pero **aún no es público**.
    
7. **Preparación de Divulgación:** Se avisa a todas las partes involucradas para que preparen el parche.
    
8. **Anuncio:** Se hace público el descubrimiento.
    
9. **Documentación Final:** Se alimenta la base de datos nacional (**NVD**) con todos los detalles técnicos.
    

---

## 🤝 Divulgación Responsable (Responsible Disclosure)

Este es el concepto más importante para tu ética como profesional en **Argos**:

- **¿Qué es?** Darle tiempo al fabricante para arreglar el fallo antes de publicarlo.
    
- **El riesgo del 0-day:** Si publicas un fallo antes de que haya un parche, los cibercriminales lo usarán de inmediato. Esto se llama **Zero Day** porque el fabricante ha tenido "cero días" para protegerse.
    

---

## 🔍 Ejemplos Reales (Para tu portafolio)

- **CVE-2020-5902 (BIG-IP):** Un atacante podía tomar el control total del servidor sin siquiera tener usuario y contraseña. Es el ejemplo perfecto de **RCE** (Remote Code Execution).
    
- **CVE-2021-34527 (PrintNightmare):** Una falla en el servicio de impresión de Windows que permitía a alguien que ya estaba dentro de la red volverse "dueño" de todo el dominio. Es una falla de **Escalada de Privilegios**.