# CONTRATO CHECK — Revisor de Contratos Simples con IA Jurídica
# Pontificia Universidad Javeriana · 2026-II · Simón Andrés Contreras Palma
# Docente: Pedro Ardila

import streamlit as st
import io
import re

# ─────────────────────────────────────────────
# Configuración general de la página
# ─────────────────────────────────────────────
st.set_page_config(
    page_title="CONTRATO CHECK — Revisor Jurídico Colombiano",
    page_icon="⚖️",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# ─────────────────────────────────────────────
# CSS personalizado
# ─────────────────────────────────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&family=Outfit:wght@600;700;800&display=swap');

html, body, [class*="css"] {
    font-family: 'Inter', sans-serif;
}

/* Fondo general */
.stApp {
    background-color: #0b0f19;
    color: #f8fafc;
}

/* Ocultar menú hamburguesa y footer de Streamlit */
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
header {visibility: hidden;}

/* Banner de advertencia legal */
.legal-banner {
    background: linear-gradient(90deg, #92400e, #78350f);
    color: #fef3c7;
    padding: 12px 20px;
    border-radius: 10px;
    font-size: 0.88rem;
    border-left: 4px solid #f59e0b;
    margin-bottom: 20px;
}

/* Header principal */
.main-header {
    background: linear-gradient(135deg, #151c2e 0%, #1e293b 100%);
    border: 1px solid #26334d;
    border-radius: 16px;
    padding: 24px 32px;
    margin-bottom: 24px;
    display: flex;
    align-items: center;
    gap: 16px;
}

.brand-title {
    font-family: 'Outfit', sans-serif;
    font-size: 2rem;
    font-weight: 800;
    background: linear-gradient(135deg, #ffffff 0%, #93c5fd 100%);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    margin: 0;
}

.brand-tagline {
    color: #f59e0b;
    font-size: 0.85rem;
    font-weight: 600;
    letter-spacing: 0.08em;
    text-transform: uppercase;
}

/* Tarjetas de hallazgos */
.finding-critical {
    background-color: rgba(239, 68, 68, 0.08);
    border-left: 4px solid #ef4444;
    border-radius: 0 10px 10px 0;
    padding: 16px;
    margin-bottom: 12px;
}

.finding-warning {
    background-color: rgba(245, 158, 11, 0.08);
    border-left: 4px solid #f59e0b;
    border-radius: 0 10px 10px 0;
    padding: 16px;
    margin-bottom: 12px;
}

.finding-missing {
    background-color: rgba(6, 182, 212, 0.08);
    border-left: 4px solid #06b6d4;
    border-radius: 0 10px 10px 0;
    padding: 16px;
    margin-bottom: 12px;
}

.finding-ok {
    background-color: rgba(16, 185, 129, 0.08);
    border-left: 4px solid #10b981;
    border-radius: 0 10px 10px 0;
    padding: 16px;
    margin-bottom: 12px;
}

.finding-title {
    font-weight: 700;
    font-size: 1rem;
    margin-bottom: 6px;
}

.finding-explanation {
    font-size: 0.9rem;
    color: #cbd5e1;
    margin-bottom: 8px;
}

.finding-quote {
    font-family: monospace;
    background: rgba(0,0,0,0.3);
    padding: 6px 10px;
    border-radius: 4px;
    font-size: 0.82rem;
    color: #94a3b8;
    margin-bottom: 8px;
}

.finding-citation {
    font-size: 0.82rem;
    color: #93c5fd;
    font-weight: 600;
}

/* Caja de recomendaciones */
.recommendations-box {
    background-color: rgba(245, 158, 11, 0.08);
    border: 1px solid rgba(245, 158, 11, 0.3);
    border-radius: 12px;
    padding: 16px 20px;
    margin-top: 20px;
}

/* Corpus cards */
.corpus-card {
    background-color: #151c2e;
    border: 1px solid #26334d;
    border-radius: 12px;
    padding: 16px;
    text-align: center;
}

/* Stat boxes */
.stat-box {
    background-color: #0f1626;
    border: 1px solid #26334d;
    border-radius: 10px;
    padding: 14px;
    text-align: center;
}

/* Overrides de Streamlit */
div[data-testid="stTextArea"] textarea {
    background-color: #0f1626 !important;
    color: #f8fafc !important;
    border: 1px solid #26334d !important;
    border-radius: 10px !important;
    font-family: 'Inter', sans-serif !important;
}

div[data-testid="stSelectbox"] > div {
    background-color: #0f1626 !important;
    color: #f8fafc !important;
    border: 1px solid #26334d !important;
}

.stButton > button {
    background: linear-gradient(135deg, #3b82f6, #1d4ed8) !important;
    color: white !important;
    border: none !important;
    border-radius: 10px !important;
    font-family: 'Outfit', sans-serif !important;
    font-weight: 700 !important;
    font-size: 1rem !important;
    padding: 14px 28px !important;
    width: 100% !important;
    transition: all 0.2s ease !important;
}

.stButton > button:hover {
    background: linear-gradient(135deg, #60a5fa, #2563eb) !important;
    transform: translateY(-1px) !important;
    box-shadow: 0 6px 20px rgba(59,130,246,0.4) !important;
}
</style>
""", unsafe_allow_html=True)


# ─────────────────────────────────────────────
# Contrato de muestra con riesgos reales
# ─────────────────────────────────────────────
CONTRATO_MUESTRA = """CONTRATO DE ARRENDAMIENTO DE VIVIENDA URBANA

Entre los suscritos a saber: MARÍA GÓMEZ, mayor de edad, identificada con C.C. 1.098.765.432, denominada el ARRENDADOR, y JUAN PÉREZ, identificado con C.C. 1.012.345.678, denominado el ARRENDATARIO, se celebra el presente contrato sujeto a las siguientes cláusulas:

PRIMERA. OBJETO: El ARRENDADOR entrega en arrendamiento al ARRENDATARIO el inmueble ubicado en la Calle 45 # 12-34 Apto 301 de la ciudad de Bogotá D.C.

SEGUNDA. CANON DE ARRENDAMIENTO Y REAJUSTE: El canon mensual será de DOS MILLONES DE PESOS ($2.000.000 COP). Al finalizar cada 12 meses, el arrendador podrá incrementar unilateralmente el canon en un VEINTE POR CIENTO (20%), independientemente de la inflación o el IPC oficial.

TERCERA. DEPÓSITO EN GARANTÍA EN DINERO: Para garantizar el cumplimiento de las obligaciones del presente contrato, el ARRENDATARIO entregará al momento de la firma la suma en efectivo de TRES MILLONES DE PESOS ($3.000.000 COP) en calidad de depósito en dinero en efectivo. Dicho depósito no devengará intereses y será devuelto si el arrendador lo considera conveniente.

CUARTA. MANTENIMIENTO Y REPARACIONES: El ARRENDATARIO asume la totalidad de las reparaciones del inmueble, incluidas las reparaciones locativas, estructurales, tuberías internas y vicios ocultos de construcción. El ARRENDADOR queda totalmente exonerado de cualquier mantenimiento.

QUINTA. TERMINACIÓN E INDEMNIZACIÓN: El ARRENDADOR podrá solicitar la restitución inmediata del inmueble en cualquier momento sin necesidad de dar preaviso alguno ni justificar causal alguna. En caso de mora de 1 solo día en el pago, el arrendatario pagará una sanción equivalente a CINCO CANONES mensuales.

SEXTA. CESIÓN: Queda totalmente prohibida la subarrienda o cesión del inmueble.

Firmado en Bogotá D.C. a los 10 días del mes de agosto de 2026."""


# ─────────────────────────────────────────────
# Extractor de texto para archivos (.txt, .pdf, .docx, .md)
# ─────────────────────────────────────────────
def extraer_texto_archivo(archivo) -> str:
    """Extrae el contenido de texto de un archivo cargado (.txt, .pdf, .docx, .md)."""
    if archivo is None:
        return ""
    nombre = archivo.name.lower()
    try:
        if nombre.endswith((".txt", ".md")):
            try:
                return archivo.read().decode("utf-8")
            except UnicodeDecodeError:
                archivo.seek(0)
                return archivo.read().decode("latin-1", errors="ignore")
        elif nombre.endswith(".pdf"):
            # Intentar pypdf / PyPDF2
            try:
                import pypdf
                reader = pypdf.PdfReader(archivo)
                paginas = [p.extract_text() or "" for p in reader.pages]
                return "\n\n".join(p for p in paginas if p.strip())
            except ImportError:
                try:
                    import PyPDF2
                    reader = PyPDF2.PdfReader(archivo)
                    paginas = [p.extract_text() or "" for p in reader.pages]
                    return "\n\n".join(p for p in paginas if p.strip())
                except ImportError:
                    # Heurística para PDF de texto sin librerías externas
                    archivo.seek(0)
                    raw = archivo.read()
                    matches = re.findall(rb"\(([\w\s\.,;:/\-áéíóúñÁÉÍÓÚÑ\$%]+)\)", raw)
                    if matches:
                        return b" ".join(matches).decode("latin-1", errors="ignore")
                    return ""
        elif nombre.endswith(".docx"):
            # docx es un archivo zip con word/document.xml
            import zipfile
            import xml.etree.ElementTree as ET
            try:
                archivo.seek(0)
                with zipfile.ZipFile(archivo) as z:
                    xml_content = z.read("word/document.xml")
                    tree = ET.fromstring(xml_content)
                    ns = "http://schemas.openxmlformats.org/wordprocessingml/2006/main"
                    parrafos = []
                    for p in tree.iter(f"{{{ns}}}p"):
                        textos = [node.text for node in p.iter(f"{{{ns}}}t") if node.text]
                        if textos:
                            parrafos.append("".join(textos))
                    return "\n\n".join(parrafos)
            except Exception:
                try:
                    import docx
                    archivo.seek(0)
                    doc = docx.Document(archivo)
                    return "\n\n".join([p.text for p in doc.paragraphs if p.text.strip()])
                except Exception:
                    return ""
    except Exception as e:
        st.error(f"Error al leer el archivo: {e}")
        return ""
    return ""


# ─────────────────────────────────────────────
# Motor de análisis jurídico normativo
# ─────────────────────────────────────────────
def analizar_contrato(texto: str, tipo: str) -> dict:
    if not texto or len(texto.strip()) < 50:
        return None

    texto_lower = texto.lower()
    hallazgos = []
    recomendaciones = []
    criticos = 0
    advertencias = 0
    faltantes = 0

    # REGLA 1: Depósito en dinero prohibido (Ley 820/2003 Art. 16)
    if tipo == "arrendamiento":
        if ("depósito" in texto_lower or "deposito" in texto_lower) and \
           ("dinero" in texto_lower or "efectivo" in texto_lower or "suma" in texto_lower):
            criticos += 1
            hallazgos.append({
                "tipo": "critical",
                "titulo": "🚨 Depósito en dinero: PROHIBIDO por ley",
                "explicacion": (
                    "En contratos de arrendamiento de vivienda urbana está expresamente "
                    "prohibido exigir depósitos en dinero en efectivo. Esta cláusula es "
                    "NULA DE PLENO DERECHO y no produce ningún efecto legal."
                ),
                "cita_texto": "Exigencia de depósito en dinero o efectivo para garantizar el contrato.",
                "fuente": "Ley 820 de 2003 — Artículo 16: 'En los contratos de arrendamiento de vivienda urbana no se podrán exigir depósitos en dinero o garantías reales...'"
            })
            recomendaciones.append(
                "Exige eliminar el depósito en dinero. El arrendador solo puede pedir "
                "póliza de arrendamiento o fiador personal (codeudor)."
            )

    # REGLA 2: Reajuste del canon superior al IPC (Ley 820/2003 Art. 20)
    if tipo == "arrendamiento":
        tiene_reajuste = any(p in texto_lower for p in ["reajust", "increment", "aument"])
        tiene_porcentaje_alto = any(p in texto_lower for p in [
            "20%", "15%", "30%", "25%",
            "independientemente de la inflación",
            "independientemente del ipc",
            "sin tener en cuenta el ipc"
        ])
        if tiene_reajuste and tiene_porcentaje_alto:
            criticos += 1
            hallazgos.append({
                "tipo": "critical",
                "titulo": "🚨 Aumento de canon SUPERIOR al límite legal (IPC)",
                "explicacion": (
                    "El arrendador NO puede fijar un porcentaje fijo de incremento (ej. 20%) "
                    "superior al IPC certificado por el DANE para el año anterior. "
                    "Este tipo de cláusula viola la Ley 820 de 2003."
                ),
                "cita_texto": "Incremento unilateral superior al índice de precios al consumidor (IPC).",
                "fuente": "Ley 820 de 2003 — Artículo 20: 'El arrendador podrá reajustar el canon en un porcentaje que no podrá ser superior al 100% del incremento que haya tenido el IPC...'"
            })
            recomendaciones.append(
                "Solicita ajustar la cláusula de reajuste para que quede limitada "
                "expresamente al 100% del IPC del año anterior, certificado por el DANE."
            )

    # REGLA 3: Exoneración de reparaciones estructurales (Código Civil Art. 1985)
    if any(p in texto_lower for p in [
        "exonerado", "exonerada", "estructural", "vicios ocultos",
        "totalidad de las reparaciones", "todas las reparaciones"
    ]):
        advertencias += 1
        hallazgos.append({
            "tipo": "warning",
            "titulo": "⚠️ Exoneración abusiva de reparaciones necesarias",
            "explicacion": (
                "Transferir al arrendatario/usuario la responsabilidad de reparaciones "
                "estructurales, de tuberías internas o vicios de construcción rompe el "
                "equilibrio del contrato. Estas son obligación del propietario/contratante."
            ),
            "cita_texto": "El arrendatario asume reparaciones estructurales o vicios ocultos de construcción.",
            "fuente": "Código Civil colombiano — Artículo 1985: El arrendador está obligado a realizar las reparaciones necesarias no locativas para el uso normal del inmueble."
        })
        recommendaciones.append(
            "Aclara que las reparaciones locativas por uso normal son del arrendatario, "
            "pero las estructurales, de tuberías internas y vicios ocultos son obligación del propietario."
        )

    # REGLA 4: Terminación sin preaviso legal (Ley 820/2003 Arts. 22 y 24)
    if any(p in texto_lower for p in [
        "sin necesidad de dar preaviso",
        "restitución inmediata",
        "en cualquier momento sin"
    ]):
        criticos += 1
        hallazgos.append({
            "tipo": "critical",
            "titulo": "🚨 Terminación sin preaviso: ILEGAL",
            "explicacion": (
                "La ley exige que el arrendador notifique por escrito con mínimo 3 meses "
                "de anticipación su intención de terminar el contrato. Pedir la restitución "
                "'inmediata' o 'en cualquier momento' sin preaviso viola la Ley 820 de 2003."
            ),
            "cita_texto": "Restitución inmediata del inmueble sin preaviso ni justificación de causal.",
            "fuente": "Ley 820 de 2003 — Artículos 22 y 24: La terminación unilateral por el arrendador exige preaviso escrito no menor a tres (3) meses de antelación."
        })
        recomendaciones.append(
            "Establece que cualquier terminación unilateral debe notificarse por escrito "
            "con al menos 3 meses de anticipación y el pago de la indemnización legal."
        )

    # REGLA 5: Cláusula penal desproporcionada (Código Civil Art. 1601)
    if any(p in texto_lower for p in [
        "cinco canon", "cinco cánones", "5 canon", "5 cánones",
        "sanción equivalente a cinco", "multa de cinco"
    ]):
        advertencias += 1
        hallazgos.append({
            "tipo": "warning",
            "titulo": "⚠️ Cláusula penal desproporcionada (penalidad enorme)",
            "explicacion": (
                "Una sanción de 5 cánones por un retraso de solo 1 día es abusiva "
                "y desproporcionada. El Código Civil permite al juez reducir cláusulas "
                "penales que excedan el doble de la obligación principal."
            ),
            "cita_texto": "Multa o sanción de 5 cánones mensuales por mora de 1 día.",
            "fuente": "Código Civil colombiano — Artículo 1601: La cláusula penal enorme puede ser reducida judicialmente si excede el duplo de la obligación principal."
        })
        recomendaciones.append(
            "Negocia que la cláusula penal sea máximo 1 o 2 cánones, y solo aplicable "
            "cuando el arrendatario esté previamente constituido en mora."
        )

    # VERIFICACIÓN: Cláusulas esenciales faltantes (solo para arrendamiento con texto suficiente)
    if tipo == "arrendamiento" and len(texto.strip()) >= 150:
        if "inventario" not in texto_lower:
            faltantes += 1
            hallazgos.append({
                "tipo": "missing",
                "titulo": "ℹ️ Falta: Acta de inventario inicial del inmueble",
                "explicacion": (
                    "Sin un inventario firmado con el estado inicial del inmueble (paredes, pisos, "
                    "servicios públicos), el arrendador podría cobrarte daños preexistentes al momento de entrega."
                ),
                "cita_texto": "No se menciona la elaboración de un acta de inventario inicial.",
                "fuente": "Código Civil — Artículo 1996 y buenas prácticas contractuales colombianas."
            })
            recomendaciones.append(
                "Exige un Anexo de Inventario firmado por ambas partes con fotos y descripción "
                "del estado de muros, pisos, baños y servicios públicos al inicio del contrato."
            )

        if "servicios públicos" not in texto_lower and "servicios publicos" not in texto_lower:
            faltantes += 1
            hallazgos.append({
                "tipo": "missing",
                "titulo": "ℹ️ Falta: Responsabilidad sobre servicios públicos",
                "explicacion": (
                    "El contrato no especifica quién paga los servicios públicos (agua, luz, gas, internet). "
                    "Esto puede generar cobros o cortes inesperados."
                ),
                "cita_texto": "No hay cláusula que asigne la responsabilidad de pago de servicios domiciliarios.",
                "fuente": "Ley 820 de 2003 — Artículo 15: Obligaciones del arrendatario respecto a servicios públicos."
            })

    # Caso sin hallazgos evidentes
    if not hallazgos:
        hallazgos.append({
            "tipo": "ok",
            "titulo": "✅ No se detectaron cláusulas evidentemente ilegales",
            "explicacion": (
                "El texto analizado no contiene los patrones de riesgo más frecuentes. "
                "De todas formas, revisa con detenimiento nombres, valores, fechas y plazos."
            ),
            "cita_texto": "Texto dentro de los parámetros contractuales generales.",
            "fuente": "Código Civil colombiano — Artículo 1602: El contrato legalmente celebrado es ley para las partes."
        })
        recomendaciones.append(
            "Verifica la identidad del propietario mediante Certificado de Libertad y Tradición "
            "reciente (solicitable en la Ventanilla Única de Registro - VUR) antes de realizar pagos."
        )

    # Puntaje de riesgo general
    puntaje = min(98, criticos * 35 + advertencias * 15 + faltantes * 8)
    if puntaje == 0 and hallazgos and hallazgos[0]["tipo"] != "ok":
        puntaje = 12
    elif puntaje == 0:
        puntaje = 5

    return {
        "puntaje": puntaje,
        "criticos": criticos,
        "advertencias": advertencias,
        "faltantes": faltantes,
        "hallazgos": hallazgos,
        "recomendaciones": recomendaciones,
    }


# ─────────────────────────────────────────────
# GESTIÓN DE ESTADO (SESSION STATE)
# ─────────────────────────────────────────────
if "texto_contrato" not in st.session_state:
    st.session_state["texto_contrato"] = ""

if "resultado_analisis" not in st.session_state:
    st.session_state["resultado_analisis"] = None

if "ultimo_archivo" not in st.session_state:
    st.session_state["ultimo_archivo"] = None


# ─────────────────────────────────────────────
# INTERFAZ PRINCIPAL
# ─────────────────────────────────────────────

# Banner legal obligatorio (Parte 6)
st.markdown("""
<div class="legal-banner">
    ⚠️ <strong>ADVERTENCIA LEGAL OBLIGATORIA:</strong>
    Esta herramienta es un ejercicio académico del curso de Derecho e Inteligencia Artificial
    de la <strong>Pontificia Universidad Javeriana</strong>.
    <em>No constituye asesoría legal ni sustituye la consulta con un abogado titulado.</em>
</div>
""", unsafe_allow_html=True)

# Header con marca
st.markdown("""
<div style="display:flex; align-items:center; gap:16px; margin-bottom:24px;">
    <div style="font-size:3rem;">⚖️</div>
    <div>
        <div class="brand-title">CONTRATO CHECK</div>
        <div class="brand-tagline">Revisa · Detecta · Decide</div>
    </div>
    <div style="margin-left:auto; display:flex; gap:8px;">
        <span style="background:rgba(59,130,246,0.15);color:#93c5fd;border:1px solid rgba(59,130,246,0.3);padding:5px 12px;border-radius:9999px;font-size:0.78rem;font-weight:600;">PUJ 2026-II</span>
        <span style="background:rgba(16,185,129,0.15);color:#6ee7b7;border:1px solid rgba(16,185,129,0.3);padding:5px 12px;border-radius:9999px;font-size:0.78rem;font-weight:600;">🟢 v1.0</span>
    </div>
</div>
""", unsafe_allow_html=True)

st.markdown("#### Analiza tu contrato antes de firmar — identifica cláusulas **ilegales, riesgosas o faltantes** con base en la ley colombiana.")
st.divider()

# ─── Columnas: entrada | resultados ───
col_izq, col_der = st.columns([1, 1], gap="large")

with col_izq:
    st.markdown("### 📄 1. Cargar Contrato")

    tipo = st.selectbox(
        "Tipo de Contrato",
        options=["arrendamiento", "servicios", "general"],
        format_func=lambda x: {
            "arrendamiento": "🏠 Arrendamiento de Vivienda Urbana (Ley 820 de 2003)",
            "servicios":     "💼 Prestación de Servicios (Código Civil / Comercial)",
            "general":       "📄 Otro Contrato Civil o Comercial General",
        }[x],
        key="tipo_contrato"
    )

    # 1. Carga de archivo
    archivo_subido = st.file_uploader(
        "📁 Subir archivo de contrato (.txt, .pdf, .docx, .md)",
        type=["txt", "pdf", "docx", "md"],
        help="Carga un archivo y su contenido se colocará automáticamente en el área de texto."
    )

    if archivo_subido is not None:
        if st.session_state.get("ultimo_archivo") != archivo_subido.name:
            texto_extraido = extraer_texto_archivo(archivo_subido)
            if texto_extraido.strip():
                st.session_state["texto_contrato"] = texto_extraido
                st.session_state["ultimo_archivo"] = archivo_subido.name
                st.session_state["resultado_analisis"] = None
                st.success(f"✅ Archivo cargado con éxito: **{archivo_subido.name}** ({len(texto_extraido):,} caracteres)")
                st.rerun()
            else:
                st.warning("⚠️ No se pudo extraer texto del archivo o está vacío. Intenta copiar y pegar el texto directamente.")

    # 2. Botones de acción rápida
    btn_col1, btn_col2 = st.columns([3, 2])
    with btn_col1:
        if st.button("✨ Cargar contrato de muestra"):
            st.session_state["texto_contrato"] = CONTRATO_MUESTRA
            st.session_state["resultado_analisis"] = None
            st.rerun()

    with btn_col2:
        if st.button("🗑️ Limpiar todo"):
            st.session_state["texto_contrato"] = ""
            st.session_state["resultado_analisis"] = None
            st.session_state["ultimo_archivo"] = None
            st.rerun()

    # 3. Área de texto
    texto_ingresado = st.text_area(
        "Texto del Contrato",
        value=st.session_state.get("texto_contrato", ""),
        placeholder="Pega aquí el texto completo de tu contrato o súbelo en un archivo arriba...",
        height=320,
        key="textarea_contrato_input"
    )

    # Actualizar estado si el usuario editó directamente en el text_area
    if texto_ingresado != st.session_state.get("texto_contrato", ""):
        st.session_state["texto_contrato"] = texto_ingresado
        # Si borró todo el texto, limpiar también el diagnóstico
        if not texto_ingresado.strip():
            st.session_state["resultado_analisis"] = None

    # 4. Botón de análisis
    analizar = st.button("🔍 Analizar Riesgos Jurídicos", use_container_width=True)

    if analizar:
        texto_actual = st.session_state.get("texto_contrato", "").strip()
        if not texto_actual:
            st.warning("⚠️ No has ingresado ningún contrato. Por favor pega el texto o sube un archivo antes de analizar.")
            st.session_state["resultado_analisis"] = None
        elif len(texto_actual) < 50:
            st.warning("⚠️ El texto ingresado es demasiado corto para constituir un contrato. Por favor ingresa el texto completo de las cláusulas.")
            st.session_state["resultado_analisis"] = None
        else:
            with st.spinner("Contrastando cláusulas con la Ley 820 de 2003 y el Código Civil..."):
                resultado = analizar_contrato(texto_actual, tipo)
                st.session_state["resultado_analisis"] = resultado

# ─── Panel de resultados ───
with col_der:
    st.markdown("### 📊 2. Diagnóstico Jurídico")

    resultado = st.session_state.get("resultado_analisis")
    texto_actual = st.session_state.get("texto_contrato", "").strip()

    # Si no hay análisis activo o el texto fue borrado, mostrar estado inicial limpio
    if not resultado or not texto_actual:
        st.info(
            "📜 **Listo para evaluar**\n\n"
            "Pega tu contrato a la izquierda, **sube un archivo** (.txt, .pdf, .docx) o carga el "
            "**contrato de muestra** y presiona **'Analizar Riesgos Jurídicos'** para ver el informe."
        )

    else:
        # Semáforo de riesgo
        p = resultado["puntaje"]
        if p >= 60:
            nivel_emoji = "🔴"
            nivel_texto = "RIESGO ALTO"
            nivel_color = "#ef4444"
        elif p >= 25:
            nivel_emoji = "🟡"
            nivel_texto = "RIESGO MEDIO"
            nivel_color = "#f59e0b"
        else:
            nivel_emoji = "🟢"
            nivel_texto = "RIESGO BAJO"
            nivel_color = "#10b981"

        st.markdown(f"""
        <div style="background:rgba(0,0,0,0.2);border:1px solid #26334d;border-radius:12px;padding:16px;margin-bottom:16px;">
            <div style="display:flex;justify-content:space-between;align-items:center;">
                <span style="font-family:'Outfit',sans-serif;font-size:1.1rem;font-weight:700;">
                    {nivel_emoji} Nivel de Riesgo Global
                </span>
                <span style="background:rgba(0,0,0,0.3);color:{nivel_color};border:1px solid {nivel_color}40;
                       padding:4px 14px;border-radius:9999px;font-weight:700;font-size:0.85rem;">
                    {nivel_texto}
                </span>
            </div>
            <div style="font-family:'Outfit',sans-serif;font-size:2.5rem;font-weight:800;color:{nivel_color};margin:8px 0 0 0;">
                {p}%
            </div>
        </div>
        """, unsafe_allow_html=True)

        # Estadísticas
        c1, c2, c3 = st.columns(3)
        with c1:
            st.markdown(f"""
            <div class="stat-box">
                <div style="font-size:0.72rem;color:#94a3b8;font-weight:600;text-transform:uppercase;">Alertas Críticas</div>
                <div style="font-size:1.8rem;font-weight:800;color:#ef4444;">{resultado['criticos']}</div>
                <div style="font-size:0.7rem;color:#64748b;">Cláusulas ilegales</div>
            </div>""", unsafe_allow_html=True)
        with c2:
            st.markdown(f"""
            <div class="stat-box">
                <div style="font-size:0.72rem;color:#94a3b8;font-weight:600;text-transform:uppercase;">Advertencias</div>
                <div style="font-size:1.8rem;font-weight:800;color:#f59e0b;">{resultado['advertencias']}</div>
                <div style="font-size:0.7rem;color:#64748b;">Cláusulas riesgosas</div>
            </div>""", unsafe_allow_html=True)
        with c3:
            st.markdown(f"""
            <div class="stat-box">
                <div style="font-size:0.72rem;color:#94a3b8;font-weight:600;text-transform:uppercase;">Faltantes</div>
                <div style="font-size:1.8rem;font-weight:800;color:#06b6d4;">{resultado['faltantes']}</div>
                <div style="font-size:0.7rem;color:#64748b;">Cláusulas esenciales</div>
            </div>""", unsafe_allow_html=True)

        st.markdown("#### 📋 Hallazgos con Citas Jurídicas")

        clases = {
            "critical": "finding-critical",
            "warning":  "finding-warning",
            "missing":  "finding-missing",
            "ok":       "finding-ok",
        }

        for h in resultado["hallazgos"]:
            css = clases.get(h["tipo"], "finding-ok")
            st.markdown(f"""
            <div class="{css}">
                <div class="finding-title">{h['titulo']}</div>
                <div class="finding-explanation">{h['explicacion']}</div>
                <div class="finding-quote">"{h['cita_texto']}"</div>
                <div class="finding-citation">📌 <strong>Fuente:</strong> {h['fuente']}</div>
            </div>
            """, unsafe_allow_html=True)

        # Recomendaciones
        if resultado["recomendaciones"]:
            recs_html = "".join(
                f"<li style='margin-bottom:6px;color:#fef3c7;font-size:0.88rem;'>➔ {r}</li>"
                for r in resultado["recomendaciones"]
            )
            st.markdown(f"""
            <div class="recommendations-box">
                <div style="color:#f59e0b;font-weight:700;font-size:0.95rem;margin-bottom:10px;">
                    💡 Recomendaciones para Negociar
                </div>
                <ul style="list-style:none;padding:0;margin:0;">{recs_html}</ul>
            </div>
            """, unsafe_allow_html=True)

st.divider()

# ─── Marco normativo de referencia ───
st.markdown("### 📚 Marco Normativo de Referencia (Corpus Colombiano)")
cn1, cn2, cn3 = st.columns(3)
with cn1:
    st.markdown("""
    <div class="corpus-card">
        <div style="font-size:2rem;">🏛️</div>
        <h4 style="margin:8px 0 4px;">Ley 820 de 2003</h4>
        <p style="font-size:0.84rem;color:#94a3b8;">Régimen de arrendamiento de vivienda urbana. Arts. 16 (depósitos), 20 (IPC), 22 y 24 (terminación).</p>
    </div>""", unsafe_allow_html=True)
with cn2:
    st.markdown("""
    <div class="corpus-card">
        <div style="font-size:2rem;">📖</div>
        <h4 style="margin:8px 0 4px;">Código Civil Colombiano</h4>
        <p style="font-size:0.84rem;color:#94a3b8;">Arts. 1601 (cláusula penal enorme), 1602 (autonomía de la voluntad), 1985 (reparaciones).</p>
    </div>""", unsafe_allow_html=True)
with cn3:
    st.markdown("""
    <div class="corpus-card">
        <div style="font-size:2rem;">🛡️</div>
        <h4 style="margin:8px 0 4px;">Equilibrio Contractual</h4>
        <p style="font-size:0.84rem;color:#94a3b8;">Principio de prohibición de cláusulas abusivas que generen indefensión al contratante débil.</p>
    </div>""", unsafe_allow_html=True)

st.divider()

# Footer
st.markdown("""
<div style="text-align:center;color:#64748b;font-size:0.85rem;padding:16px 0;">
    <strong style="color:#94a3b8;">CONTRATO CHECK</strong> — Proyecto Académico
    <strong style="color:#94a3b8;">Pontificia Universidad Javeriana</strong> · 2026-II<br>
    Desarrollado por <strong style="color:#94a3b8;">Simón Andrés Contreras Palma</strong> · Docente: Pedro Ardila<br>
    <em>⚠️ Este análisis NO constituye asesoría legal. Siempre consulta con un abogado antes de firmar.</em>
</div>
""", unsafe_allow_html=True)
