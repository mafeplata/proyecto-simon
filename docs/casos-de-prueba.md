# 🧪 Banco de Casos de Prueba — CONTRATO CHECK (Hito M2)

**Pontificia Universidad Javeriana · Facultad de Ciencias Jurídicas**  
**Curso:** Derecho e Inteligencia Artificial (2026-II)  
**Docente:** Pedro Ardila  
**Estudiante:** Simón Andrés Contreras Palma  
**Proyecto:** CONTRATO CHECK — Revisor de Contratos Simples  

---

## 🎯 Metodología de Evaluación y Pruebas

El objetivo de este banco de pruebas es someter el motor de análisis normativo de **CONTRATO CHECK** a escenarios contractuales reales del derecho colombiano (arrendamiento de vivienda urbana y contratos civiles afines).

En los asistentes de propósito general sin corpus normativo estricto, la IA suele:
1. Pasar por alto cláusulas nulas de pleno derecho redactadas con lenguaje persuasivo.
2. Confundir los límites de la autonomía de la voluntad con normas de orden público indisponibles.
3. Alucinar artículos o leyes extranjeras (ej. leyes de inquilinato de España, México o Argentina).
4. No cuantificar el nivel de riesgo objetivo ni advertir cláusulas esenciales omitidas.

A continuación se documentan **5 casos de prueba críticos** (más 1 caso de control de falsos positivos) donde se evalúa el comportamiento esperado, el fallo común de herramientas no especializadas y la respuesta validada en **CONTRATO CHECK**.

---

### 📋 Caso 1: Exigencia de Depósito en Efectivo / Garantía Dineraria

* **Norma aplicable:** Ley 820 de 2003 — Artículo 16 (Prohibición de depósitos y garantías en dinero).
* **Tipo de contrato:** Arrendamiento de vivienda urbana.
* **Cláusula sometida a prueba:**
  > *"CLÁUSULA QUINTA. DEPÓSITO EN GARANTÍA: Para garantizar el cumplimiento de todas y cada una de las obligaciones pecuniarias derivadas del presente contrato, el ARRENDATARIO entregará en efectivo al ARRENDADOR la suma de TRES MILLONES DE PESOS ($3.000.000 COP) al momento de la firma, los cuales serán devueltos a discreción del arrendador al finalizar el contrato."*
* **Problema jurídico:** El artículo 16 de la Ley 820 de 2003 prohíbe de forma taxativa exigir depósitos en dinero o garantías reales en arrendamientos de vivienda urbana. La ley determina expresamente que tales estipulaciones no producen efecto alguno (ineficacia de pleno derecho).
* **¿Dónde fallaba antes?** En prompts estándar de IA general, el modelo solía validar la cláusula diciendo que *"es una práctica común en el mercado inmobiliario para cubrir daños"*, desconociendo que en Colombia es expresamente ilegal en vivienda urbana.
* **Resultado arrojado por CONTRATO CHECK:**
  * **Nivel:** 🚨 ALERTA CRÍTICA (Cláusula Nula / Ilegal).
  * **Hallazgo:** *"Depósito en dinero prohibido por ley"*.
  * **Cita Jurídica:** Ley 820 de 2003 — Artículo 16.
  * **Recomendación:** Exigir la eliminación inmediata del depósito en dinero; sustituir únicamente por póliza de arrendamiento o fiador con fianza personal.
* **Estado del caso:** ✅ **SUPERADO CON ÉXITO**

---

### 📋 Caso 2: Reajuste Unilateral del Canon Superior al Límite Legal (IPC)

* **Norma aplicable:** Ley 820 de 2003 — Artículo 20 (Reajuste del canon de arrendamiento).
* **Tipo de contrato:** Arrendamiento de vivienda urbana.
* **Cláusula sometida a prueba:**
  > *"CLÁUSULA TERCERA. INCREMENTO DEL CANON: Cumplidos doce (12) meses de ocupación, el arrendador tendrá la facultad de reajustar automáticamente el valor del canon en un VEINTE POR CIENTO (20%), independientemente de la tasa de inflación o del IPC oficial determinado por las autoridades."*
