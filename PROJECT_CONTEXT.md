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

### 7.6 Dataset maestro

Debido a que las cinco tablas mensuales presentan el mismo esquema, se consolidaron mediante `UNION ALL` en una única tabla maestra denominada `master_events`.

La tabla maestra se almacenó en una nueva base de datos:

`data/interim/master_events.db`

Esta base de datos contiene la tabla:

`master_events`

con los 2,095,076 registros correspondientes al periodo octubre de 2019 a febrero de 2020.

La base de datos original `data/raw/ecommerce.db` se mantiene sin modificaciones.

La separación entre `raw` e `interim` permite conservar los datos originales y utilizar una versión consolidada para las siguientes etapas del proyecto.

### Flujo de datos actual

```text
data/raw/ecommerce.db
        │
        │ Consolidación de tablas mensuales
        │ mediante UNION ALL
        ↓
data/interim/master_events.db
        │
        └── master_events
                │
                ↓
       02_data_quality.ipynb

### 7.6 Hallazgos iniciales de Data Quality

#### `category_code`

`category_code` presenta 2,060,411 valores missing, equivalentes al 98.35% de los registros.

El análisis a nivel de producto muestra que el problema es estructural:

| Estado | Productos | % |
|---|---:|---:|
| Completamente missing | 45,527 | 98.89% |
| Completo | 507 | 1.10% |
| Parcial | 4 | 0.01% |
| **Total** | **46,038** | **100%** |

La ausencia del atributo es prácticamente total a nivel de producto, por lo que no parece tratarse de un problema aleatorio de eventos.

No se tomará todavía ninguna decisión de imputación o eliminación. Se investigará si `category_id` puede proporcionar una alternativa analítica más fiable.

#### `brand`

`brand` presenta 891,646 valores missing, equivalentes al 42.56% de los registros.

A nivel de producto:

| Estado | Productos | % |
|---|---:|---:|
| Completo | 22,169 | 48.15% |
| Completamente missing | 20,148 | 43.77% |
| Parcial | 3,721 | 8.08% |
| **Total** | **46,038** | **100%** |

A diferencia de `category_code`, existe un porcentaje relevante de productos con información parcial de marca. Estos productos requieren investigación adicional para determinar si existe una inconsistencia en los registros o una característica propia de la fuente de datos.

#### Interpretación metodológica

Los valores missing se están evaluando teniendo en cuenta la granularidad de cada variable. Para atributos asociados conceptualmente al producto, como `brand` y `category_code`, se analiza también la completitud a nivel de `product_id` y no únicamente a nivel de evento.

### 7.7 Duplicados y unicidad

Se realizaron tres comprobaciones diferentes:

- Filas completamente duplicadas: `0`.
- Registros duplicados excluyendo `index`: `0`.
- Valores duplicados de `index`: `363,983`.

La duplicación de `index` se debe a la consolidación de las cinco tablas mensuales mediante `UNION ALL`. Los mismos valores de `index` aparecen en diferentes meses, llegando algunos a aparecer cinco veces, una por cada tabla mensual.

Por lo tanto:

- No se detectaron duplicados reales de registros.
- `index` no debe considerarse un identificador global de evento.
- La repetición de `index` no será utilizada como criterio para eliminar registros.
- Se evaluará posteriormente si `index` debe conservarse en el dataset analítico o eliminarse por no aportar información de negocio.

## 8. Data Quality — Estado y decisiones

### 8.1 Dataset analizado

El análisis de calidad se realizó sobre la tabla maestra `master_events`, consolidada desde las cinco tablas mensuales originales.

Dataset inicial:

- Registros: 2,095,076
- Columnas: 10
- Periodo: octubre 2019 a febrero 2020

El dataset fue cargado a Pandas para realizar las transformaciones y análisis de calidad.

### 8.2 Transformaciones de tipos

- `event_time` fue convertido de texto a `datetime64[ns, UTC]`.
- Se verificó que la conversión fuera correcta.
- No se detectaron valores `NaT`.
- El rango temporal coincide con el periodo esperado.

### 8.3 Completitud

| Variable | Missing | % Missing | Decisión |
|---|---:|---:|---|
| `event_time` | 0 | 0.00% | Mantener |
| `event_type` | 0 | 0.00% | Mantener |
| `product_id` | 0 | 0.00% | Mantener |
| `category_id` | 0 | 0.00% | Mantener |
| `category_code` | 2,060,411 | 98.35% | Mantener |
| `brand` | 891,646 | 42.56% | Mantener |
| `price` | 0 | 0.00% | Mantener |
| `user_id` | 0 | 0.00% | Mantener |
| `user_session` | 506 | 0.02% | Mantener por ahora |

#### `category_code`

El análisis a nivel de producto mostró que la ausencia es estructural:

- 45,527 productos completamente missing.
- 507 productos completos.
- 4 productos con información parcial.

Por tanto, no se realizará imputación de `category_code`.

`category_id`, que presenta 100% de completitud, será utilizado como referencia categórica principal cuando sea necesario.

#### `brand`

A nivel de producto:

- 22,169 productos tienen `brand` completo.
- 20,148 productos tienen `brand` completamente missing.
- 3,721 productos presentan información parcial.

Se conservarán los valores missing. No se realizará imputación en esta etapa.

### 8.4 Duplicados y unicidad

- Filas completamente duplicadas: 0.
- Registros duplicados excluyendo `index`: 0.
- `index` presenta 363,983 valores duplicados.

La duplicación de `index` se debe a que las cinco tablas mensuales fueron consolidadas mediante `UNION ALL` y el índice original no representa un identificador global de evento.

Por lo tanto:

- No se eliminaron registros por duplicación de `index`.
- `index` fue eliminado del dataset analítico por no aportar información de negocio.

### 8.5 Validación de eventos

Los únicos valores encontrados en `event_type` fueron:

- `view`
- `cart`
- `remove_from_cart`
- `purchase`

No se detectaron valores inválidos.

### 8.6 Validación de identificadores

No se detectaron:

- `product_id` negativos.
- `product_id` iguales a 0.
- `category_id` negativos.
- `category_id` iguales a 0.
- `user_id` negativos.
- `user_id` iguales a 0.

Cardinalidad observada:

- 46,038 productos.
- 508 categorías.
- 163,936 usuarios.

### 8.7 Validación de precios

Se detectaron:

- 11 registros con `price < 0` (0.001%).
- 20,533 registros con `price = 0` (0.98%).

Los 11 registros con precio negativo correspondían a eventos `purchase`. Al no existir en el dataset un evento explícito de devolución que permita justificar estos valores, se consideraron inválidos para el análisis de ventas y fueron eliminados.

Los 20,533 registros con `price = 0` correspondían exclusivamente a eventos:

- `view`
- `cart`
- `remove_from_cart`

No se encontraron compras con precio igual a 0. Estos registros fueron eliminados para evitar distorsiones en análisis posteriores relacionados con precio, ingresos, AOV y LTV.

### 8.8 Dataset procesado

Después de las transformaciones de Data Quality:

- Registros iniciales: 2,095,076
- Registros eliminados: 20,544
- Registros finales: 2,074,532
- Columnas finales: 9

El dataset limpio fue exportado a:

`data/processed/ecommerce_clean.parquet`

El archivo Parquet conserva los tipos de datos, incluyendo `event_time` como datetime con timezone UTC.

### 8.9 Estructura actual de datos

```text
data/
├── raw/
│   └── ecommerce.db
│
├── interim/
│   └── master_events.db
│
└── processed/
    └── ecommerce_clean.parquet

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

