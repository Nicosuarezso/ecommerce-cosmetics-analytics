# Estructura del proyecto
ecommerce-cosmetics-analytics/
│
├── data/
│   ├── raw/
│   │   └── .gitkeep
│   │
│   ├── interim/
│   │   └── .gitkeep
│   │
│   └── processed/
│       └── .gitkeep
│
├── notebooks/
│   ├── 01_data_understanding.ipynb
│   ├── 02_data_quality.ipynb
│   ├── 03_customer_journey_analysis.ipynb
│   ├── 04_customer_analysis.ipynb
│   ├── 05_product_analysis.ipynb
│   ├── 06_rfm_segmentation.ipynb
│   ├── 07_cohort_analysis.ipynb
│   ├── 08_ltv_analysis.ipynb
│   ├── 09_advanced_analytics.ipynb
│   └── 10_ml_solution.ipynb
│
├── src/
│   ├── __init__.py
│   │
│   ├── data/
│   │   ├── __init__.py
│   │   ├── loading.py
│   │   └── cleaning.py
│   │
│   ├── analysis/
│   │   ├── __init__.py
│   │   ├── funnel.py
│   │   ├── customers.py
│   │   ├── products.py
│   │   ├── rfm.py
│   │   ├── cohorts.py
│   │   └── ltv.py
│   │
│   └── models/
│       ├── __init__.py
│       ├── preprocessing.py
│       ├── train.py
│       └── evaluate.py
│
├── reports/
│   ├── figures/
│   └── business_report.md
│
├── models/
│
├── README.md
├── PROJECT_CONTEXT.md
├── requirements.txt
├── .gitignore
└── LICENSE

# PROJECT CONTEXT

## 1. Contexto del proyecto

Este proyecto analiza los datos transaccionales de un e-commerce del sector cosméticos que ha experimentado una evolución plana durante los últimos meses.

La empresa ha contratado un equipo de consultoría analítica para comprender el comportamiento de sus usuarios, clientes y productos, identificar oportunidades de crecimiento y proponer acciones de CRO (Conversion Rate Optimization) basadas en datos.

El análisis se realizará sobre los datos correspondientes a los últimos tres meses de actividad del e-commerce.

Actualmente se dispone de una base de datos en formato `.db` con aproximadamente 2 millones de registros. La estructura, tablas, variables, relaciones y calidad de los datos aún deben ser investigadas y documentadas durante la fase de comprensión de los datos.

---

## 2. Objetivo de negocio

El objetivo principal es identificar oportunidades que permitan incrementar la facturación global del e-commerce mediante una mejor comprensión del comportamiento de los usuarios y clientes.

Las principales palancas de crecimiento consideradas son:

1. **Más clientes**
   - Incrementar visitas.
   - Mejorar la tasa de conversión.

2. **Mayor frecuencia de compra**
   - Incrementar la recurrencia.
   - Reducir el abandono de clientes.
   - Aumentar el valor generado por cada cliente.

3. **Mayor ticket medio**
   - Incrementar el número de productos por compra.
   - Favorecer la venta cruzada.
   - Identificar oportunidades de incremento del valor de cada pedido.

---

## 3. Objetivos analíticos

El proyecto busca analizar el customer journey completo del e-commerce, desde la llegada del usuario al sitio web hasta la conversión y posterior comportamiento de compra.

Entre las principales áreas de análisis se encuentran:

### Customer Journey

- Comprender el proceso típico de compra.
- Analizar el comportamiento de los usuarios durante las sesiones.
- Analizar views, productos añadidos al carrito y compras.
- Identificar puntos de abandono dentro del funnel.
- Analizar la evolución temporal de los principales indicadores.

### Clientes

- Analizar el comportamiento de compra de los clientes.
- Identificar diferentes perfiles de clientes.
- Analizar frecuencia de compra y gasto.
- Identificar clientes de mayor valor.
- Analizar recurrencia y retención.
- Estimar LTV cuando los datos disponibles lo permitan.
- Evaluar oportunidades de personalización de campañas.

### Productos

- Identificar los productos más vendidos.
- Detectar productos con bajo o nulo volumen de ventas.
- Analizar la relación entre precio y volumen de ventas.
- Identificar productos con muchas visitas pero pocas compras.
- Analizar productos retirados recurrentemente del carrito.
- Evaluar oportunidades de venta cruzada y recomendación personalizada.

