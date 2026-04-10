Iniciarlo


```shell-session
sudo systemctl start nessusd.service
```

To access Nessus, we can navigate to `https://localhost:8834`. Once we arrive at the setup page, we should select `Nessus Essentials` for the free version, and then we can enter our activation code:

Finally, once the setup is complete, we can start creating scans, scan policies, plugin rules, and customizing settings. The `Settings` page has a wealth of options such as setting up a Proxy Server or SMTP server, standard account management options, and advanced settings to customize the user interface, scanning, logging, performance, and security options.

# Nessus

**Etiquetas:** #ciberseguridad #vulnerability-assessment #herramientas #pentesting

**Desarrollador:** Tenable Network Security

## ¿Qué es Nessus?

Nessus es uno de los escáneres de vulnerabilidades más populares y utilizados en la industria de la ciberseguridad. Es una herramienta comercial (con una versión gratuita limitada llamada Nessus Essentials) diseñada para automatizar la detección de fallos de seguridad en sistemas, redes y aplicaciones.

A diferencia de un simple escáner de puertos (como Nmap), Nessus analiza los servicios descubiertos para identificar si son vulnerables a exploits conocidos, si están mal configurados o si les faltan parches de seguridad.

## ¿Para qué sirve?

El objetivo principal de Nessus es proporcionar una "fotografía" del estado de seguridad de un objetivo. Se utiliza habitualmente en las fases de **Reconocimiento** y **Análisis de Vulnerabilidades** para:

- **Identificar vulnerabilidades conocidas (CVEs):** Detecta fallos como EternalBlue (MS17-010), vulnerabilidades en Apache/Nginx, etc.
    
- **Detectar misconfiguraciones:** Encuentra contraseñas por defecto, servicios innecesarios expuestos, o cifrados débiles (ej. SMBv1 activo).
    
- **Auditoría de parches:** Verifica si un sistema operativo o software de terceros tiene instaladas las últimas actualizaciones de seguridad.
    
- **Cumplimiento (Compliance):** Evalúa si un servidor cumple con normativas de seguridad específicas (como CIS Benchmarks, PCI-DSS, HIPAA).
    

## Conceptos Clave (Glosario)

- **Plugins:** Son el "cerebro" de Nessus. Cada plugin es un pequeño script escrito en NASL (Nessus Attack Scripting Language) que contiene la lógica para detectar una vulnerabilidad específica. Nessus compila y actualiza miles de estos plugins constantemente.
    
- **Escaneo No Autenticado (Uncredentialed / Black-box):** El escáner interactúa con el objetivo desde afuera, viendo solo lo que está expuesto públicamente en los puertos de red. Es más rápido pero menos preciso (genera más falsos positivos).
    
- **Escaneo Autenticado (Credentialed / White-box):** Se le proporcionan credenciales a Nessus (SMB para Windows, SSH para Linux). Esto le permite iniciar sesión en la máquina, leer el registro, revisar la lista exacta de software instalado y verificar versiones de archivos locales. Es el método más exhaustivo y profesional.
    
- **Falsos Positivos/Negativos:** Como cualquier herramienta automatizada, Nessus puede equivocarse. Siempre requiere verificación manual por parte de un analista para confirmar que la vulnerabilidad es real y explotable.