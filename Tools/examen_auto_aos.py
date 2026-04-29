from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
import time
import re

def limpiar_texto(texto):
    """Limpia el texto quitando saltos de línea y espacios dobles."""
    if not texto: return ""
    texto = texto.lower()
    # Reemplaza múltiples espacios/saltos por un solo espacio
    return re.sub(r'\s+', ' ', texto).strip()

def automatizar_examen():
    print("[*] Iniciando el navegador...")
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    
    # === LA MAGIA ESTÁ AQUÍ ===
    # En lugar de frases exactas, usamos tuplas de PALABRAS CLAVE.
    # El script verificará que TODAS las palabras de una tupla existan en la opción.
    respuestas_keywords = [
        # Eq 1 - Tema 1
        ("administrar", "recursos", "hardware", "software"),
        ("puente", "usuario", "máquina"),
        ("ejecutar", "varios", "procesos", "simultáneamente"),
        ("protegen", "integridad", "datos", "regulan", "acceso"),
        
        # Eq 2 - Tema 2
        ("bios", "uefi", "configuran", "orden", "inicio"),
        ("fuente", "alimentación", "adecuada", "garantizar"),
        ("códigos", "pitidos", "avisar", "fallos"),
        ("activa", "comienza", "buscar", "sistema", "operativo"),
        
        # Eq 3 - Tema 3
        ("usb", "discos", "ópticos", "red", "iso"),
        ("limpia", "actualizacion", "dual", "boot", "remota"),
        ("ntfs", "fat32", "ext4"),
        ("división", "secciones", "independientes", "disco"),
        
        # Eq 4 - Tema 3
        ("localiza", "núcleo", "sistema", "dispositivo", "almacenamiento"),
        ("configura", "controladores", "adecuados", "dispositivo", "detectado"),
        ("archivos", "configuración", "registros"),
        ("gestión", "red", "almacenamiento", "seguridad"),
        
        # Eq 1 - Tema 5
        ("finalizar", "correctamente", "aplicaciones", "servicios"),
        ("ocasionar", "pérdida", "datos", "fallos"),
        ("teclas", "botones", "físicos", "energía"),
        ("programas", "seguro", "actualizaciones", "interfieren"),
        
        # Eq 2 - Tema 6
        ("sobrecarga", "conflictos", "software", "malware"),
        ("configuraciones", "básicas", "detección", "discos", "prioridades"),
        ("reinicios", "constantes", "bloqueos", "pantallas", "negras"),
        ("desactiva", "servicios", "controladores", "esenciales"),
        
        # Eq 3 - Tema 7 & Procesos
        ("sistema", "actúa", "control", "central", "coordinando"),
        ("control", "central", "gestión", "recursos", "comunicación"),
        ("planificar", "asignar", "sincronizar", "supervisar", "procesos"),
        ("distribución", "necesidades", "programa", "protección", "división"),
        ("forma", "árbol", "jerárquico", "nodo", "raíz", "init"),
        ("genera", "llamada", "sistema", "fork"),
        ("finaliza", "enviar", "señales", "gestionar", "terminación"),
        ("relación", "parental", "determina", "propagan", "permisos"),
        
        # Eq 4 - Tema 4
        ("mecanismos", "simples", "procesos", "envían", "notificaciones"),
        ("garantiza", "procesos", "acceso", "suficiente", "memoria"),
        ("permite", "programas", "utilizar", "memoria", "físicamente"),
        ("procesos", "comparten", "segmentos", "memoria", "intercambiar"),
        ("establece", "organización", "jerárquica", "directorios", "subdirectorios"),
        ("ejecutar", "tareas", "avanzadas", "forma", "eficiente", "expertos"),
        ("firewalls", "cifrado", "capas", "seguridad"),
        ("linux", "jerarquía", "única", "comenzando", "raíz"),
        ("monolíticos", "integran", "funcionalidades", "bloque", "código"),
        ("microkernel", "minimizan", "núcleo", "incluir", "básicas"),
        ("enfoque", "organiza", "sistema", "operativo", "capas"),
        ("arquitectura", "fusiona", "aspectos", "monolítica", "microkernel"),
        
        # Ciclo de vida y concurrencia
        ("cambia", "proceso", "estados", "nuevo", "listo"),
        ("interrupciones", "hardware", "eventos", "externos"),
        ("terminado", "completar", "instrucciones", "señal"),
        ("asigna", "pequeño", "intervalo", "tiempo", "cola"),
        ("unidad", "pequeña", "procesamiento", "tarea", "dentro", "proceso"),
        ("paralelismo", "implica", "ejecución", "simultánea", "múltiples", "núcleos"),
        ("herramientas", "mutex", "aseguran", "hilo", "acceda", "recursos"),
        ("problemas", "múltiples", "hilos", "modifiquen", "datos", "compartidos"),
        
        # Archivos y E/S
        ("unidad", "lógica", "almacenamiento", "contiene", "datos"),
        ("directo",), # Usamos tupla de 1 elemento (ojo con la coma)
        ("organización", "carpetas", "subcarpetas"),
        ("dividir", "memoria", "páginas", "pequeñas", "mejorar"),
        ("ocultar", "detalles", "complejos", "dispositivos", "específicos"),
        ("optimizar", "tiempo", "respuesta", "operaciones", "e/s"),
        ("replicar", "datos", "frecuentemente", "usados", "ubicaciones"),
        ("spooling",),
        ("usuarios", "legítimos", "accedan", "sistema"),
        ("roles", "limitando", "acciones", "minimizando", "riesgos"),
        ("identificar", "accesos", "indebidos", "actividades", "inusuales"),
        ("datos", "transferidos", "dispositivos", "interceptados")
    ]

    url = "https://docs.google.com/forms/d/e/1FAIpQLSdTr4jYUqUXzyGcKlBUU8OirR_8AM28jfzkDuMU9rhjcc8mwA/viewform"
    driver.get(url)

    print("\n" + "="*50)
    print("Inicia sesión en tu cuenta de Google en la ventana.")
    print("Navega hasta que veas las preguntas del examen.")
    input("Presiona ENTER cuando veas las preguntas en la pantalla...")
    print("="*50 + "\n")

    print("[*] Escaneando la página en busca de opciones...")
    marcadas = 0
    respuestas_pendientes = list(respuestas_keywords) # Copia de la lista

    # Estrategia: Buscar todos los contenedores visuales de las opciones de respuesta.
    # En Google Forms, la clase 'M7eMe' (o el contenedor adyacente al radio) suele tener el texto.
    # Para ser seguros, buscaremos el 'div' padre general y leeremos TODO su texto.
    elementos_opciones = driver.find_elements(By.XPATH, "//div[@role='radio' or @role='checkbox']/ancestor::label | //div[@role='radio' or @role='checkbox']/parent::div/parent::div")

    if not elementos_opciones:
        print("[!] No encontré etiquetas <label>. Intentando estrategia alternativa...")
        elementos_opciones = driver.find_elements(By.XPATH, "//div[@role='radio' or @role='checkbox']")

    print(f"[*] Se encontraron {len(elementos_opciones)} bloques de opciones.")

    for elemento in elementos_opciones:
        try:
            texto_web = limpiar_texto(elemento.text)
            if not texto_web:
                continue
                
            match_encontrado = None
            
            # Revisamos si el texto web contiene TODAS las palabras clave de alguna respuesta
            for tupla_keywords in respuestas_pendientes:
                coincide_todas = True
                for kw in tupla_keywords:
                    # Buscamos la palabra exacta usando fronteras de palabra o simplemente `in` si queremos ser laxos
                    if kw.lower() not in texto_web:
                        coincide_todas = False
                        break
                
                if coincide_todas:
                    match_encontrado = tupla_keywords
                    break
            
            if match_encontrado:
                # Hacer Scroll
                driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", elemento)
                time.sleep(0.2)
                
                # Intentamos hacer clic en el contenedor (label) o en su radio button hijo
                click_exitoso = False
                try:
                    # Intento 1: Click directo al elemento de Selenium
                    elemento.click()
                    click_exitoso = True
                except:
                    pass
                
                if not click_exitoso:
                    try:
                        # Intento 2: Buscar el radio button dentro y clickearlo
                        radio = elemento.find_element(By.XPATH, ".//div[@role='radio' or @role='checkbox']")
                        driver.execute_script("arguments[0].click();", radio)
                        click_exitoso = True
                    except:
                        pass
                
                if not click_exitoso:
                    # Intento 3: Click forzado por JS en el contenedor principal
                    driver.execute_script("arguments[0].click();", elemento)
                
                marcadas += 1
                print(f"[+] Marcada opción con keywords: {match_encontrado}")
                respuestas_pendientes.remove(match_encontrado)

        except Exception as e:
            # print(f"Error procesando elemento: {e}")
            continue

    print(f"\n[!] Finalizado. Se lograron marcar {marcadas} respuestas.")
    print("[*] Revisa el formulario visualmente antes de enviarlo.")
    input("Presiona ENTER para cerrar el navegador...")
    driver.quit()

if __name__ == "__main__":
    automatizar_examen()