* **Problema jurídico:** El reajuste anual del canon en vivienda urbana tiene un tope legal imperativo: no puede exceder el 100% del incremento del Índice de Precios al Consumidor (IPC) del año calendario inmediatamente anterior fijado por el DANE. Fijar un 20% arbitrario viola norma de orden público.
* **¿Dónde fallaba antes?** Frecuentemente los asistentes asumían que, al haber acuerdo libre de las partes bajo la autonomía de la voluntad (Art. 1602 C.C.), el porcentaje pactado era vinculante y válido.
* **Resultado arrojado por CONTRATO CHECK:**
  * **Nivel:** 🚨 ALERTA CRÍTICA (Violación a norma imperativa).
  * **Hallazgo:** *"Incremento de canon superior al límite legal (IPC)"*.
  * **Cita Jurídica:** Ley 820 de 2003 — Artículo 20.
  * **Recomendación:** Limitar expresamente cualquier ajuste al 100% del IPC acumulado certificado por el DANE.
* **Estado del caso:** ✅ **SUPERADO CON ÉXITO**

---

### 📋 Caso 3: Terminación Inmediata Unilateral sin Preaviso Legal

* **Norma aplicable:** Ley 820 de 2003 — Artículos 22 y 24 (Causales y requisitos de terminación unilateral).
* **Tipo de contrato:** Arrendamiento de vivienda urbana.
* **Cláusula sometida a prueba:**
  > *"CLÁUSULA NOVENA. RESTITUCIÓN EXPEDITA: El ARRENDADOR podrá dar por terminado el contrato en cualquier momento de manera unilateral y solicitar la restitución inmediata del inmueble sin necesidad de dar preaviso alguno ni mediar indemnización ni motivo legal alguno."*
* **Problema jurídico:** La Ley 820 de 2003 regula de forma detallada las causales de terminación. Cuando el arrendador termina sin causal de incumplimiento, la ley impone obligatoriamente un preaviso escrito por servicio postal de mínimo tres (3) meses y el pago de una indemnización tasada legalmente (3 meses de canon).
* **¿Dónde fallaba antes?** El asistente general advertía que era *"una cláusula estricta pero negociable"*, sin catalogarla como frontalmente ilegal según el régimen de vivienda urbana colombiano.
* **Resultado arrojado por CONTRATO CHECK:**
  * **Nivel:** 🚨 ALERTA CRÍTICA.
  * **Hallazgo:** *"Terminación sin preaviso legal"*.
  * **Cita Jurídica:** Ley 820 de 2003 — Artículos 22 y 24.
  * **Recomendación:** Pactar que toda terminación sin causal exige preaviso escrito mínimo de 3 meses e indemnización legal.
* **Estado del caso:** ✅ **SUPERADO CON ÉXITO**

---

### 📋 Caso 4: Exoneración de Reparaciones Estructurales y Vicios Ocultos

* **Norma aplicable:** Código Civil Colombiano — Artículo 1985 (Obligación de reparaciones en la cosa arrendada) y Ley 820 de 2003.
* **Tipo de contrato:** Arrendamiento de inmueble.
* **Cláusula sometida a prueba:**
  > *"CLÁUSULA SÉPTIMA. REPARACIONES Y ESTADO DEL INMUEBLE: El arrendatario asume a su exclusiva cuenta y costo la totalidad de las reparaciones del inmueble, comprendiendo daños estructurales, humedades por vicios de construcción, tuberías principales y fallas en la red eléctrica. El arrendador se declara totalmente exonerado de cualquier deber de conservación."*
* **Problema jurídico:** El Código Civil impone al arrendador la obligación de mantener el bien en estado de servir, asumiendo las reparaciones necesarias no locativas (estructuras, tuberías, vicios ocultos). Trasladar los daños constructivos y estructurales al arrendatario genera un grave desequilibrio contractual lesivo de la buena fe objetiva.
* **¿Dónde fallaba antes?** La IA genérica clasificaba esto como *"acuerdo sobre distribución de gastos de mantenimiento"* sin alertar sobre el desbalance patrimonial que traslada el riesgo de vicios redhibitorios.
* **Resultado arrojado por CONTRATO CHECK:**
  * **Nivel:** ⚠️ ADVERTENCIA (Cláusula de desequilibrio grave / abusiva).
  * **Hallazgo:** *"Exoneración desproporcionada de reparaciones necesarias"*.
  * **Cita Jurídica:** Código Civil Colombiano — Artículo 1985.
  * **Recomendación:** Clarificar que el arrendatario solo asume locativas por uso ordinario, mientras que las obras estructurales corresponden al arrendador.
* **Estado del caso:** ✅ **SUPERADO CON ÉXITO**

---

### 📋 Caso 5: Cláusula Penal Exorbitante y Omisión de Cláusulas Esenciales

