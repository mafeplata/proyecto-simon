# ⚖️🤖 Proyecto Final — Derecho e Inteligencia Artificial

**Pontificia Universidad Javeriana · 2026-II · Docente: Pedro Ardila**

> **Estudiante:** Simón Andrés Contreras Palma 
> **Nombre del proyecto:** REVISOR DE CONTRATOS SIMPLES
> **Fecha de inicio:** 18/08/2026

---

Bienvenido/a a tu repositorio de proyecto. **Este archivo es tu tablero de mando**: aquí describes tu proyecto, planificas su desarrollo y dejas evidencia del avance. Lo vas a completar por partes, siguiendo el curso.

📌 Si ya habías escrito una descripción de tu proyecto cuando creaste el repo, la encuentras intacta en `README-ORIGINAL.md`. Úsala como punto de partida para la Parte 1 — no empieces de cero.

**No necesitas saber programar.** Todo el código lo construirás con asistencia de IA (*vibe coding*). Tu valor como estudiante de derecho está en el problema que eliges, las fuentes que alimentas, las instrucciones que diseñas y el juicio crítico con el que evalúas el resultado.

---

## 📋 Parte 1 — Descripción del proyecto

> Completa cada sección con 3–10 frases. Sé concreto/a: esta descripción es la que tu IA usará como contexto y la que el docente usará para realimentarte.

### 1.1 El problema jurídico
¿Qué problema **real del derecho colombiano** resuelve tu herramienta? ¿Quién lo sufre hoy y cómo lo resuelve sin tu herramienta?
Las personas que firman contratos sencillos de arrendamiento o de prestación de servicios muchas veces no identifican cláusulas abusivas, riesgosas, ambiguas o elementos importantes que hacen falta en el contrato. Esto puede generar conflictos posteriores sobre pagos, terminación, obligaciones, responsabilidades o incumplimientos. Actualmente, una persona sin conocimientos jurídicos debe revisar el contrato por su cuenta o pagar una asesoría para identificar estos riesgos. La herramienta busca ofrecer una primera revisión orientativa basada en una lista de verificación jurídica colombiana. No reemplaza la asesoría de un abogado, pero permite detectar problemas básicos antes de firmar.

### 1.2 Usuarios
¿Quién va a usarla? Describe a tu usuario ideal en una frase (ej. *"un arrendatario bogotano que le subieron el canon de arrendamiento más del límite legal"*). Recuerda que al final necesitas **al menos un usuario real** que la pruebe.
El usuario ideal es una persona en Colombia que está a punto de firmar un contrato sencillo de arrendamiento de vivienda o de prestación de servicios y quiere identificar posibles riesgos antes de firmarlo. También puede ser utilizado por estudiantes, pequeños arrendadores, trabajadores independientes o personas que contratan servicios. El usuario debe poder cargar o copiar el texto del contrato en la herramienta.

### 1.3 Qué hace y qué NO hace (alcance)
| ✅ Sí hace | ❌ No hace |
| --- | --- |
| [Identifica cláusulas potencialmente riesgosas, ambiguas o faltantes.] | [No reemplaza la asesoría de un abogado.] |
| [Señala aspectos que el usuario debería revisar antes de firmar.] | [No representa al usuario ante jueces, autoridades o particulares.] |

*Consejo de abogado: un alcance pequeño y perfecto vale más que uno grande y roto.*

### 1.4 Marco jurídico y fuentes
¿Qué normas alimentan tu herramienta? Lista tu corpus normativo (leyes, decretos, sentencias — debe ser **pequeño y público**):
- [x] Norma 1: Ley 820 de 2003 — Régimen de arrendamiento de vivienda urbana. http://www.secretariasenado.gov.co/senado/basedoc/ley_0820_2003.html
- [x] Norma 2: Código Civil colombiano — artículos sobre arrendamiento (Arts. 1985, 1601, 1602). http://www.secretariasenado.gov.co/senado/basedoc/codigo_civil.html

