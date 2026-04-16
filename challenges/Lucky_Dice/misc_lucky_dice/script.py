from pwn import *
import re

context.log_level = 'info'

def solve():
    target_ip = '154.57.164.72'
    target_port = 32321

    io = remote(target_ip, target_port)

    try:
        io.recvuntil(b"Are you ready?\n")
        io.recvuntil(b"2. No\n")
        io.sendline(b"1")
        io.recvuntil(b"Go!\n")

        log.info("Conectado, iniciando rondas...")

        for i in range(100):
            # Recibir solo hasta "Who wins this round?\n"
            # En este punto YA tenemos todos los dados — calculamos y enviamos
            # ANTES de que el servidor imprima la lista de jugadores
            data = io.recvuntil(b"Who wins this round?\n", timeout=10).decode()

            # Calcular ganador
            player_data = re.findall(r"Player (\d+): ([\d ]+)", data)
            scores = {}
            for p_id, dice_str in player_data:
                scores[int(p_id)] = sum(map(int, dice_str.strip().split()))

            if not scores:
                print(f"[!] Sin jugadores en ronda {i+1}: {repr(data)}")
                break

            winner = sorted(scores.keys(), key=lambda k: scores[k])[-1]

            # PIPELINE: enviar respuesta AHORA, mientras el servidor
            # todavía está imprimiendo la lista de jugadores con sus sleeps.
            # El servidor llama input("> ") DESPUÉS de imprimir la lista,
            # pero nuestro dato ya estará en el buffer TCP esperando.
            io.sendline(str(winner).encode())

            # Ahora consumir la lista + prompt + resultado (ya llegaron o llegarán pronto)
            res = io.recvuntil([b"Yes.. Correct!", b"too slow", b"corrupted"], timeout=10).decode()

            if "too slow" in res or "CPU" in res:
                print(f"[!] Demasiado lento en ronda {i+1}")
                break
            elif "corrupted" in res or "off" in res:
                print(f"[!] Incorrecto en ronda {i+1} — winner={winner}, scores={scores}")
                break
            elif "Yes.. Correct!" in res:
                if (i + 1) % 10 == 0:
                    log.success(f"Ronda {i+1}/100 ✓")
            else:
                print(f"[?] Inesperado en ronda {i+1}: {repr(res)}")
                break

        log.success("¡Listo! Recibiendo flag...")
        final = io.recvall(timeout=5).decode()
        print("\n" + final)

    except Exception as e:
        print(f"[!] Error: {e}")
        import traceback
        traceback.print_exc()
    finally:
        io.close()

if __name__ == "__main__":
    solve()
