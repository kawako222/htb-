import socket
from concurrent.futures import ThreadPoolExecutor

target = "10.0.5.4"
# Escanearemos los puertos que salieron "filtered" o sospechosos
ports = [80, 443, 1337, 3000, 4000, 5000, 8000, 8080, 8888, 9000, 9090, 31337]

def check_port(port):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.settimeout(1)
        if s.connect_ex((target, port)) == 0:
            print(f"[*] ¡PUERTO {port} ABIERTO!")

print(f"Probando puertos críticos en {target}...")
with ThreadPoolExecutor(max_workers=20) as executor:
    executor.map(check_port, ports)