---

## 4. Activos analíticos potenciales

El contexto inicial del proyecto plantea la posibilidad de desarrollar:

- Segmentación RFM.
- Análisis de cohortes.
- Análisis de LTV.
- Sistema de recomendación.
- Modelos de Machine Learning.

Estos activos serán considerados como **oportunidades analíticas y no como entregables obligatorios predeterminados**.

La viabilidad y utilidad de cada uno dependerá de la estructura, calidad, granularidad y cobertura temporal de los datos, así como de su potencial impacto sobre el negocio.

---

## 5. Machine Learning

La empresa también está interesada en evaluar la posibilidad de implementar una solución de Machine Learning.

El problema de Machine Learning **no está definido previamente**.

La selección del problema y del modelo será una decisión analítica que deberá surgir del análisis exploratorio, la comprensión del negocio y las características de los datos.

Entre las posibles oportunidades se encuentran, de manera exploratoria:

- Predicción de propensión de compra.
- Predicción de churn.
- Forecasting.
- Recomendación de productos.
- Otras aplicaciones que puedan surgir durante el análisis.

La pregunta principal será:

> **¿Qué solución de Machine Learning tiene mayor potencial para generar impacto de negocio dadas las características reales de los datos?**

No se implementará Machine Learning simplemente por disponer de los datos. Primero se deberá demostrar que existe un problema de negocio adecuado y que una solución predictiva aporta valor frente a alternativas analíticas más simples.

---

## 6. Alcance

El proyecto contempla las siguientes etapas:

1. Comprensión del negocio.
2. Comprensión de la estructura de los datos.
3. Evaluación de la calidad de los datos.
4. Definición de preguntas analíticas.
5. Análisis exploratorio.
6. Análisis del customer journey.
7. Análisis de clientes.
8. Análisis de productos.
9. Segmentación y análisis de cohortes.
10. Análisis de LTV, cuando sea viable.
11. Identificación y priorización de oportunidades de negocio.
12. Evaluación de oportunidades de Machine Learning.
13. Desarrollo y evaluación de la solución analítica seleccionada.
14. Traducción de resultados a recomendaciones de negocio.
15. Documentación y comunicación de resultados.

---

## 7. Estado actual del proyecto

### 7.1 Información confirmada

- Sector: e-commerce de cosméticos.
- Contexto: evolución plana durante los últimos meses.
- Periodo disponible: 1 de octubre de 2019 a 29 de febrero de 2020.
- Formato de datos: base de datos SQLite `.db`.
- Número de tablas: 5.
- Volumen total: 2,095,076 registros.
- Las cinco tablas representan meses consecutivos y presentan el mismo esquema.
- Todas las tablas contienen las siguientes variables:
  - `index`
  - `event_time`
  - `event_type`
  - `product_id`
  - `category_id`
  - `category_code`
  - `brand`
  - `price`
  - `user_id`
  - `user_session`

La base de datos contiene cuatro tipos de eventos:

| Evento | Registros | Participación |
|---|---:|---:|
| `view` | 965,893 | 46.10% |
| `cart` | 585,854 | 27.96% |
| `remove_from_cart` | 415,754 | 19.84% |
| `purchase` | 127,575 | 6.09% |
| **Total** | **2,095,076** | **100%** |

Los eventos observados permiten representar diferentes etapas del customer journey, incluyendo visualización de productos, adición al carrito, eliminación del carrito y compra.

Se confirmó que:

- Un usuario puede tener múltiples sesiones.
- Un usuario tiene un promedio de 2.74 sesiones en el periodo analizado.
- Se observó un máximo de 3,368 sesiones asociadas a un único `user_id`.
- Una sesión puede contener múltiples eventos.
- Una sesión contiene un promedio de 4.67 eventos.
- Se observó un máximo de 5,411 eventos asociados a una única sesión.

Estos valores extremos requieren investigación adicional para determinar si representan comportamiento real, usuarios/sesiones atípicas o posibles problemas de tracking.


### 7.2 Interpretación actual de la estructura

Las observaciones iniciales sugieren que cada fila representa un evento asociado a un usuario, una sesión y un producto en un momento determinado.