## 9. Customer Journey — decisiones metodológicas iniciales

### 9.1 Unidad de análisis: sesión

Para el análisis del customer journey se utilizará `user_session` como identificador de sesión, ya que es la unidad de sesión proporcionada por la fuente.

Antes de adoptar esta decisión se evaluó su consistencia:

- 446,054 sesiones únicas.
- 446,047 sesiones están asociadas a un único usuario.
- 6 sesiones están asociadas a 2 usuarios.
- 1 sesión está asociada a 3 usuarios.
- En total, únicamente 7 sesiones presentan múltiples usuarios, por lo que su impacto es marginal.

También se evaluó una estrategia alternativa de *sessionization* basada en 30 minutos de inactividad. Esta metodología produjo 332,431 sesiones frente a las 446,054 sesiones originales, una reducción del 25.47%.

Debido a que la sessionization de 30 minutos altera sustancialmente la estructura proporcionada por la fuente, se decidió conservar `user_session` como unidad de análisis.

### 9.2 Limitación de duración de sesión

Se detectaron algunas `user_session` con duraciones extremadamente elevadas. Algunas abarcan varios meses, llegando la duración máxima calculada a aproximadamente 217,502 minutos (~151 días).

Esto indica que la diferencia entre el primer y último evento de `user_session` no puede interpretarse de forma fiable como duración real de una sesión de navegación.

