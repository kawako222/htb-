## Enumeration (Enumeración)

**La enumeración es la fase más crítica del hacking.**  
No se trata de “entrar” al sistema, sino de **descubrir TODAS las formas posibles de atacarlo**.

> Acceder al sistema suele ser fácil… **cuando ya sabes cómo hacerlo**.

---

## 🧠 Idea clave

- Las herramientas **no hackean por ti**
    
- Sirven **solo si sabes interpretar lo que te devuelven**
    
- La enumeración es **conocimiento + observación + contexto**
    

👉 Las tools son un **medio**, no el objetivo.

---

## 🎯 Objetivo de la enumeración

Recolectar **la mayor cantidad de información posible**, porque:

> **Más información = más vectores de ataque**

La enumeración busca principalmente:

1. **Funciones o recursos** que permitan interactuar con el objetivo
    
2. **Información sensible** que facilite el acceso al sistema
    

---

## 🧩 Analogía rápida

- ❌ “Las llaves están en la sala”
    
- ✅ “Las llaves están en la sala, en el estante blanco, tercer cajón”
    

👉 **La precisión lo es todo**

---

## 🔌 ¿Qué se enumera?

- Servicios expuestos (HTTP, SMB, LDAP, SSH, etc.)
    
- Versiones y configuraciones
    
- Usuarios, rutas, permisos
    
- Errores, banners, respuestas inesperadas
    
- **Misconfigurations** (configuraciones incorrectas)
    

---

## ⚠️ Errores comunes de seguridad

La mayoría de la info viene de:

- Configuraciones incorrectas
    
- Negligencia
    
- Falsa confianza en:
    
    - Firewalls
        
    - GPOs
        
    - Updates automáticos
        

👉 **Seguridad por capas mal implementada = info leak**

---

## 🛠️ Herramientas ≠ Enumeración

Muchas personas se quedan atoradas porque:

- “Ya corrí todas las tools”
    
- Pero **no saben cómo funciona el servicio**
    
- No saben **qué es relevante**
    

📌 Aprender **cómo funciona un servicio** ahorra horas o días.

---

## 🧑‍💻 Enumeración manual (MUY importante)

- Las tools automatizan y aceleran
    
- Pero **no siempre evaden protecciones**
    
- La enumeración manual:
    
    - Detecta comportamientos raros
        
    - Permite bypasses
        
    - Revela lógica interna
        