### 1.5 Nombre y lema
CONTRATO CHECK
“Revisa. Detecta. Decide.”
---

## 🗺️ Parte 2 — Plan de desarrollo

Marca cada hito cuando lo termines. Los hitos siguen las sesiones del curso.

- [x] **M0 — Descripción y plan** *(con Sesión 1)*: Partes 1 y 2 de este README completas.
- [x] **M1 — Asistente con instrucciones v1** *(Sesión 1–2)*: Prompt de sistema redactado y documentado en la Parte 5. Funciona en ChatGPT, Claude y Gemini.
- [x] **M2 — Casos de prueba documentados** *(Sesión 2)*: 5 casos de prueba documentados y superados con éxito en `docs/casos-de-prueba.md` (más 1 caso de control de falsos positivos).
- [x] **M3 — Corpus conectado (RAG / Motor Normativo)** *(Sesión 3)*: corpus normativo cargado en `corpus/` con Ley 820 de 2003 y Código Civil colombiano. La herramienta cita la fuente normativa en cada hallazgo.
- [x] **M4 — Interfaz web y aplicación funcional** *(Sesión 4)*: desarrollada en **Python con Streamlit** (`app.py`, `requirements.txt`) y con interfaz web complementaria en HTML5/CSS/JS (`index.html`, `styles.css`, `app.js`). Pendiente activar URL pública.
- [x] **M5 — Análisis crítico y demo** *(Sesión 5)*: Parte 7 completada con análisis crítico honesto sobre las limitaciones de la herramienta.

### Bitácora de avance semanal
| Semana | Qué hice | Enlace/captura | Dudas para la clase |
| --- | --- | --- | --- |
| 1 | Definí el problema jurídico, los usuarios y el alcance del proyecto. Elegí el nombre CONTRATO CHECK y el lema. | Parte 1 del README | |
| 2 | Redacté el prompt de sistema y documenté los 5 casos de prueba obligatorios en `docs/casos-de-prueba.md`. | Parte 5 del README y `docs/` | |
| 3 | Construí el corpus normativo: Ley 820 de 2003 (Arts. 16, 20, 22, 24) y Código Civil (Arts. 1601, 1985). Subí archivos a `corpus/`. | Carpeta `corpus/` en el repo | |
| 4 | Desarrollé la aplicación principal en **Python usando Streamlit (`app.py`)** con su motor de análisis normativo y `requirements.txt`, junto a la interfaz web complementaria (`index.html`, `styles.css`, `app.js`). | Archivos en la raíz del repo | Despliegue en Streamlit Cloud / Vercel |
| 5 | Completé el análisis crítico (Parte 7) y los entregables finales (Parte 8). | Partes 7 y 8 del README | |

---

## 🛠️ Parte 3 — Stack técnico implementado (Desarrollado en Python)

El núcleo de **CONTRATO CHECK** fue desarrollado en **Python** como lenguaje principal del proyecto, aprovechando su ecosistema para procesamiento de texto, análisis normativo estructurado y visualización ágil.

```
[Usuario]
   │
   ▼ (Pega contrato o selecciona tipo)
[Interfaz interactiva en Python — Streamlit (app.py)]
   │
   ▼ (Extracción de cláusulas y contraste de reglas)
[Motor de Análisis Normativo en Python] ⟷ [Corpus Colombiano: Ley 820 / Código Civil (corpus/)]
   │
   ▼ (Cálculo ponderado de riesgo y citas legales exactas)
[Diagnóstico Jurídico Visual: Semáforo de Riesgo + Alertas + Cláusulas Faltantes + Consejos de Negociación]
```

### Componentes de la solución implementada