* **Norma aplicable:** Código Civil — Artículos 1601 (Cláusula penal enorme) y 1996; Ley 820 de 2003, Art. 15.
* **Tipo de contrato:** Arrendamiento de vivienda urbana.
* **Cláusula sometida a prueba:**
  > *"CLÁUSULA DÉCIMA. PENALIDAD POR MORA: Si el arrendatario se retarda 1 solo día en el pago del canon mensual, incurrirá en una cláusula penal automática a favor del arrendador por la suma fija equivalente a CINCO (5) CÁNONES mensuales de arrendamiento, sin perjuicio del cobro de intereses moratorios al doble de la tasa máxima permitida."*  
  *(Nota adicional: el contrato no contiene ninguna mención a inventario inicial ni a la especificación de servicios públicos domiciliarios).*
* **Problema jurídico:**
  1. Una sanción de 5 cánones por un retraso de un día constituye una **cláusula penal enorme** reducible judicialmente al amparo del Art. 1601 del Código Civil (límite del duplo de la obligación).
  2. La omisión del acta de inventario inicial deja en indefensión al arrendatario ante reclamaciones de deterioros preexistentes al entregar el inmueble.
  3. No estipular los servicios públicos (Art. 15, Ley 820) propicia cortes y cobros indebidos.
* **¿Dónde fallaba antes?** Los modelos genéricos evaluaban únicamente el texto escrito pero pasaban por alto **lo que no estaba escrito** (cláusulas faltantes indispensables).
* **Resultado arrojado por CONTRATO CHECK:**
  * **Nivel:** ⚠️ ADVERTENCIA + ℹ️ VACÍO NORMATIVO FALTANTE.
  * **Hallazgos:**
    1. *"Cláusula penal desproporcionada"* (Cita: Código Civil — Art. 1601).
    2. *"Ausencia de acta de inventario inicial"* (Cita: Código Civil — Art. 1996).
    3. *"Falta: Responsabilidad sobre servicios públicos"* (Cita: Ley 820 de 2003 — Art. 15).
  * **Recomendaciones:** Reducir la pena a un tope razonable (1-2 cánones) y obligar a levantar acta de entrega con inventario fotográfico firmado.
* **Estado del caso:** ✅ **SUPERADO CON ÉXITO**

---

### 📋 Caso de Control (Negativo): Contrato Equilibrado y Conforme a Derecho

* **Objetivo:** Verificar que la herramienta no arroje falsas alertas críticas en contratos que cumplen la ley.
* **Fragmento probado:** Contrato de arrendamiento donde el canon se reajusta expresamente según el IPC del DANE, se pacta fianza personal sin depósito dinerario, las reparaciones necesarias corresponden al arrendador, y se contempla preaviso legal de 3 meses con anexo de inventario.
* **Resultado arrojado por CONTRATO CHECK:**
  * **Nivel:** 🟢 RIESGO BAJO (Puntaje inferior al 20%).
  * **Hallazgo:** No detecta violaciones de orden público; recuerda recomendaciones preventivas de verificación de títulos de propiedad (VUR / Certificado de Tradición).
* **Estado del caso:** ✅ **SUPERADO CON ÉXITO**

---

## 📊 Matriz Resumen de Pruebas

| Caso | Hipótesis Jurídica Probada | Norma Colombiana | Resultado Previsto | Detección CONTRATO CHECK | Estado |
| :---: | :--- | :--- | :---: | :---: | :---: |
| **1** | Depósito dinerario exigido | Ley 820/2003 Art. 16 | Alerta Crítica (Nula) | 🚨 Nula de pleno derecho | **Aprobado ✅** |
| **2** | Incremento fijo del 20% | Ley 820/2003 Art. 20 | Alerta Crítica (Tope IPC) | 🚨 Exceso sobre IPC legal | **Aprobado ✅** |
| **3** | Restitución sin preaviso | Ley 820/2003 Arts. 22-24 | Alerta Crítica (3 meses) | 🚨 Violación preaviso legal | **Aprobado ✅** |
| **4** | Arrendatario asume vicios | Código Civil Art. 1985 | Advertencia (Desbalance) | ⚠️ Exoneración abusiva | **Aprobado ✅** |
| **5** | Cláusula penal de 5 cánones + Omisión de inventario | C.C. Arts. 1601, 1996; Ley 820 Art. 15 | Advertencia + Faltante | ⚠️ Penal enorme + 2 Faltantes | **Aprobado ✅** |
| **6** | Contrato estándar ajustado a norma | Código Civil Art. 1602 | Riesgo Bajo / Sin críticas | 🟢 Parámetros legales cumplidos | **Aprobado ✅** |

---

*Documento elaborado como evidencia del **Hito M2** del curso Derecho e Inteligencia Artificial, Pontificia Universidad Javeriana.*