Por este motivo:

- No se utilizará `duration_min` como métrica de sesión.
- No se eliminarán sesiones únicamente por presentar una duración elevada.
- No se aplicará una sessionization artificial para corregir este comportamiento.
- El análisis se centrará en la presencia, volumen y comportamiento de los eventos dentro de cada `user_session`.

### 9.3 Radiografía inicial de sesiones

La tabla agregada de sesiones presenta los siguientes resultados:

| Métrica | Media | Mediana | P75 | Máximo |
|---|---:|---:|---:|---:|
| Eventos | 4.65 | 1 | 3 | 2,793 |
| Views | 2.16 | 1 | 2 | 1,005 |
| Carts | 1.29 | 0 | 0 | 778 |
| Remove from cart | 0.92 | 0 | 0 | 2,422 |
| Purchases | 0.29 | 0 | 0 | 259 |

Las distribuciones presentan un fuerte sesgo hacia la derecha. La sesión mediana contiene únicamente un evento, normalmente una visualización, mientras que una proporción reducida de sesiones concentra un volumen elevado de eventos.

Esto sugiere que la mayoría de las sesiones presentan un comportamiento superficial y no avanzan hacia las etapas profundas del customer journey.

### 9.4 Alcance preliminar de eventos por sesión

Porcentaje de sesiones que contienen al menos un evento de cada tipo:

| Evento | % de sesiones |
|---|---:|
| View | 94.41% |
| Cart | 21.78% |
| Remove from cart | 10.77% |
| Purchase | 3.46% |

Estos porcentajes son métricas descriptivas de presencia de eventos por sesión y no se consideran todavía tasas de conversión definitivas.

Para el funnel se utilizará como estructura principal:

**View → Cart → Purchase**

`remove_from_cart` se analizará como una señal de fricción/abandono y no como una etapa obligatoria del funnel.

### 9.5 Resultados descartados

Durante la exploración inicial se calcularon métricas utilizando la primera versión de la tabla de sesiones, incluyendo duración de sesión y una clasificación preliminar de sesiones.

Estas métricas fueron descartadas después de identificar las limitaciones de `user_session` para representar duración real de navegación.

El valor de 3.46% de sesiones con compra se conserva únicamente como estadística descriptiva de presencia de eventos, pero no se interpreta todavía como una tasa de conversión final.

### 9.6 Próximo paso

Construir el Customer Journey/Funnel utilizando `user_session` como unidad de análisis.

Se calcularán y analizarán:

- sesiones que alcanzan cada etapa;
- conversión View → Cart;
- conversión Cart → Purchase;
- conversión global de sesión;
- abandono y señales de fricción asociadas a `remove_from_cart`.

Las definiciones de cada KPI se establecerán antes de interpretar los resultados.
## 10. Customer Journey — línea base de KPIs

Se consolidaron los principales KPIs del Customer Journey utilizando `user_session`
como unidad de análisis. Los indicadores se agrupan en tráfico, conversión,
fricción y facturación.

### 10.1 KPIs de tráfico y usuarios

| KPI | Valor | Definición |
|---|---:|---|
| Sesiones | 446,054 | `user_session` únicas |
| Usuarios únicos | 163,781 | `user_id` únicos |
| Sesiones por usuario | 2.72 | Sesiones / usuarios |
| View Rate | 94.41% | Sesiones con ≥1 `view` / sesiones totales |
| View-only Rate | 75.57% | Sesiones cuya secuencia contiene únicamente `view` / sesiones totales |

### 10.2 KPIs de conversión

| KPI | Valor | Definición |
|---|---:|---|
| Cart Rate | 21.78% | Sesiones con ≥1 `cart` / sesiones totales |
| Purchase Rate | 3.46% | Sesiones con ≥1 `purchase` / sesiones totales |
| View → Cart | 23.07% | Sesiones con `cart` / sesiones con `view` |
| Cart → Purchase | 15.91% | Sesiones con `purchase` / sesiones con `cart` |

