# Writeup: Social Media Investigation Hub

**Categoría:** OSINT (Open Source Intelligence)

**Nivel:** Principiante / Intermedio

**Plataformas Analizadas:** ChirpNet (Twitter), ConnectPro (LinkedIn), ForumHub (Reddit)

## 1. Resumen del Reto

Una empresa tecnológica reportó una campaña de desprestigio coordinada contra su nuevo producto, el **XyloPhone Pro**. Nuestra misión como analistas OSINT fue investigar el rastro digital del usuario **"TechReviewer2024"** a través de tres redes sociales simuladas para descubrir su verdadera identidad, sus motivos y exponer la campaña de sabotaje.

## 2. Recolección de Inteligencia (Paso a Paso)

A través de la correlación cruzada de perfiles en las tres plataformas, pudimos responder a las interrogantes clave del incidente:

### Fase 1: Identificación del Objetivo (ConnectPro)

La plataforma orientada a lo profesional fue el eslabón más débil en la seguridad operacional (OPSEC) del atacante.

* **Nombre Real (Q1):** Al revisar el titular profesional de la cuenta, descubrimos que el nombre detrás del alias es **Alex Morgan**.
* **Motivación y Nexos (Q2):** En la sección de experiencia laboral, notamos que Alex trabajó como *Marketing Specialist* en **RivalTech Inc.** (desde enero de 2021 hasta diciembre de 2023). Esto expuso un claro conflicto de intereses, apuntando a un sabotaje corporativo por parte de un competidor directo.
* **Educación (Q7):** Se graduó de la **University of California, Berkeley** con un *Bachelor of Science in Marketing* (2017-2021).
* **Análisis de Credibilidad (Q8):** Su perfil cuenta con apenas **89 conexiones**. Un número inusualmente bajo para alguien que dice ser un "revisor profesional de tecnología", lo que nos indicó que la cuenta profesional podría ser una fachada reciente.

### Fase 2: Descubrimiento de la Campaña (ForumHub)

Al analizar la actividad del usuario en foros, encontramos la evidencia irrefutable de la coordinación del ataque.

* **Producto Objetivo (Q5):** Un post del usuario reveló instrucciones exactas para dejar reseñas negativas sobre el **XyloPhone Pro**.
* **Nombre Clave de la Operación (Q3):** En el post titulado *"XyloPhone Pro Campaign Coordination"*, el atacante cometió el error de escribir el nombre interno de la campaña: **operation_social_storm_2024**.
* **Nivel de Influencia (Q6):** Para dar peso a sus críticas, Alex logró infiltrarse y obtener el rol de **Moderador** en el subreddit `r/TechReviews`.
* **Actividad Anómala (Q9):** La cuenta acumuló rápidamente **1,247 puntos de Post Karma**, demostrando un esfuerzo intensivo por inflar la reputación de la cuenta en muy poco tiempo para ganar legitimidad.

### Fase 3: Análisis de la Red de Bots (ChirpNet)

* **Cronología del Ataque (Q4):** Al revisar la lista de *Siguiendo* (Following) en la red de microblogging, notamos un patrón: casi todas las cuentas sospechosas (como `@ReviewMaster_Bob` y `@TechTruth_Sally`) comenzaron a ser seguidas y fueron creadas alrededor de **Febrero de 2024**, confirmando que se trata de una granja de cuentas (sockpuppets) coordinada.

## 3. Conclusión y Flag Final

El análisis OSINT demostró exitosamente que "TechReviewer2024" no es un consumidor insatisfecho, sino un ex-empleado de una compañía rival (RivalTech Inc.) ejecutando una campaña de difamación organizada llamada *Operation Social Storm*.

Al recopilar todas las piezas de inteligencia, el sistema valida la investigación y nos otorga la bandera:

**Flag:** `HTB{alexmorgan_operationsocialstorm2024_february2024}`

---


Este reto es un ejemplo perfecto de cómo funciona el análisis de amenazas reales. El atacante hizo un buen trabajo creando contenido que "parecía" auténtico, pero falló en su **OPSEC** al reciclar su alias ("TechReviewer2024") y conectarlo con su perfil profesional real de LinkedIn. En ciberseguridad, los atacantes solo necesitan cometer un error para que todo su castillo de naipes se derrumbe. ¡Excelente investigación!