Esta interpretación todavía debe validarse mediante un análisis más profundo de la granularidad, los identificadores, los eventos y los posibles casos especiales.

Las cinco tablas mensuales parecen representar particiones temporales del mismo tipo de información, dado que presentan el mismo esquema.

### 7.3 Información todavía por investigar

- Número exacto de registros de cada tabla.
- Distribución de eventos.
- Granularidad exacta de los registros.
- Unicidad y comportamiento de `index`.
- Unicidad y comportamiento de `user_id`.
- Unicidad y comportamiento de `user_session`.
- Posibles relaciones entre usuarios, sesiones y eventos.
- Cobertura temporal exacta de cada tabla.
- Valores faltantes.
- Duplicados.
- Calidad de `event_time`.
- Distribución y valores de `event_type`.
- Comportamiento de `product_id`, `category_id`, `category_code` y `brand`.
- Comportamiento y distribución de `price`.
- Posibles inconsistencias entre tablas mensuales.
- Viabilidad de los análisis RFM, cohortes, LTV y recomendación.
- Oportunidades de Machine Learning.evolución plana durante los últimos meses.
- Periodo disponible: octubre de 2019 a febrero de 2020.
- Formato de datos: base de datos SQLite `.db`.

### 7.4 Observaciones iniciales

- Existe variabilidad en el volumen mensual de eventos.
- `2019-Dec` presenta el menor número de registros del periodo.
- Esta variación no debe interpretarse todavía como una variación del desempeño comercial, ya que el conteo corresponde a eventos y no directamente a visitas, sesiones, conversiones, clientes, pedidos o ingresos.

La evidencia inicial sugiere que cada fila representa un evento asociado a un usuario, una sesión y un producto en un momento determinado.

Sin embargo, todavía no está confirmado que cada registro corresponda a una acción humana única. Se observaron eventos `remove_from_cart` consecutivos sobre el mismo producto en segundos sucesivos, por lo que será necesario investigar la granularidad y posibles duplicados o comportamientos particulares del sistema de tracking.

Los porcentajes de eventos no deben interpretarse como tasas de conversión o funnel, ya que una misma sesión puede generar múltiples eventos de cada tipo.

### 7.5 Cobertura temporal

| Tabla | Registros | Inicio | Fin |
|---|---:|---|---|
| `2019-Oct` | 407,925 | 2019-10-01 00:01:46 UTC | 2019-10-31 23:56:54 UTC |
| `2019-Nov` | 462,833 | 2019-11-01 00:04:51 UTC | 2019-11-30 23:59:27 UTC |
| `2019-Dec` | 351,304 | 2019-12-01 00:01:02 UTC | 2019-12-31 23:59:52 UTC |
| `2020-Jan` | 443,224 | 2020-01-01 00:01:31 UTC | 2020-01-31 23:58:26 UTC |
| `2020-Feb` | 429,790 | 2020-02-01 00:01:43 UTC | 2020-02-29 23:59:54 UTC |
| **Total** | **2,095,076** | **2019-10-01** | **2020-02-29** |

### Por investigar

- Número y nombre de tablas.
- Número exacto de registros por tabla.
- Columnas disponibles.
- Tipos de datos.
- Claves primarias y foráneas.
- Relaciones entre entidades.
- Granularidad de cada tabla.
- Calidad de los datos.
- Valores faltantes.
- Duplicados.
- Cobertura temporal exacta.
- Identificación de usuarios y clientes.
- Disponibilidad de información de sesiones y eventos.
- Disponibilidad de precios y pedidos.
- Viabilidad de RFM, cohortes y LTV.
- Viabilidad de las diferentes alternativas de Machine Learning.

---

## 8. Principio metodológico

El proyecto seguirá una metodología orientada a la resolución de problemas reales de negocio.

No se asumirá previamente que una técnica, modelo o algoritmo determinado sea la solución.

Las decisiones analíticas deberán estar justificadas por:

- El problema de negocio.
- La evidencia encontrada en los datos.
- La calidad y disponibilidad de la información.
- La viabilidad técnica.
- El potencial impacto sobre el negocio.

El objetivo no es únicamente construir modelos, sino **utilizar datos para identificar oportunidades y apoyar mejores decisiones de negocio**.
