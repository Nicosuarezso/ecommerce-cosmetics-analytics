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

### Conocido

- Sector: e-commerce de cosméticos.
- Contexto: evolución plana durante los últimos meses.
- Periodo de datos: últimos tres meses.
- Volumen aproximado: 2 millones de registros.
- Formato de datos: base de datos `.db`.
- Objetivo principal: identificar oportunidades para incrementar la facturación.
- Áreas principales: customer journey, clientes y productos.
- Posible uso de Machine Learning: sí, sujeto a evaluación.

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