| Componente | Tecnología implementada | Función en CONTRATO CHECK |
|---|---|---|
| **Lenguaje Core** | **Python (>=3.9)** | Lenguaje principal del proyecto. Ejecuta la lógica jurídica, la validación de condiciones de validez contractual y el cálculo ponderado del índice de riesgo. |
| **Aplicación e Interfaz** | **Streamlit (`app.py`)** | Framework de Python que genera una interfaz web interactiva, moderna y con modo oscuro para cargar o subir contratos (.txt, .pdf, .docx), ejecutar el análisis en tiempo real y mostrar estadísticas visuales. |
| **Dependencias** | **`requirements.txt`** | Archivo estándar de Python con las dependencias del proyecto (`streamlit>=1.28.0`, `pypdf>=3.17.0`) para instalación inmediata con `pip install -r requirements.txt`. |
| **Motor de Análisis Normativo** | **Python Scripting (`analizar_contrato`)** | Escáner algorítmico en Python que contrasta el texto del contrato con las disposiciones prohibitivas y obligatorias de la legislación colombiana (depósitos, topes de IPC, preavisos, reparaciones y penalidades). |
| **Corpus Jurídico** | **Markdown en `corpus/`** | Repositorio estructurado de fuentes normativas públicas colombianas: Ley 820 de 2003 (régimen de vivienda urbana) y Código Civil (obligaciones y arrendamiento). |
| **Cliente Web Alternativo** | **HTML5 + CSS3 + JS (`index.html`, `app.js`, `styles.css`)** | Versión complementaria basada en navegador cliente para facilitar ejecución estática sin servidor y despliegue alternativo en Vercel. |
| **Privacidad y Datos** | **Procesamiento Local (Ley 1581 de 2012)** | Al procesar los contratos localmente mediante Python sin recurrir a APIs externas opacas, se garantiza que ningún dato confidencial o personal sea almacenado ni transferido a terceros. |

> 💡 **¿Por qué se eligió Python?** Python permite construir una herramienta jurídica determinista, confiable y auditable. Evita "alucinaciones" de leyes extranjeras, opera sin costos de consumo por tokens de APIs y garantiza estricta confidencialidad en el tratamiento de los contratos de los usuarios.

---

## 🚀 Parte 4 — Ruta de despliegue

Tu meta: **una URL pública** que cualquiera pueda abrir. Elige una ruta:

