import os
import subprocess
import re
import sys
import argparse
import json

# =========================
# 🎨 Colores Matrix
# =========================
G_DARK = '\033[32m'
G_BRIGHT = '\033[1;32m'
GB = G_BRIGHT 
RB = '\033[1;31m'
W = '\033[0m'
R = '\033[31m'

REPORT_FILE = "reporte_equestria.md"

# =========================
# 🧠 Utilidades
# =========================

def clean_target(target):
    temp = re.sub(r'https?://', '', target)
    return temp.split('/')[0]

def safe_clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def pause():
    input(f"\n{G_DARK}Presiona ENTER para continuar...{W}")

# =========================
# 🎨 Banner Único
# =========================

def banner(target):
    logo = r"""
  ______  ______  __  __  ______  ______  ______  ______  __  ______    
 /\  ___\/\  __ \/\ \/\ \/\  ___\/\  __ \/\  __ \/\  == \/\ \/\  __ \   
 \ \  __\\ \ \/\ \ \ \_\ \ \  __\\ \___  \ \ \/\ \ \  __< \ \ \ \  __ \  
  \ \_____\ \___\_\ \_____\ \_____\/\_____\ \_____\ \_\ \_\ \_\ \_\ \_\\ 
   \/_____/\/__/ \/_/_____/\/_____/\/_____/\/_____/\/_/ /_/\/_/\/_/\/_/ 
    
        ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠋⡏⠄⢲⢁⠂⡌⢐⠡⢒⠈⣌⡰⠔⡚⠡⠛⠿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
        ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⢋⠀⡂⢼⠃⢌⡇⠂⡔⠐⣂⢰⠬⡚⢁⠆⠡⡐⠡⢉⠔⣊⣻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
        ⣿⣿⣿⣿⣿⣿⣿⣿⡿⢟⣿⡿⠊⢄⢂⠱⠀⢾⠡⢼⠠⠑⣨⢖⢕⠃⡐⢠⣡⠬⠒⠎⡩⢉⠂⡔⣀⠊⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
        ⣿⣿⣿⣿⣿⣿⣿⣯⠁⠀⠈⠱⣌⠂⠆⠌⡑⠠⡗⢸⠀⣃⡵⢁⠊⣰⠜⠍⠠⠌⣈⠐⠡⣈⣒⠐⠤⢈⡁⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
        ⣿⣿⣿⣿⣿⣿⣿⣻⠀⡀⠀⠀⠑⢿⠈⠉⠉⠉⠉⠛⠲⠼⣀⢢⠟⡁⠌⣀⠃⢰⡤⢺⡉⠥⠉⣙⣦⣡⠄⢣⢹⣿⣿⣿⣿⣿⣿⣿⣿⣿
        ⣿⣿⣿⣿⣿⡿⡿⣧⠀⢡⠀⠀⠀⠀⠁⠀⠀⠀⠀⠀⠀⠀⠈⠑⢦⡘⡐⣠⣼⣫⣤⣴⣿⣾⣿⣿⣿⣿⡎⠄⡃⢾⣿⣿⣿⣿⣿⣿⣿⣿
        ⣿⣿⣿⣿⣿⡟⢀⢿⡀⠸⡄⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣠⣤⣴⣶⣾⣿⣿⣿⣿⣿⣿⡿⣿⣿⣿⣿⣿⣇⠎⠰⣸⣿⣿⣿⣿⣿⣿⣿⣿
        ⣿⣿⣿⣿⣟⠣⠈⠜⣇⠀⠑⡀⠀⣠⣤⣤⣶⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣻⣿⣿⣿⡯⣐⠡⢸⣿⣿⣿⣿⣿⣿⣿⣿
        ⣿⣿⣿⣿⣟⡎⢡⠈⠜⣆⢀⣴⣿⣿⣿⣿⣿⣿⣿⣿⣯⣿⡾⣟⣿⣿⣿⣿⡏⢿⣿⣿⣿⣿⣿⣽⣿⣿⢇⠉⢗⡸⣽⣿⣿⣿⣿⣿⣿⣿
        ⣿⣿⣿⣿⣿⣵⢀⣊⣴⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣽⣿⣿⣿⣿⣿⡇⠈⢻⣿⣿⣿⣿⣿⣾⢏⠞⠀⠈⢛⣿⣿⣿⣿⣿⣿⣿⣿
        ⣿⣿⣿⣿⣿⣦⣷⣿⣿⣿⣿⢿⠟⠛⠉⢻⣿⣿⣿⣿⣿⣿⣿⣷⣿⢿⣿⡿⠀⠀⠀⠘⠋⠹⡟⠫⠕⠁⠀⠀⠀⠀⢚⢿⣿⣿⣿⣿⣿⣿
        ⣿⣿⣿⣿⣿⣿⣿⣿⣿⢁⠢⡘⢧⠀⠀⠀⠙⢿⣿⣿⣿⣿⣿⣿⣿⣿⡟⠁⠀⠀⠀⠒⠂⢠⡿⣄⠀⠀⠀⠀⠀⠀⠀⢫⢿⣿⣿⣿⣿⣿
        ⣿⣿⣿⣿⣿⣿⣿⣿⣿⠘⡠⠐⠌⢧⡀⠀⠀⠀⠙⠻⢿⣿⣿⡿⠟⠉⠀⠀⠀⠠⠤⠴⡲⡝⢠⠘⣧⡀⠀⠀⠀⠀⠀⠀⠩⢿⣿⣿⣿⣿
        ⣿⣿⣿⣿⣿⣿⣿⣝⢄⠳⡠⢁⠊⠄⠳⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣔⠮⡊⠔⡡⣸⠡⢙⣦⡀⠀⠀⠀⠀⠀⠑⡿⣿⣿⣿
        ⣿⣿⣿⣿⣿⣿⣿⣿⣎⢣⡙⢆⡈⠤⠁⠜⢳⡀⠀⠀⠀⠤⠤⠤⠤⠖⠒⢺⠛⠩⠐⣀⠒⠠⣱⠣⠑⣠⣞⠟⢦⡀⠀⠀⠀⠀⢰⣿⣿⣿
        ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣆⠱⣌⠱⣆⠉⡄⠡⠘⠦⣄⠀⠀⠀⠀⠀⠀⠀⠸⣇⢃⠡⠄⠌⢢⣧⠶⠟⠉⠀⠀⠀⠈⠀⠀⢀⣴⣽⣿⣿⣿
        ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣄⢈⠲⡈⠳⣌⠤⢉⠰⠈⠷⣄⠀⠀⠀⠀⠀⠀⠙⢧⣢⠼⠚⠉⠁⠀⠀⠀⠀⠀⠀⢀⣠⣮⣿⣿⣿⣿⣿⣿
        ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣄⢈⠲⡈⠳⣌⠤⢉⠰⠈⠷⣄⠀⠀⠀⠀⠀⠀⠙⢧⣢⠼⠚⠉⠁⠀⠀⠀⠀⠀⠀⢀⣠⣮⣿⣿⣿⣿⣿
        ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣆⠐⡑⢆⠄⠳⣌⠢⡁⠆⡉⠷⣄⠀⠀⠀⠀⠀⠀⠙⠦⡀⠀⠀⠀⠀⠀⣀⢤⣦⣿⣿⣿⣿⣿⣿⣿⣿⣿
        ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣟⢦⢀⠉⠳⡐⢠⠓⣔⢂⠰⢀⠉⠷⣄⠀⠀⠀⠀⠀⠈⢻⢤⡤⢶⣮⣿⣿⣿⢿⣡⣦⣀⠙⢿⣿⣿⣿⣿
        ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣯⠘⢝⡈⢧⡈⠤⠙⣢⡒⢈⠳⣔⠈⠤⠑⡘⢦⡀⠀⠀⠀⠀⠀⢛⡆⣸⢿⣿⣿⣯⣿⣿⣿⣿⠈⠆⣿⣿⣿⣿
        ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣧⡃⠀⢇⠀⠻⣄⠥⢀⡑⣆⠂⠌⡳⣂⠡⠐⣈⠳⣴⠀⠀⠀⠀⠀⢿⡸⡘⢿⣿⣿⣿⣿⣿⡟⢈⠐⣿⣿⣿⣿
        ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡴⡀⠘⡄⣰⠟⢦⡂⡔⢈⢮⠐⡄⡙⣆⠥⢀⠡⠹⣧⠀⠀⠀⠀⢸⢇⢇⢂⠙⠻⠿⠿⢋⠐⡀⢺⣽⣿⣿⣿
        ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡵⢠⡟⠁⠀⠀⠳⣌⠂⢂⢳⠠⠁⠌⢧⠊⠰⠁⢻⡆⠀⠀⠀⠈⢼⠸⡌⠂⠡⠘⠠⠃⣢⣼⣿⣿⣿⣿⣿
    
    """
    print(f"{GB}{logo}{W}")
    print(f" {GB}Target:{W} {RB}{target}{W}")
    print(f"{G_DARK}" + "-" * 60 + f"{W}")


