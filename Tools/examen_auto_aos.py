from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import re

def limpiar_texto(texto):
    if not texto: return ""
    return re.sub(r'\s+', ' ', texto.lower()).strip()

def automatizar_examen():
    print("\n" + "="*50)
    url_formulario = input("[?] Pega aquí la URL del examen de Google Forms:\n> ").strip()
    if not url_formulario: return

    print("[*] Iniciando el navegador...")
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    
    # Tus palabras clave (dejé las mismas que ya tenías)
    respuestas_keywords = [
    # Equipo 1 - Tema 1
    ("administrar", "recursos", "hardware", "software"),
    ("puente", "usuario", "máquina"),
    ("ejecutar", "varios", "procesos", "simultáneamente"),
    ("protegen", "integridad", "datos", "regulan", "acceso"),

    # Equipo 2 - Tema 2
    ("bios", "uefi", "configuran", "orden", "inicio", "dispositivos"),
    ("fuente", "alimentación", "adecuada", "garantizar", "componentes"),
    ("códigos", "pitidos", "avisar", "fallos"),
    ("activa", "comienza", "buscar", "sistema", "operativo", "ubicación"),

    # Equipo 3 - Tema 3
    ("discos", "duros", "cd", "google", "drive"),  # FORMULARIO INCORRECTO (PDF dice USB/ISO)
    ("limpia", "actualizacion", "dual", "boot", "remota"),
    ("ntfs", "fat32", "ext4"),
    ("división", "secciones", "independientes", "disco", "almacenamiento"),

    # Equipo 4 - Tema 3
    ("localiza", "núcleo", "sistema", "dispositivo", "almacenamiento"),
    ("configura", "controladores", "adecuados", "dispositivo", "detectado"),
    ("archivos", "configuración", "registros"),
    ("gestión", "red", "almacenamiento", "seguridad"),

    # Equipo 1 - Tema 5
    ("finalizar", "correctamente", "aplicaciones", "servicios", "apagado"),
    ("ocasionar", "pérdida", "datos", "fallos", "sistema"),
    ("teclas", "botones", "físicos", "energía"),
    ("programas", "seguro", "actualizaciones", "interfieren"),

    # Equipo 2 - Tema 6
    ("sobrecarga", "conflictos", "software", "malware"),
    ("configuraciones", "básicas", "detección", "discos", "prioridades"),
    ("reinicios", "constantes", "bloqueos", "pantallas", "negras"),
    ("desactiva", "servicios", "controladores", "esenciales"),

    # Equipo 3 - Tema 7
    ("sistema", "actúa", "control", "central", "coordinando"),
    ("control", "central", "gestión", "recursos", "comunicación"),
    ("planificar", "asignar", "sincronizar", "supervisar", "procesos"),
    ("distribución", "necesidades", "programa", "protección", "división"),

    # Equipo 4 - Tema 3 P8
    ("establece", "organización", "jerárquica", "directorios", "subdirectorios"),
    ("ejecutar", "tareas", "avanzadas", "eficiente", "expertos"),
    ("firewalls", "cifrado", "capas", "seguridad"),
    ("linux", "jerarquía", "única", "raíz", "windows", "letras", "unidad"),

    # Equipo 4 - Tema 4 P4 (IPC / Memoria)
    ("mecanismos", "simples", "procesos", "envían", "notificaciones", "sigint"),
    ("garantiza", "procesos", "acceso", "suficiente", "memoria", "física"),
    ("permite", "programas", "utilizar", "memoria", "físicamente", "disponible"),
    ("procesos", "comparten", "segmentos", "memoria", "intercambiar", "volúmenes"),

    # Equipo 4 - Tema 4 P8 (Arquitecturas)
    ("monolíticos", "integran", "funcionalidades", "bloque", "código", "rendimiento", "dificultando"),
    ("microkernel", "minimizan", "núcleo", "básicas", "delegando", "módulos"),
    ("enfoque", "organiza", "capas", "interactúa", "inmediata", "superior", "inferior"),
    ("fusiona", "monolítica", "microkernel", "aprovecha", "beneficios", "estabilidad"),

    # Equipo 1 - Tema 4 P1 (Ciclo de vida)
    ("cambia", "proceso", "estados", "nuevo", "listo", "ejecución", "bloqueado"),
    ("interrupciones", "hardware", "eventos", "externos"),
    ("terminado", "completar", "instrucciones", "señal", "explícita"),
    ("asigna", "pequeño", "intervalo", "tiempo", "cola", "listo"),

    # Equipo 2 - Tema 4 P2 (Hilos)
    ("unidad", "pequeña", "procesamiento", "tarea", "dentro", "proceso"),
    ("paralelismo", "implica", "ejecución", "simultánea", "núcleos", "concurrencia", "alternando"),
    ("herramientas", "mutex", "aseguran", "hilo", "acceda", "recursos", "incoherencias"),
    ("problemas", "múltiples", "hilos", "modifiquen", "datos", "compartidos"),

    # Equipo 3 - Tema 3 P3 (Procesos árbol)
    ("forma", "árbol", "jerárquico", "nodo", "raíz", "init"),
    ("genera", "llamada", "sistema", "fork", "heredando", "recursos"),
    ("finaliza", "enviar", "señales", "gestionar", "terminación", "hijos"),
    ("relación", "parental", "determina", "propagan", "permisos", "variables"),

    # Equipo 4 - Tema 4 P4 segunda parte (IPC señales versión corta)
    ("mecanismos", "simples", "proceso", "envía", "notificaciones", "comandos"),
    ("gestión", "memoria", "protege", "fallos", "jerarquía", "asignación", "eficiente"),
    ("mover", "datos", "ram", "disco", "duro", "llena"),
    ("divide", "memoria", "bloques", "tamaño", "fijo", "organizar"),

    # Equipo 1 - Tema 4 P5 (Archivos)
    ("unidad", "lógica", "almacenamiento", "contiene", "datos", "programas"),
    ("directo",),   # ← coma obligatoria para que sea tupla
    ("organización", "carpetas", "subcarpetas"),
    ("dividir", "memoria", "páginas", "pequeñas", "mejorar", "gestión"),

    # Equipo 2 - Tema 4 P6 (E/S)
    ("ocultar", "detalles", "complejos", "dispositivos", "interfaces", "estándar"),
    ("optimizar", "tiempo", "respuesta", "operaciones"),
    ("replicar", "datos", "frecuentemente", "usados", "ubicaciones", "acceso", "rápido"),
    ("spooling",),  # ← coma obligatoria

    # Equipo 3 - Tema 7 P3 (Seguridad)
    ("usuarios", "legítimos", "accedan", "sistema"),
    ("roles", "limitando", "acciones", "minimizando", "riesgos"),
    ("identificar", "accesos", "indebidos", "actividades", "inusuales"),
    ("datos", "transferidos", "dispositivos", "interceptados"),

    # Pregunta: "¿Cuál de las siguientes describe el mecanismo de señales en IPC?" (Equipo 4 Tema 4)
    # La respuesta tiene "SIGINT" — palabra única, no aparece en ninguna otra opción
    ("sigint", "interrupciones", "notificaciones", "comandos"),

    # Pregunta: "¿Cómo describirías las señales IPC?" (Equipo 4 Tema 4 segunda versión)
    # La respuesta tiene "notificaciones/comandos" sin mencionar SIGINT
    ("mecanismos", "simples", "proceso", "envía", "notificaciones"),

    # Pregunta: abstracción del hardware
    # "simplificando el desarrollo de software" es único de esta opción
    ("ocultar", "detalles", "simplificando", "desarrollo", "software"),

    # Pregunta: almacenamiento en caché
    # "reduciendo el tiempo de espera y mejorando la eficiencia" es único
    ("replicar", "frecuentemente", "reduciendo", "tiempo", "espera", "eficiencia"),

    # Pregunta: "Directo" — el problema aquí es diferente
    # La opción solo dice "Directo", una sola palabra, el umbral del 60% nunca se cumple con pocas keywords
    # Bajar el umbral o usar una tupla de 1 elemento con coma:
    ("directo",),
]

    driver.get(url_formulario)

    print("\n" + "="*50)
    input("1. Inicia sesión.\n2. Llega a las preguntas.\n3. Presiona ENTER aquí para aniquilar el examen...")
    print("="*50 + "\n")

    print("[*] Cacheando textos de la página (Ultra rápido)...")
    
    # Agarramos las opciones visuales
    elementos = driver.find_elements(By.XPATH, "//div[@role='radio' or @role='checkbox']/ancestor::label | //div[@role='radio' or @role='checkbox']/parent::div/parent::div")
    if not elementos:
        elementos = driver.find_elements(By.XPATH, "//div[@role='radio' or @role='checkbox']")

    # MAGIA DE VELOCIDAD: Extraemos todos los textos a la RAM de Python de un solo golpe.
    cache_opciones = []
    for el in elementos:
        texto = limpiar_texto(el.text)
        if texto:
            cache_opciones.append({"elemento": el, "texto": texto, "usado": False})

    print(f"[*] Escaneados {len(cache_opciones)} elementos. Calculando...")

    marcadas = 0

    for tupla_keywords in respuestas_keywords:
        mejor_opcion = None
        max_aciertos = 0
        
        # Procesamos todo en la RAM, sin preguntarle al navegador (Tarda milisegundos)
        for cache in cache_opciones:
            if cache["usado"]: continue # Saltamos las ya marcadas
            
            aciertos_actuales = sum(1 for kw in tupla_keywords if kw in cache["texto"])
            
            if aciertos_actuales > max_aciertos:
                max_aciertos = aciertos_actuales
                mejor_opcion = cache

        umbral_minimo = 1 if len(tupla_keywords) == 1 else max(1, len(tupla_keywords) * 0.6)


        if mejor_opcion and max_aciertos >= umbral_minimo:
            try:
                # CLIC INSTANTÁNEO CON JAVASCRIPT (Sin scroll, sin esperas)
                el = mejor_opcion["elemento"]
                try:
                    radio = el.find_element(By.XPATH, ".//div[@role='radio' or @role='checkbox']")
                    driver.execute_script("arguments[0].click();", radio)
                except:
                    driver.execute_script("arguments[0].click();", el)
                
                marcadas += 1
                mejor_opcion["usado"] = True # Marcamos como usado para no repetir
                print(f"[+] Marcada rápida ({max_aciertos}/{len(tupla_keywords)}) -> {tupla_keywords[:3]}")
            except:
                pass

    print(f"\n[!] ¡Rápido y letal! Marcadas: {marcadas}.")
    input("[*] Presiona ENTER para salir...")
    driver.quit()

if __name__ == "__main__":
    automatizar_examen()