import sys
import os
import subprocess
import platform
import re

# ============================================================
#  BANNER + COLORES
# ============================================================

class C:
    RED    = "\033[91m"
    GREEN  = "\033[92m"
    YELLOW = "\033[93m"
    CYAN   = "\033[96m"
    WHITE  = "\033[97m"
    DIM    = "\033[2m"
    RESET  = "\033[0m"
    BOLD   = "\033[1m"

BANNER = f"""
            {C.RED}{C.BOLD}
            ███████╗ ██████╗ ██████╗ ███╗   ███╗███████╗
            {C.RED}██╔════╝██╔═══██╗██╔══██╗████╗ ████║██╔════╝
            {C.RED}█████╗  ██║   ██║██████╔╝██╔████╔██║███████╗
            {C.YELLOW}██╔══╝  ██║   ██║██╔══██╗██║╚██╔╝██║╚════██║
            {C.YELLOW}██║     ╚██████╔╝██║  ██║██║ ╚═╝ ██║███████║
            {C.YELLOW}╚═╝      ╚═════╝ ╚═╝  ╚═╝╚═╝     ╚═╝╚══════╝
            {C.RED}██╗  ██╗██╗██╗     ██╗     ███████╗██████╗
            {C.RED}██║ ██╔╝██║██║     ██║     ██╔════╝██╔══██╗
            {C.RED}█████╔╝ ██║██║     ██║     █████╗  ██████╔╝
            {C.YELLOW}██╔═██╗ ██║██║     ██║     ██╔══╝  ██╔══██╗
            {C.YELLOW}██║  ██╗██║███████╗███████╗███████╗██║  ██║
            {C.YELLOW}╚═╝  ╚═╝╚═╝╚══════╝╚══════╝╚══════╝╚═╝  ╚═╝
            {C.DIM}{C.WHITE}          [ Google Forms Auto-Solver v2.0 ]
                    [ coded for educational purposes   ]{C.RESET}

⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣠⣤⣤⣤⣀⣀⡀⠀⠀⠀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⢄⢀⠀⡀⣠⣴⣾⣿⠿⠟⠛⠛⠛⠿⠿⠿⠽⠿⠿⠿⠿⠿⢶⣦⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⡿⡵⣯⣾⣿⣿⠟⠉⢀⣤⠶⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠙⠿⣷⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣿⢫⣮⢿⣿⡿⠛⠁⠠⠔⢋⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⠀⠈⠻⣷⣦⠠⣃⣆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣾⢟⣵⡿⢻⡿⠋⠀⠀⣠⢴⡾⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠁⠀⠀⠈⢻⣷⣏⢫⣧⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⣿⣿⢸⣿⣠⠋⠀⡠⣪⢞⡵⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⣿⣧⡻⣷⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡟⡙⢾⣿⣸⡟⠁⠀⢠⠞⠁⠋⠀⠀⡴⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⣿⣷⡹⣷⡄⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⠁⡇⢸⣿⠋⠀⢀⡶⠃⠀⠀⢠⠃⠜⠁⠀⣀⠀⠀⠀⠀⢀⣦⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠨⣿⠏⣿⣇⡀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡏⠀⡄⡼⠁⠀⢀⣾⠁⠀⠀⠀⡜⡸⠀⠀⣰⢻⠀⠀⠀⠀⢸⠉⣦⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣆⠀⠀⠀⠀⠀⢿⢸⣿⢻⢱⡄⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢰⠁⢀⡟⠀⢠⢃⣾⠇⠀⠀⠀⢰⠁⠀⠀⣰⢃⢸⡄⡄⠀⠀⢸⢀⠘⢧⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⡄⢸⠀⠀⠀⢸⣾⠃⠈⠈⡇⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡎⢠⠞⠀⡰⠃⣼⠏⠀⠀⠀⠀⡜⠀⠀⢰⠃⠉⠸⡇⣧⠀⠀⢸⠈⢦⠘⢷⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⢱⡀⠁⠀⠀⢸⡿⠀⠀⠀⡇⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⢰⣵⠃⠀⢰⠁⣼⠏⠀⠀⠀⠀⢀⠇⠀⢠⠟⠒⠒⠴⣷⣿⡀⠀⢸⠂⠀⠱⣄⠻⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⢧⠀⠀⠀⠈⠀⠀⠀⠀⠣⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⣠⡾⢋⠀⢀⠇⣸⠏⠀⠀⠀⠀⠀⡸⠄⢀⠎⠀⠀⠀⠀⠸⣇⢣⠀⢸⡄⠀⠀⠈⡴⠞⣆⠀⠀⠀⠀⠀⠀⠀⠀⠘⡆⠀⠀⠀⠀⠀⠀⠀⢰⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⢀⡾⢟⡇⡘⠃⡜⣼⣯⠀⠀⠀⠀⠀⠀⡇⢀⡞⠀⠀⠀⠀⠀⠀⢻⠈⢧⠸⡇⠀⠀⠀⠀⠀⠙⢆⠀⠀⠀⠀⠀⠀⠀⠀⢹⡀⠀⠀⠀⠀⠀⠀⢸⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠐⠉⠀⡸⠀⠃⢰⣻⣯⠇⠀⠀⠀⠀⠀⢸⢁⣾⣤⣀⠀⠀⠀⠀⠀⠀⠀⠈⢷⡇⠀⠀⠀⠀⠀⠀⠈⠧⡀⠀⢠⠀⠀⠀⠀⠀⢧⠀⠀⠀⠀⠀⠀⢸⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⡇⠀⢀⣷⢣⠎⠀⠀⠀⠀⠀⠀⢹⡞⠀⠉⠛⠿⣶⣬⡒⠄⠀⠀⠀⠈⠋⠀⠀⠀⣀⡀⠀⣀⣀⣼⣦⡀⢇⠀⠀⠀⠀⠸⣧⠀⠀⠀⠀⠀⢸⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⢀⠀⠀⣼⣯⠏⢀⣀⡀⠀⠀⠀⠀⢸⡇⢰⠿⠿⠿⠟⠛⠛⠃⠀⠀⠀⠀⠀⠀⠀⣯⣴⣾⡿⠛⠛⠉⠉⠳⡞⡆⠀⢀⣀⢰⠻⣆⠀⠀⠀⠀⠈⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⢸⠀⠀⣿⠋⠀⡜⠀⡇⠀⠀⠀⠀⢸⣷⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠙⠛⠿⢷⣶⠀⡼⠀⠹⣀⣺⠈⡏⠇⠀⠀⠀⠀⠀⠀⡇⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⡏⠀⠜⠁⠀⢀⠃⢰⠃⠀⣰⡆⠀⢸⠉⢣⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣼⢧⣄⣴⠋⢿⡀⢹⠀⠀⠀⠀⠀⠀⠀⡇⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⢠⠇⠀⠀⠀⠀⡞⠀⢸⢀⡞⠁⣸⠀⢸⣄⠀⢣⡀⠀⠀⠀⠀⠀⡤⠤⠤⢄⣀⠀⠀⠀⠀⠀⠀⠀⢀⠞⡟⡎⡧⠨⠀⠀⡇⠈⡇⠀⠀⠀⠀⠀⠀⡇⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⢸⠀⠀⠀⠀⢠⠇⢀⣿⠏⠀⡰⢹⠀⢸⠈⠳⣤⣥⣄⣀⣀⣀⡀⠣⡀⠀⢀⠔⠀⠀⠀⠀⠀⣀⡴⠃⣼⡇⢠⠛⡄⠀⠀⢡⠀⢺⠀⠀⠀⠀⠀⠀⢰⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⡞⠀⠀⠀⠀⡼⠀⢸⠃⠀⢠⠃⠀⡆⢸⠀⠀⠈⠉⢻⣿⣿⣿⣿⡇⠈⠉⠁⠀⠀⠀⣠⠶⠾⠧⠄⠐⣻⢠⠃⠀⠱⡀⠀⠘⡄⠈⣆⠀⠀⠀⠀⠀⢸⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⣰⣣⠤⠎⠉⠽⠁⠀⠘⠀⡲⠏⠀⠀⢱⢸⠀⠀⠀⠀⠀⠘⠀⣷⢄⠑⠦⠤⠒⢂⣩⡮⡞⠀⠀⠀⠀⢠⣧⠃⠀⠀⠀⢣⠠⠀⠃⠀⠘⠍⠙⢦⠤⣕⠾⡄⠀⠀⠀⠀
⠀⠀⠀⠀⢰⢹⡀⠀⠀⠀⠀⠀⠀⠀⠈⠙⠀⣄⡀⠈⢿⠀⠀⠀⣰⢞⠇⠀⠘⠀⠙⣢⣠⠖⠉⠈⠀⠀⠈⢢⣀⠀⠰⠃⠀⠀⢀⡴⡞⠉⠀⠀⠀⠀⠀⠀⠈⠀⢸⠎⡇⠀⠀⠀⠀
⠀⠀⠀⢀⣾⣄⢧⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢻⣝⠢⡌⠀⠀⢸⣿⡆⠀⠀⠀⠀⢀⡨⠶⢀⡀⠀⣠⢦⡀⣸⣿⠀⠀⠀⣠⢞⣩⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⠞⡼⢱⠀⠀⠀⠀
⠀⠀⠀⣼⣿⣾⣷⣍⠲⢄⡀⠀⠀⠀⠀⠀⢀⣾⣿⡷⣌⢢⡀⣾⠛⣿⡀⠀⠀⣠⡏⠀⠀⠀⢱⣘⢧⣠⢿⡏⢻⡧⢠⠟⡵⢿⣿⣧⠀⠀⠀⠀⠀⠀⣀⡤⢞⣡⣾⣾⣌⣆⠀⠀⠀
⠀⠀⢰⣿⣿⣿⣿⣿⣿⣶⣬⡑⠲⢤⣀⣠⣾⣿⣿⠃⠈⢢⢻⡇⠀⠙⠷⠞⠋⠉⢷⠀⠀⢠⡋⠛⠻⠻⠟⠁⠈⣻⢇⠞⠁⣹⣿⣿⣷⣄⣀⠤⠖⣋⣥⣶⣿⣿⣿⣿⣿⣼⡄⠀⠀
⠀⢠⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣬⣌⣉⠙⠛⠓⠒⠚⣠⠏⠀⠀⠀⠀⠀⠀⢸⠀⠀⢸⡀⠀⠀⠀⠀⠀⠀⢿⡘⠒⠒⠚⠛⠋⣉⣨⣤⣶⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣧⠀⠀
⢀⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣭⣽⠿⣹⠁⠀⠀⠀⠀⠀⠀⠀⢸⠀⠀⠸⡇⠀⠀⠀⠀⠀⠀⠀⠸⣿⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢧⠀
⢾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠋⡴⡏⠀⠀⠀⠀⠀⠀⠀⠀⡟⠀⠀⠀⡇⠀⠀⠀⠀⠀⠀⠀⠈⣿⡄⠙⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣯⢇
⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠋⢠⢰⣿⠁⠀⠀⠀⠀⠀⠀⠀⠀⡇⠀⠀⠀⡇⠀⢠⣀⣀⣀⣀⣦⠀⢹⣧⠀⠈⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣮
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠏⠀⠀⠘⣿⠏⠀⠀⠀⠀⠀⠀⠀⠀⠀⡇⠀⠀⠀⡇⠀⠀⠉⠉⠉⠉⠁⠀⠀⢿⣶⠀⠀⠈⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠟⠁⠀⠀⠀⢰⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠁⠀⠀⠀⢸⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⠀⠀⠀⠀⠈⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
"""

