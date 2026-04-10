
El objetivo central de cualquier **Security Assessment** es identificar, confirmar y neutralizar vulnerabilidades (mediante parches, mitigación o eliminación) para fortalecer la postura de ciberseguridad de una organización.

## 📌 Conceptos Clave

- **Adaptabilidad:** No existe una metodología única. Las evaluaciones dependen de los requisitos de cumplimiento, la tolerancia al riesgo y el modelo de negocio.
    
- **Niveles de Madurez:** 
	-  _Nivel Básico:_ Organizaciones que apenas establecen controles de seguridad esenciales.
    
	- _Nivel Avanzado:_ Organizaciones con posturas maduras que realizan simulaciones de **Red Team**.
        
- **Continuidad:** Es imperativo mantenerse al tanto de vulnerabilidades tanto **heredadas (legacy)** como recientes.
    

---

## 🔍 Evaluación de Vulnerabilidades (Vulnerability Assessment)

Es un proceso universalmente aplicable que mide qué tan bien se alinea una red con **estándares de seguridad específicos**.

### 🛠️ Características Principales:

1. **Basada en Estándares:** Se utilizan listas de verificación (checklists) derivadas de marcos normativos.
    
2. **Factores Determinantes:** Los estándares aplicados varían según:
    
    - Regulaciones regionales o de industria (ej. GDPR, PCI-DSS).
        
    - Tamaño y arquitectura de la red.
        
    - Nivel de madurez de seguridad actual.
        
3. **Versatilidad:** Puede ejecutarse como un proceso independiente o integrarse dentro de un ecosistema de evaluaciones más amplio.
# 🕵️ Penetration Testing (Pentesting)

Un **Pentest** es un ataque cibernético simulado diseñado para determinar **si** y **cómo** un atacante podría penetrar una red. A diferencia de un ataque real, este se realiza con **consentimiento legal total** y bajo un contrato estricto que define el alcance (qué se puede y qué no se puede tocar).

## 🔳 Tipos de Pentest según el conocimiento previo

- **Black Box (Caja Negra):** El auditor no tiene conocimiento previo de la infraestructura. Se simula a un atacante externo. A menudo solo se le da el nombre de la empresa.
    
- **Grey Box (Caja Gris):** Conocimiento limitado. Simula la perspectiva de un empleado que no es de TI (recepcionista, soporte). Se suelen entregar rangos de IP o accesos básicos.
    
- **White Box (Caja Blanca):** Conocimiento total. Acceso a configuraciones, documentos de red y código fuente. El objetivo es encontrar el mayor número de fallos posible en poco tiempo.
    

---

## 🎯 Especialidades en Pentesting

1. **Application Pentesting:** Evaluación de aplicaciones web, móviles, APIs y software de escritorio. Incluye revisión de código fuente (Secure Code Review).
    
2. **Network/Infrastructure:** Evaluación de routers, firewalls, servidores y Active Directory. Requiere dominio de redes, Linux/Windows y scripting.
    
    > ⚠️ **Nota:** Los escáneres automáticos (como Nessus) son solo una herramienta auxiliar; no reemplazan el análisis humano.
    
3. **Physical Pentesting:** Pruebas de seguridad física. Intentar entrar a oficinas, centros de datos o gatear por ductos de ventilación.
    
4. **Social Engineering:** Probar el "eslabón más débil": el humano. Phishing, vishing o suplantación de identidad presencial.
    

---

## 📈 Madurez de Seguridad y Pentesting

El Pentesting es más efectivo en organizaciones con una **madurez de seguridad media o alta**.

- **Madurez Alta:** Implica tener CISO/CTO, políticas de parches, un equipo de respuesta a incidentes (CSIRT) y una cultura de seguridad sólida.
    
- **Madurez Baja:** Organizaciones que aún no tienen lo básico deben empezar con **Vulnerability Assessments**. Un Pentest en una red inmadura encontraría tantas fallas que abrumaría al equipo de remediación sin ser útil.
## 🔍 Vulnerability Assessment vs. Penetration Test

Aunque a menudo se confunden, son procesos distintos que se complementan.

### 1. Vulnerability Assessment (Evaluación de Vulnerabilidades)

- **Enfoque:** Listas de verificación (**checklists**) y estándares (GDPR, OWASP, PCI-DSS).
    
- **Método:** Escaneo de vulnerabilidades seguido de una **validación** para descartar falsos positivos.
    
- **Límite:** El auditor demuestra que la vulnerabilidad existe, pero **no realiza explotación** (no busca escalada de privilegios ni movimiento lateral).
    
- **Objetivo:** Obtener una visión periódica (mensual o trimestral) de los problemas conocidos.
    

### 2. Penetration Test (Pentest)

- **Enfoque:** Ataque cibernético simulado para evaluar el impacto real y la seguridad de los activos.
    
- **Método:** Tácticas manuales y automatizadas. Ilustra una **cadena de ataque real** (Attack Chain).
    
- **Requisito:** Solo debe realizarse después de que se hayan hecho evaluaciones de vulnerabilidad y se hayan aplicado parches.
    
- **Objetivo:** Identificar fallos que los escáneres automáticos no detectan.
## 📋 Otros Tipos de Evaluaciones

### ⚖️ Auditorías de Seguridad (Security Audits)

A diferencia de las evaluaciones internas, las auditorías son **obligatorias y mandatorias** por entidades externas o regulaciones gubernamentales.

- **Ejemplo:** **PCI-DSS** para cualquier negocio que acepte tarjetas de crédito. El incumplimiento conlleva multas o la prohibición de procesar pagos.
    

### 💰 Bug Bounties

Programas donde se invita al público general (hackers éticos) a encontrar vulnerabilidades a cambio de recompensas económicas.

- **Uso:** Ideal para empresas con **alta madurez de seguridad** (Microsoft, Apple) que pueden gestionar el triaje de reportes masivos.
    

### 🔴 Red Team Assessment

Evaluación ofensiva avanzada y evasiva (Black Box).

- **Enfoque en Objetivos:** No busca encontrar "todas" las fallas, sino cumplir un objetivo específico (ej. comprometer la base de datos de clientes).
    
- **Dinámica:** Simula las acciones de grupos de amenazas persistentes avanzadas (**APTs**).
    

### 🟣 Purple Team Assessment

Es la colaboración directa entre el **Red Team** (Ofensivo) y el **Blue Team** (Defensivo/SOC).

- **Dinámica:** El equipo azul observa el ataque en tiempo real, aprende las técnicas del equipo rojo y proporciona retroalimentación inmediata para mejorar la detección y respuesta.