# =========================
# 📖 Help
# =========================

def show_help():
    print(f"""{GB}
E Q U E S T R I A  F R A M E W O R K
{W}
Uso:
  python3 equestria.py
  python3 equestria.py -h

Módulos:

[1] Editar Hosts
    Abre /etc/hosts para agregar dominios manualmente.

[2] DNS Dig
    Enumeración DNS básica con dig.

[3] Crawling
    Ejecuta spider básico contra el target.

[4] WhatWeb + Headers
    Detecta tecnologías y muestra headers HTTP.

[5] FFUF Subs/Vhosts
    Enumeración de subdominios y virtual hosts.
    ✔ Incluye recursividad automática.
    ✔ Guarda resultados en JSON.
    ✔ Muestra solo hallazgos.

[6] FFUF Dirs
    Fuzzing de directorios.
    ✔ Solo muestra códigos interesantes.
    ✔ Guarda JSON.
    ✔ Modo limpio tipo nmap.

[7] Extract Common Files
    Busca robots.txt, .env, etc.

[8] Nmap Scan
    Escaneo completo con scripts y versiones.
""")
    sys.exit()


# =========================
# ⚙️ Wordlists
# =========================

def get_wordlist():
    print(f"\n{G_BRIGHT}[!] Selecciona tu Wordlist:{W}")
    print(" 1. Common (4k)")
    print(" 2. Web extensions")
    print(" 3. Dirbuster Medium")
    print(" 4. Subs 110k")
    print(" 5. Subs 20k")
    print(" 6. Subs 50k")

    choice = input(f"\n{G_BRIGHT}wordlist > {W}").strip()

    paths = {
        "1": "/usr/share/wordlists/dirb/common.txt",
        "2": "/usr/share/seclists/Discovery/Web-Content/web-extensions-big.txt",
        "3": "/usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt",
        "4": "/usr/share/seclists/Discovery/DNS/subdomains-top1million-110000.txt",
        "5": "/usr/share/seclists/Discovery/DNS/subdomains-top1million-20000.txt",
        "6": "/usr/share/seclists/Discovery/DNS/subdomains-top1million-50000.txt"
    }

    return paths.get(choice, paths["1"])