def print_banner():
    # Limpia pantalla según OS
    os.system("cls" if platform.system() == "Windows" else "clear")
    print(BANNER)

def print_status(msg, tipo="info"):
    iconos = {
        "info":    f"{C.CYAN}[*]{C.RESET}",
        "ok":      f"{C.GREEN}[+]{C.RESET}",
        "warn":    f"{C.YELLOW}[!]{C.RESET}",
        "error":   f"{C.RED}[-]{C.RESET}",
        "input":   f"{C.YELLOW}[?]{C.RESET}",
    }
    print(f"  {iconos.get(tipo, '[*]')} {msg}")

# ============================================================
#  VERIFICACIÓN DE DEPENDENCIAS
# ============================================================

DEPS = ["selenium", "webdriver_manager"]

def verificar_e_instalar_deps():
    print_status("Verificando dependencias...", "info")
    faltantes = []

    for dep in DEPS:
        try:
            __import__(dep)
            print_status(f"{dep:<20} {C.GREEN}OK{C.RESET}", "ok")
        except ImportError:
            print_status(f"{dep:<20} {C.RED}NO INSTALADO{C.RESET}", "error")
            faltantes.append(dep)

    if faltantes:
        print()
        print_status(f"Instalando: {', '.join(faltantes)}", "warn")
        try:
            subprocess.check_call(
                [sys.executable, "-m", "pip", "install"] + faltantes,
                stdout=subprocess.DEVNULL,
                stderr=subprocess.DEVNULL
            )
            print_status("Dependencias instaladas correctamente.", "ok")
        except subprocess.CalledProcessError:
            print_status("Error instalando dependencias. Corre manualmente:", "error")
            print(f"\n    pip install {' '.join(faltantes)}\n")
            sys.exit(1)
    else:
        print_status("Todas las dependencias están listas.", "ok")

    print()