La métrica de Purchase Rate se interpreta como **conversión por sesión** y no
como conversión tradicional por orden, debido a que el dataset no contiene un
identificador explícito de transacción.

### 10.3 KPIs de fricción

| KPI | Valor | Definición |
|---|---:|---|
| Cart Remove Rate | 49.46% | Sesiones con `remove_from_cart` / sesiones con `cart` |
| Remove/Cart Event Ratio | 71.39% | Eventos `remove_from_cart` / eventos `cart` |

El Cart Remove Rate indica que aproximadamente la mitad de las sesiones que
registran actividad en carrito también registran al menos una eliminación.

Estas métricas **no se interpretan directamente como tasa de abandono de
carrito**, ya que una sesión puede añadir, eliminar y volver a añadir productos
antes de completar una compra.

### 10.4 KPIs de ventas y facturación

Se creó `df_purchases`, compuesto exclusivamente por eventos
`event_type == "purchase"`.

El dataset presenta una granularidad de **evento de producto comprado** y no
contiene un `order_id` explícito. Por este motivo, algunos indicadores
tradicionales de e-commerce, como AOV por orden, no pueden calcularse
directamente.

| KPI | Valor | Interpretación |
|---|---:|---|
| Purchase Events | 127,564 | Número de eventos `purchase` |
| Compradores | 11,040 | `user_id` únicos con purchase |
| Sesiones con compra | 15,452 | `user_session` únicas con purchase |
| Revenue | 621,549.60 | Suma de `price` en eventos purchase |
| Revenue por comprador | 56.30 | Revenue / compradores |
| Valor medio por evento de compra | 4.87 | Revenue / purchase events |
| Mediana por evento de compra | 3.00 | Mediana de `price` en purchase events |

**Nota:** No se utilizará "Unidades vendidas" como KPI definitivo, ya que no se
ha demostrado que cada evento `purchase` represente necesariamente una unidad
física vendida.

El valor medio de 4.87 se denomina **Valor medio por evento de compra** y no AOV
tradicional, dado que no existe una variable que identifique órdenes.

### 10.5 Hallazgos principales de Customer Journey

Los principales resultados obtenidos hasta esta etapa son:

1. El 75.57% de las sesiones son exclusivamente `view`, indicando un tráfico
   predominantemente superficial.
2. El 94.41% de las sesiones registra al menos un `view`.
3. El 21.78% de las sesiones registra actividad en carrito.
4. El 3.46% de las sesiones registra al menos un `purchase`.
5. La conversión View → Cart es 23.07%.
6. La conversión Cart → Purchase es 15.91%.
7. El 49.46% de las sesiones con actividad de carrito registra al menos un
   `remove_from_cart`.
8. El journey observado no es estrictamente lineal. Existen secuencias como
   `view → cart → view`, `view → cart → remove_from_cart` y
   `cart → view → cart`.
9. Por este motivo, el Customer Journey se analizará como un conjunto de
   comportamientos y transiciones observadas dentro de las sesiones, evitando
   asumir que todos los usuarios siguen un funnel lineal.
10. La principal oportunidad preliminar parece encontrarse en la transición
    desde visualización hacia carrito, aunque se requieren análisis posteriores
    de clientes y productos para determinar las causas y cuantificar el impacto
    económico.

### 10.6 Limitaciones relevantes

- `user_session` se utilizará como unidad de sesión, pero no como medida fiable
  de duración.
- No existe un `order_id` explícito.
- No puede calcularse un AOV tradicional por orden con la información disponible.
- Los eventos `purchase` se tratarán como eventos de compra, no necesariamente
  como unidades físicas.
- `remove_from_cart` se considera una señal de fricción y no una medida directa
  de abandono.
- Los resultados del Customer Journey describen comportamiento observado y no
  establecen causalidad.

### 10.7 Estado del proyecto

**Customer Journey: COMPLETADO**

Se dispone de una línea base de comportamiento, conversión, fricción y
facturación para utilizar como referencia en los siguientes análisis.

Próximas áreas de análisis:

