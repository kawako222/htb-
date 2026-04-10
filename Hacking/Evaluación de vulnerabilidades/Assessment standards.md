## ⚖️ Estándares y Ética en el Pentesting

Un Pentest no es un ataque libre; es una actividad controlada. Estos son los pilares de un compromiso profesional:

### 1. El Contrato Legal y el Alcance (Scope)

- **Nunca** se realiza un Pentest sin un contrato firmado.
    
- El documento define qué se puede atacar, qué está prohibido y las horas permitidas para trabajar.
    

### 2. Principio de Mínimo Daño

- El objetivo es probar la seguridad, no destruir el negocio.
    
- **Evitar cambios:** No se deben cambiar contraseñas de cuentas reales ni borrar datos.
    
- **Pruebas de concepto:** En lugar de robar archivos sensibles, un Pentester toma una captura de pantalla de los nombres de los archivos para demostrar que tuvo acceso.
    

### 3. Segmentación (CDE)

En entornos financieros, se pone mucho énfasis en el **CDE**. Como Pentester, uno de tus objetivos suele ser intentar saltar desde la red normal de la oficina hacia el CDE para demostrar que la segmentación falló.

# 📑 Metodologías y Marcos de Trabajo (Frameworks)

Para que un Pentest no sea un caos, los profesionales siguen guías que aseguran que no se salte ningún paso crítico.

## 1. PTES (Penetration Testing Execution Standard)

Es el estándar más completo y se puede aplicar a cualquier tipo de prueba. Divide el proceso en 7 fases lógicas:

1. **Pre-engagement Interactions:** Definir contratos, alcances y reglas.
    
2. **Intelligence Gathering:** Recolección de información (OSINT, reconocimiento).
    
3. **Threat Modeling:** Identificar qué activos son los más probables de ser atacados.
    
4. **Vulnerability Analysis:** Buscar los fallos (lo que hace **Equestria**).
    
5. **Exploitation:** Intentar entrar al sistema.
    
6. **Post Exploitation:** Qué puedes hacer una vez dentro (moverte a otros PCs, persistencia).
    
7. **Reporting:** El documento final con los hallazgos.
    

---

## 2. OSSTMM (Open Source Security Testing Methodology Manual)

Se enfoca en la precisión científica de las pruebas. Divide el Pentesting en **5 canales** principales para asegurar una cobertura total:

- **Human Security:** Ingeniería social.
    
- **Physical Security:** Accesos físicos a edificios.
    
- **Wireless Communications:** WiFi, Bluetooth y otras radiofrecuencias.
    
- **Telecommunications:** Telefonía y sistemas de voz.
    
- **Data Networks:** Redes locales y externas.
    

---

## 3. NIST (National Institute of Standards and Technology)

El NIST es el estándar de oro para el gobierno de EE. UU. y muchas empresas globales. Su marco de Pentesting es más simplificado pero muy robusto:

1. **Planning** (Planificación).
    
2. **Discovery** (Descubrimiento).
    
3. **Attack** (Ataque).
    
4. **Reporting** (Reporte).
    

---

## 4. OWASP (Open Web Application Security Project)

Es la referencia absoluta para **aplicaciones web**. Si vas a auditar una web (como la de tu proyecto **Argos**), debes usar sus guías:

- **WSTG (Web Security Testing Guide):** La guía "maestra" para aplicaciones web.
    
- **MSTG (Mobile Security Testing Guide):** Especializada en apps de Android e iOS.
    
- **Firmware Security Testing:** Para dispositivos de Internet de las Cosas (IoT).