# ============================================================
#  INFO DEL SISTEMA
# ============================================================

def mostrar_info_sistema():
    so = platform.system()
    so_ver = platform.version()
    py_ver = platform.python_version()
    arch = platform.machine()

    print_status(f"Sistema operativo : {C.CYAN}{so} {arch}{C.RESET}", "info")
    print_status(f"Python            : {C.CYAN}v{py_ver}{C.RESET}", "info")
    print()

# ============================================================
#  LÓGICA PRINCIPAL
# ============================================================

def limpiar_texto(texto):
    if not texto: return ""
    return re.sub(r'\s+', ' ', texto.lower()).strip()

def automatizar_examen():
    print_banner()
    mostrar_info_sistema()
    verificar_e_instalar_deps()

    # Importamos DESPUÉS de verificar que existen
    from selenium import webdriver
    from selenium.webdriver.common.by import By
    from selenium.webdriver.chrome.service import Service
    from webdriver_manager.chrome import ChromeDriverManager

    print()
    print_status("Pega aquí la URL del examen de Google Forms:", "input")
    url_formulario = input(f"  {C.YELLOW}>{C.RESET} ").strip()
    if not url_formulario:
        print_status("URL vacía. Saliendo.", "error")
        return

    print()
    print_status("Iniciando ChromeDriver...", "info")
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

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
        ("discos", "duros", "cd", "google", "drive"),
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

        # Equipo 4 - Tema 4 P4 (IPC / Memoria) — versión larga con SIGINT
        ("sigint", "interrupciones", "notificaciones", "comandos"),
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
        ("directo",),
        ("organización", "carpetas", "subcarpetas"),
        ("dividir", "memoria", "páginas", "pequeñas", "mejorar", "gestión"),

        # Equipo 2 - Tema 4 P6 (E/S)
        ("ocultar", "detalles", "simplificando", "desarrollo", "software"),
        ("optimizar", "tiempo", "respuesta", "operaciones"),
        ("replicar", "frecuentemente", "reduciendo", "tiempo", "espera", "eficiencia"),
        ("spooling",),

        # Equipo 3 - Tema 7 P3 (Seguridad)
        ("usuarios", "legítimos", "accedan", "sistema"),
        ("roles", "limitando", "acciones", "minimizando", "riesgos"),
        ("identificar", "accesos", "indebidos", "actividades", "inusuales"),
        ("datos", "transferidos", "dispositivos", "interceptados"),
    ]

    driver.get(url_formulario)

    print()
    print(f"  {C.YELLOW}{'='*48}{C.RESET}")
    print_status("1. Inicia sesión en Google en la ventana.", "warn")
    print_status("2. Navega hasta ver las preguntas.", "warn")
    print_status("3. Presiona ENTER aquí para ejecutar.", "warn")
    print(f"  {C.YELLOW}{'='*48}{C.RESET}")
    input(f"\n  {C.GREEN}>> ENTER para iniciar <<{C.RESET} ")
    print()

    print_status("Escaneando DOM de Google Forms...", "info")

    elementos = driver.find_elements(
        By.XPATH,
        "//div[@role='radio' or @role='checkbox']/ancestor::label | "
        "//div[@role='radio' or @role='checkbox']/parent::div/parent::div"
    )
    if not elementos:
        elementos = driver.find_elements(By.XPATH, "//div[@role='radio' or @role='checkbox']")

    cache_opciones = []
    for el in elementos:
        texto = limpiar_texto(el.text)
        if texto:
            cache_opciones.append({"elemento": el, "texto": texto, "usado": False})

    print_status(f"Elementos cacheados: {C.CYAN}{len(cache_opciones)}{C.RESET}", "ok")
    print_status("Calculando mejores matches...", "info")
    print()

    marcadas = 0
    no_encontradas = []

    for tupla_keywords in respuestas_keywords:
        mejor_opcion = None
        max_aciertos = 0

        for cache in cache_opciones:
            if cache["usado"]:
                continue
            aciertos_actuales = sum(1 for kw in tupla_keywords if kw in cache["texto"])
            if aciertos_actuales > max_aciertos:
                max_aciertos = aciertos_actuales
                mejor_opcion = cache

        umbral_minimo = 1 if len(tupla_keywords) == 1 else max(1, len(tupla_keywords) * 0.6)

        if mejor_opcion and max_aciertos >= umbral_minimo:
            try:
                el = mejor_opcion["elemento"]
                try:
                    radio = el.find_element(By.XPATH, ".//div[@role='radio' or @role='checkbox']")
                    driver.execute_script("arguments[0].click();", radio)
                except Exception:
                    driver.execute_script("arguments[0].click();", el)

                marcadas += 1
                mejor_opcion["usado"] = True
                kw_preview = str(tupla_keywords[:3])[1:-1]
                print_status(
                    f"{C.GREEN}({max_aciertos}/{len(tupla_keywords)}){C.RESET} {kw_preview}...",
                    "ok"
                )
            except Exception:
                no_encontradas.append(str(tupla_keywords[:2]))
        else:
            no_encontradas.append(str(tupla_keywords[:2]))

    print()
    print(f"  {C.GREEN}{'='*48}{C.RESET}")
    print_status(
        f"Respuestas marcadas: {C.GREEN}{C.BOLD}{marcadas}{C.RESET} / {len(respuestas_keywords)}",
        "ok"
    )
    if no_encontradas:
        print_status(f"No encontradas ({len(no_encontradas)}) — pueden estar en otra página:", "warn")
        for r in no_encontradas:
            print(f"      {C.DIM}{r}{C.RESET}")
    print(f"  {C.GREEN}{'='*48}{C.RESET}")
    print()
    print_status("Revisa el formulario antes de enviar.", "warn")
    input(f"  {C.RED}>> ENTER para cerrar el navegador <<{C.RESET} ")
    driver.quit()

if __name__ == "__main__":
    automatizar_examen()