### 🕵️‍♂️ El Escenario Práctico (Estudio de Caso)

El texto narra una situación real de pentesting donde el analista se topa con múltiples defensas al intentar escalar privilegios:

- **Punto de partida:** Se logra Ejecución Remota de Código (RCE) en un servidor web IIS y se obtiene una _reverse shell_.
    
- **Bloqueo 1 (Políticas de Host):** Se intenta usar **PowerShell** para descargar el script `PowerUp.ps1`, pero la política de control de aplicaciones lo bloquea.
    
- **La Oportunidad:** Se descubre manualmente el permiso `SeImpersonatePrivilege`, lo que requiere subir el binario `PrintSpoofer` a la máquina víctima.
    
- **Bloqueo 2 (Filtro Web):** Se intenta usar **Certutil** para descargar el binario desde GitHub, pero el proxy/filtro web corporativo bloquea sitios de almacenamiento.
    
- **Bloqueo 3 (Firewall de Red):** Se levanta un servidor **FTP** propio, pero el firewall bloquea la salida por el puerto 21 (TCP).
    
- **¡Éxito! (Evasión por SMB):** Se utiliza **Impacket smbserver**, descubriendo que el tráfico de salida por el puerto 445 (SMB) sí estaba permitido. Se transfiere el archivo y se escala a Administrador.
    

---

### 🛡️ Conceptos y Lecciones Clave

- **Adaptabilidad:** No existe un método único infalible. Tienes que conocer varias rutas porque las herramientas comunes suelen estar vigiladas.
    
- **Conoce a tu enemigo (Las Defensas):** * _Controles de Host:_ Antivirus, EDR y listas blancas (AppLocker) bloquearán ejecutables y scripts no firmados.
    
    - _Controles de Red:_ Firewalls, IDS e IPS vigilarán y cerrarán puertos inusuales o tráfico sospechoso.