# =========================
# 🚀 FFUF limpio
# =========================

def run_ffuf_clean(cmd, output_file):
    print(f"\n{GB}[*] Ejecutando FFUF...{W}\n")

    subprocess.run(cmd, shell=True)

    if os.path.exists(output_file):
        with open(output_file, "r") as f:
            data = json.load(f)

        print(f"\n{GB}=== RESULTADOS ==={W}\n")

        for r in data.get("results", []):
            print(f"{GB}{r['status']}  {r['url']}{W}")

        print(f"\n{GB}Total encontrados: {len(data.get('results', []))}{W}")

    else:
        print(f"{R}No se generó archivo de resultados.{W}")




# =========================
# 📋 Menú principal
# =========================
def menu():
    # Pedimos el target una sola vez al inicio
    target_raw = input(f"{GB}[?] Ingrese el objetivo (IP o URL): {W}").strip()

    if not target_raw:
        print(f"{R}Objetivo inválido.{W}")
        return # Usamos return para salir de la función de forma limpia

    target_clean = clean_target(target_raw)
    # Aseguramos que target_url tenga el protocolo para curl/ReconSpider
    target_url = target_raw if target_raw.startswith("http") else f"http://{target_clean}"

    while True:
        safe_clear()
        banner(target_clean)

        print(f" {G_DARK}[1]{W} Editar Hosts          {G_DARK}[5]{W} FFUF Subs/Vhosts")
        print(f" {G_DARK}[2]{W} DNS Dig               {G_DARK}[6]{W} FFUF Dirs")
        print(f" {G_DARK}[3]{W} ReconSpider Crawl     {G_DARK}[7]{W} Extract Common Files")
        print(f" {G_DARK}[4]{W} WhatWeb + Headers     {G_DARK}[8]{W} Nmap Scan")
        print(f" {G_DARK}[0]{W} Salir")

        choice = input(f"\n{GB}equestria > {W}").strip()

        if choice == "1":
            os.system("sudo nano /etc/hosts")

        elif choice == "2":
            # Usamos target_clean para herramientas de red
            os.system(f"dig {target_clean} ANY")
            pause()

        elif choice == "3":
            # Usamos target_url para la araña
            os.system(f"python3 ReconSpider.py {target_url}")
            pause()

        elif choice == "4":
            os.system(f"whatweb {target_url} && curl -I -s {target_url}")
            pause()

        elif choice == "5":
            # Corregido: Llamada sin argumentos o con lógica de filtrado
            w = get_wordlist() 
            output = "subs_results.json"
            # Comando FFUF para VHOSTS
            cmd = f'ffuf -s -w {w} -u {target_url} -H "Host: FUZZ.{target_clean}" -mc 200,301,302,403 -of json -o {output}'
            run_ffuf_clean(cmd, output)
            pause()

        elif choice == "6":
            w = get_wordlist()
            port = input(f"{GB}[?] Puerto (80): {W}").strip() or "80"
            
            # TRUCO: Primero detectamos el tamaño de un 404 para filtrarlo
            print(f"{GB}[*] Detectando tamaño de página de error...{W}")
            check_404 = f"curl -s -o /dev/null -w '%{{size_download}}' http://{target_clean}:{port}/archivo_inexistente_axmi"
            bad_size = subprocess.getoutput(check_404)
            print(f"{G_DARK}[!] Filtrando respuestas de tamaño: {bad_size}{W}")

            output = "dir_results.json"
            # Añadimos -fs {bad_size} para que no te salgan los falsos positivos
            cmd = f'ffuf -s -w {w} -u http://{target_clean}:{port}/FUZZ -mc 200,301,302,403 -fs {bad_size} -of json -o {output}'
            run_ffuf_clean(cmd, output)
            pause()

        elif choice == "7":
            print(f"{GB}[*] Extrayendo archivos...{W}")
            for f in ["robots.txt", "sitemap.xml", ".env", ".git/config"]:
                print(f"{G_DARK}--- {f} ---{W}")
                os.system(f"curl -s {target_url}/{f}")
            pause()

        elif choice == "8":
            os.system(f"nmap -sC -sV -p- {target_clean}")
            pause()

        elif choice == "0":
            print(f"{GB}Saliendo del Framework... ¡Yay!{W}")
            break

        else:
            print(f"{R}Opción inválida.{W}")
            pause()

# =========================
# 🚀 MAIN
# =========================

if __name__ == "__main__":
    # Verificamos si se pidió ayuda antes de lanzar el menú
    parser = argparse.ArgumentParser(add_help=False)
    parser.add_argument("-h", "--help", action="store_true")
    args, unknown = parser.parse_known_args() # Ignora argumentos que no sean -h

    if args.help:
        show_help()

    try:
        menu()
    except KeyboardInterrupt:
        print(f"\n{R}[!] Interrumpido por el usuario. Cerrando Equestria...{W}")
        sys.exit(0)