1. Análisis de clientes.
2. Segmentación RFM.
3. Análisis de cohortes.
4. LTV y comportamiento de recompra.
5. Análisis de productos.
6. Sistema de recomendación.
7. Evaluación de oportunidades de Machine Learning.

## 11. Customer Journey — análisis temporal

Se inició el análisis temporal del Customer Journey con el objetivo de identificar
patrones de actividad, conversión y facturación que puedan aportar valor al equipo
comercial y de marketing.

El análisis temporal se dividió en:

1. Tendencia mensual.
2. Patrón semanal.
3. Patrón intradía.
4. Interpretación de negocio.

### 11.1 Tendencia mensual

Se analizaron mensualmente:

- Sesiones.
- Usuarios únicos.
- Sesiones con carrito.
- Sesiones con compra.
- Purchase Rate.
- View → Cart.
- Cart → Purchase.
- Purchase Events.
- Revenue.
- Valor medio por evento de compra.

#### Principales observaciones

**2019-11** destacó como un período particularmente fuerte:

- Aumento de sesiones respecto a octubre.
- Disminución considerable de usuarios únicos.
- Purchase Rate superior al 4%, uno de los valores más altos del período.
- View → Cart disminuyó respecto al mes anterior, aproximadamente de 27% a 24%.
- Cart → Purchase alcanzó aproximadamente 17%, el valor más alto del período.

Esto muestra que un mayor desempeño comercial no necesariamente implica una
mejoría simultánea en todas las etapas del journey.

Posteriormente se observó una disminución progresiva de:

- Purchase Rate: aproximadamente de 4% hacia 3.2%.
- View → Cart: aproximadamente de 27% hacia 22%.

Mientras que Cart → Purchase permaneció relativamente estable.

Esto genera como hipótesis de análisis que la disminución de la conversión global
podría estar relacionada principalmente con una menor conversión de View → Cart,
aunque no se establece causalidad.

#### Revenue y Purchase Events

2019-11 presentó el mayor revenue del período, aproximadamente Bs 140,000.

En 2019-12 se observó una caída importante, hasta aproximadamente Bs 100,000,
seguida posteriormente por una recuperación.

La evolución de Revenue y Purchase Events presentó una trayectoria muy similar,
lo que indica descriptivamente una fuerte asociación entre el volumen de eventos
de compra y la facturación.

Se analizó además el valor medio por evento de compra:

| Mes | Valor medio por evento |
|---|---:|
| 2019-10 | 4.869 |
| 2019-11 | 4.768 |
| 2019-12 | 4.968 |
| 2020-01 | 4.923 |
| 2020-02 | 4.870 |

El valor medio permaneció relativamente estable durante todo el período,
aproximadamente entre 4.77 y 4.97.

Por lo tanto, la variación mensual del revenue parece estar explicada
principalmente por cambios en el volumen de eventos de compra, mientras que el
valor medio por evento presenta poca variación.

Esta interpretación es descriptiva y no implica causalidad.

### 11.2 Patrón semanal

Se analizaron:

- Sesiones.
- Usuarios.
- Events.
- Sesiones con carrito.
- Sesiones con compra.
- Revenue.
- Purchase Rate.
- View → Cart.
- Cart → Purchase.

#### Tráfico

La actividad se concentra principalmente entre martes y jueves:

- Martes: 68,361 sesiones.
- Miércoles: 68,705 sesiones.
- Jueves: 69,021 sesiones.

Los días con menor actividad son:

- Sábado: 58,632 sesiones.
- Domingo: 59,138 sesiones.

Existe por tanto un patrón semanal de mayor actividad entre semana y menor
actividad durante el fin de semana.

#### Conversión

El jueves presentó el Purchase Rate más alto:

- Jueves: 3.61%.
- Lunes: 3.58%.
- Viernes: 3.50%.
- Martes: 3.38%.
- Miércoles: 3.37%.
- Domingo: 3.37%.
- Sábado: 3.14%.

El sábado presentó simultáneamente el menor volumen de sesiones y el menor
Purchase Rate.

#### Revenue

El jueves fue el día con mayor revenue:

- Jueves: Bs 101,597.
- Viernes: Bs 93,569.
- Lunes: Bs 92,364.
- Martes: Bs 91,278.
- Miércoles: Bs 88,977.
- Domingo: Bs 79,925.
- Sábado: Bs 73,840.