### Opción A — Streamlit Community Cloud ⭐ (Recomendada para la versión Python)
1. El proyecto cuenta con `app.py` y `requirements.txt` listos en la raíz del repositorio.
2. Inicia sesión gratis en [share.streamlit.io](https://share.streamlit.io/) vinculando tu cuenta de GitHub.
3. Haz clic en **"New app"** → selecciona tu repositorio → archivo principal: `app.py`.
4. Haz clic en **Deploy**: en menos de 2 minutos tu app Python estará pública en la nube con URL gratuita.
- ✅ Ideal para Python y Streamlit · 100% gratuito · sin servidor que configurar.

### Opción B — Vercel (Para el cliente web estático alternativo)
1. Sube tu código a este repo de GitHub (incluye `index.html`, `styles.css`, `app.js` y `vercel.json`).
2. Conecta tu cuenta en [vercel.com](https://vercel.com) con tu GitHub.
3. "Add New Project" → importa tu repo → Deploy.
- ✅ Despliegue estático ultra rápido sin backend.

### Checklist de despliegue ✅
- [x] Código listo en el repo: `app.py`, `requirements.txt`, `index.html`, `styles.css`, `app.js`, `vercel.json` y corpus normativo.
- [x] La advertencia legal obligatoria es **visible** en la parte superior de la interfaz (tanto en Python como en Web).
- [x] No hay API keys ni secretos en el código (procesamiento local seguro y privado).
- [ ] URL pública funciona en el navegador de otra persona — pendiente activación en Streamlit Cloud / Vercel.
- [ ] Anota la URL aquí: **`[pegar URL pública aquí cuando esté activa]`**

> El dominio propio (.com, .co) **no es necesario** — la URL gratuita de Streamlit Community Cloud o Vercel es suficiente para el curso.

---

## 🧠 Parte 5 — Guía de prompting para *vibe coding*

Tu competencia más transferible a la práctica profesional: **instruir bien a la IA**. Reglas:

1. **Un hito a la vez.** No le pidas "hazme todo el proyecto". Pide: "vamos por M1".
2. **Da contexto jurídico, recibe código.** Pega tu Parte 1 y dile: "eres mi ingeniero, yo soy el abogado del proyecto".
3. **Pide explicaciones.** "Explícame como a alguien que no sabe programar qué acabas de hacer."
4. **Commits frecuentes.** Cada vez que algo funcione, guarda los cambios en GitHub. Si rompes algo, siempre puedes volver atrás.
5. **Nunca pegues datos personales reales** de usuarios en el chat ni en el código (Ley 1581).
6. **Verifica como abogado.** Toda respuesta legal que dé la herramienta, contrástala con la norma. Tú respondes por lo que publicas.

### Prompt de sistema de CONTRATO CHECK (M1 — completado ✅)

El siguiente es el prompt de sistema que guía a la herramienta al analizar contratos:

> Eres CONTRATO CHECK, una herramienta de asistencia jurídica orientativa para Colombia, desarrollada como ejercicio académico en la Pontificia Universidad Javeriana.
>
> Tu función es analizar el texto de contratos sencillos de arrendamiento de vivienda urbana o prestación de servicios que el usuario te comparte, e identificar:
>
> 1. **CLÁUSULAS ILEGALES O NULAS:** Aquellas que violan expresamente normas colombianas (Ley 820 de 2003, Código Civil). Ejemplo: exigir depósito en dinero en arrendamiento de vivienda (prohibido por Art. 16, Ley 820/2003).
> 2. **CLÁUSULAS RIESGOSAS O ABUSIVAS:** Aquellas que generan un desequilibrio grave en contra del usuario. Ejemplo: cláusulas penales desproporcionadas, terminación sin preaviso.
> 3. **CLÁUSULAS AMBIGUAS:** Redacción confusa que puede interpretarse de formas contradictorias y generar conflictos.
> 4. **CLÁUSULAS ESENCIALES FALTANTES:** Elementos que la ley exige o que son indispensables para proteger al usuario y que no aparecen en el contrato.
>
> **REGLAS:** Cita siempre la norma jurídica específica (artículo y ley). Si no tienes norma que respalde un hallazgo, dilo explícitamente. Nunca inventes leyes ni artículos. Al final de cada análisis incluye siempre: *"⚠️ Este análisis es un ejercicio académico y NO constituye asesoría legal. Consulta con un abogado antes de firmar."*
>
> Organiza tu respuesta en secciones: 🚨 Alertas críticas / ⚠️ Riesgos / ℹ️ Cláusulas faltantes / 💡 Recomendaciones para negociar.
>
> **Corpus normativo:** Ley 820 de 2003, Código Civil colombiano, Código de Comercio.

---

## ⚖️ Parte 6 — Ética, datos y responsabilidad

Estas salvaguardas son **obligatorias** y hacen parte de la evaluación:

- **Advertencia visible obligatoria.** La interfaz muestra en la parte superior de la pantalla, en un banner de color naranja permanente:
  > *"Esta herramienta es un ejercicio académico del curso de Derecho e Inteligencia Artificial de la Pontificia Universidad Javeriana. No constituye asesoría legal ni sustituye la consulta con un abogado titulado."*
  - [x] Implementada y visible en la interfaz
- **Protección de datos (Ley 1581 de 2012).** La herramienta no recolecta ni almacena datos personales reales. No tiene base de datos ni registro de usuarios. El análisis ocurre en el navegador del usuario y no se transmite ninguna información a servidores externos. Los contratos de prueba utilizan datos ficticios.
  - [x] Verificado: no guardo datos personales
- **Corpus público.** Todas las fuentes utilizadas son públicas: Ley 820 de 2003 (Diario Oficial) y Código Civil colombiano (Secretaría del Senado). No se usan fuentes privadas ni datos reservados.
  - [x] Verificado
- **Anti-alucinaciones.** El asistente está instruido explícitamente para citar la norma jurídica específica en cada hallazgo y para decir "No encuentro una norma específica sobre esto" cuando no tiene respaldo normativo. Nunca debe inventar leyes ni artículos.
  - [x] Verificado: la herramienta cita artículo y ley en cada hallazgo y admite cuando no tiene fuente

---

## 🔍 Parte 7 — Análisis crítico (insumo de mi sustentación final)

### 1. ¿Dónde falla mi herramienta?

**Situación 1 — Contratos con lenguaje técnico o inusual:**
La herramienta detecta riesgos buscando patrones de palabras clave en el texto (como "depósito", "reajuste" o "terminación inmediata"). Si un contrato usa lenguaje técnico o redacción inusual para expresar la misma cláusula abusiva, la herramienta puede no detectarla. Por ejemplo, si un contrato dice "el locatario constituirá una garantía dineraria" en lugar de "el arrendatario pagará un depósito en dinero", el sistema podría no identificarlo como una violación al Artículo 16 de la Ley 820 de 2003.

**Situación 2 — Contratos de tipos no previstos:**
La herramienta fue diseñada para contratos de arrendamiento de vivienda urbana y prestación de servicios simples. Si un usuario carga un contrato de compraventa, una promesa de contrato, un acuerdo de confidencialidad o un contrato laboral, el análisis será superficial e impreciso, ya que las reglas jurídicas que los rigen son completamente diferentes.

### 2. ¿Qué datos procesa mi herramienta?

- **Qué entra:** El texto del contrato que el usuario pega directamente en la interfaz web, y el tipo de contrato seleccionado (arrendamiento o servicios).
- **Qué se guarda:** Nada. La herramienta no tiene base de datos ni servidor propio. El análisis ocurre en el navegador y no se transmite ni almacena ninguna información.
- **Qué sale:** Un diagnóstico con nivel de riesgo (alto/medio/bajo), listado de hallazgos con citas normativas específicas y recomendaciones para negociar antes de firmar.

### 3. ¿Por qué no reemplaza al abogado?

CONTRATO CHECK es una herramienta orientativa que identifica patrones de riesgo basados en reglas predefinidas, pero no puede ejercer el juicio profesional que requiere el derecho. Un abogado no solo conoce la ley, sino que la interpreta en contexto: evalúa la capacidad de las partes, la validez del consentimiento, el historial del contratante, el entorno económico del negocio y las implicaciones fiscales y procesales de cada cláusula. La herramienta no conoce al usuario, no sabe si firmó bajo presión, si tiene antecedentes contractuales con la contraparte ni si existe una relación de poder desigual. Además, el derecho colombiano evoluciona constantemente con nuevas sentencias de la Corte Suprema y la Corte Constitucional que la herramienta no puede incorporar en tiempo real. Por estas razones, CONTRATO CHECK es útil como primera lectura orientativa antes de una consulta profesional, pero nunca como sustituto de ella.

---

## ✅ Parte 8 — Entregables finales (Definition of Done)

Requisitos de entrega del curso — todos deben estar ✅:

- [x] 🔗 **Solución funcionando**: CONTRATO CHECK desarrollada en **Python con Streamlit (`app.py`)** y versión web complementaria (`index.html`), detectando cláusulas ilegales y abusivas con citas expresas a la Ley 820 de 2003 y Código Civil. Pendiente activar URL pública en Streamlit Cloud / Vercel.
- [ ] 👤 **Usuario real**: al menos una persona externa al curso la usó, con evidencia (video corto o testimonio). Guarda la evidencia en `docs/evidencia-usuario.md`.
- [x] 📦 **Repositorio con historial**: este repo contiene todos los archivos del proyecto con commits documentados y la bitácora de avance semanal.
- [x] 🧠 **Análisis crítico**: Parte 7 completada con análisis honesto de las limitaciones.
- [x] 📋 Partes 1–7 de este README completas y al día.

---

*Construido con asistencia de IA — como se enseña en este curso.* 🧑‍⚖️🤖