El jueves destaca por combinar alto volumen de tráfico, mayor Purchase Rate y
mayor revenue.

#### Etapas del Customer Journey

View → Cart presentó su valor máximo el miércoles (24.57%), seguido por
domingo (24.16%) y lunes (24.15%).

Cart → Purchase presentó sus valores más altos el viernes (16.98%) y jueves
(16.89%).

Esto demuestra que las distintas etapas del journey no presentan necesariamente
el mismo comportamiento temporal.

Por ejemplo:

- Miércoles presenta el mayor View → Cart, pero un Cart → Purchase relativamente
  menor.
- Jueves presenta un View → Cart inferior al miércoles, pero un Cart → Purchase
  considerablemente mayor.

Por lo tanto, no se debe optimizar una única etapa del funnel de manera aislada.

### 11.3 Hipótesis y oportunidades preliminares

Los análisis temporal mensual y semanal generan las siguientes hipótesis para
investigaciones posteriores:

1. La caída de conversión observada durante el período podría estar relacionada
   principalmente con una menor conversión View → Cart.
2. Las variaciones de revenue parecen estar asociadas principalmente con cambios
   en el volumen de eventos de compra, dado que el valor medio por evento se
   mantiene relativamente estable.
3. El jueves representa un período de alto desempeño comercial.
4. El sábado presenta una combinación de menor tráfico y menor conversión.
5. Las diferentes etapas del Customer Journey responden de manera diferente a la
   temporalidad.
6. Los patrones semanales podrían tener implicaciones para la planificación de
   campañas y acciones comerciales, pero no deben convertirse todavía en
   recomendaciones causales.

### 11.4 Limitaciones del análisis temporal

- El dataset contiene únicamente cinco meses de información, por lo que no es
  suficiente para establecer estacionalidad anual.
- No se dispone de información sobre canal de adquisición, campaña o fuente de
  tráfico.
- Las diferencias temporales son descriptivas y no permiten determinar
  causalidad.
- `user_session` presenta limitaciones para análisis de duración temporal, por lo
  que el análisis se concentra en comportamiento agregado por período.
- Revenue se calcula a partir de eventos `purchase`.
- No existe `order_id`, por lo que el valor medio utilizado corresponde a eventos
  de compra y no a órdenes.

### 11.5 Estado actual

**Customer Journey: COMPLETADO**

**Análisis temporal: 5.1 Tendencia mensual — COMPLETADO**

**Análisis temporal: 5.2 Patrón semanal — COMPLETADO**

**Pendiente:**
- 5.3 Patrón intradía.
- 5.4 Interpretación final de negocio.
- Análisis de abandono y recuperación de carrito.
- Insights CRO.

### 11.6 Próximo paso

Continuar con **5.3 Patrón intradía**, utilizando la variable `hour` para
analizar volumen de actividad, conversión, revenue y posibles señales de
fricción según la hora del día.

### Hipótesis pendiente — intención nocturna y conversión diurna

El análisis intradía identificó una diferencia relevante entre las etapas del Customer Journey:

* `View → Cart` presenta mayores niveles durante aproximadamente **21:00–01:00**.
* `Cart → Purchase` presenta mayores niveles principalmente durante aproximadamente **06:00–23:00**.
* El tráfico, revenue y sesiones con compra se concentran principalmente durante el período diurno.

Esto genera una hipótesis de comportamiento:

> **Los usuarios podrían desarrollar intención de compra durante la noche y completar la compra posteriormente durante el día.**

Esta hipótesis **NO ha sido validada**. Las métricas actuales están agregadas por hora y no permiten determinar si los eventos nocturnos y diurnos pertenecen al mismo usuario.

### Acción futura

Investigar durante el notebook de **Customer Analysis** utilizando:

* `user_id`
* `user_session`
* `event_time`
* `event_type`
* `product_id`

El objetivo será determinar si existe una transición temporal a nivel individual:

`View/Cart nocturno → Compra posterior`

y, de existir, medir:

* proporción de usuarios que realizan este comportamiento;
* tiempo entre intención y compra;
* hora de inicio y finalización del journey;
* comportamiento entre sesiones;
* productos o categorías involucradas, si la estructura del dataset lo permite.

**Prioridad:** hipótesis relevante para Customer Analysis.

**Estado:** pendiente de validación.
