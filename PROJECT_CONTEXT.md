# Contexto del proyecto — E-commerce Cosmetics Analytics

> Documento de continuidad para retomar el proyecto en un chat nuevo. Resume el estado vigente, las decisiones metodológicas y el trabajo priorizado; no es una bitácora cronológica.

## 1. Propósito y objetivo de negocio

El proyecto analiza la actividad de un e-commerce de cosméticos para identificar oportunidades de crecimiento de la facturación. El negocio ha presentado una evolución plana y dispone de cinco meses de datos transaccionales y de navegación.

Las palancas de crecimiento son:

1. Más clientes: aumentar tráfico y conversión.
2. Mayor frecuencia de compra: recurrencia, retención y valor por cliente.
3. Mayor ticket: más productos por compra y venta cruzada.

El análisis debe traducir la evidencia en hipótesis y recomendaciones accionables. No se debe asumir causalidad ni proponer Machine Learning sin demostrar primero que resuelve un problema de negocio mejor que una alternativa más simple.

## 2. Datos y activos disponibles

### Fuente y cobertura

- Fuente original: SQLite \`data/raw/ecommerce.db\` (no modificar).
- Periodo: 2019-10-01 a 2020-02-29, en UTC.
- Cinco tablas mensuales con el mismo esquema: \`2019-Oct\`, \`2019-Nov\`, \`2019-Dec\`, \`2020-Jan\` y \`2020-Feb\`.
- Registros originales: 2,095,076.
- Dataset maestro intermedio: \`data/interim/master_events.db\`, tabla \`master_events\`, creada mediante \`UNION ALL\`.
- Dataset analítico vigente: \`data/processed/ecommerce_clean.parquet\`.

### Variables

\`event_time\`, \`event_type\`, \`product_id\`, \`category_id\`, \`category_code\`, \`brand\`, \`price\`, \`user_id\` y \`user_session\`.

\`index\` existía en la fuente, pero se eliminó del dataset analítico: se repite entre meses y no es un identificador global de evento.

### Granularidad e interpretación

Cada fila representa un evento asociado a un usuario, sesión, producto y momento temporal. Los únicos eventos válidos son \`view\`, \`cart\`, \`remove_from_cart\` y \`purchase\`. Los datos no contienen \`order_id\`; un evento \`purchase\` representa una compra de producto observada, no necesariamente una orden ni una unidad física.

## 3. Calidad de datos y decisiones vigentes

El parquet limpio contiene 2,074,532 registros y 9 columnas. Se eliminaron 20,544 registros: 11 \`purchase\` con precio negativo y 20,533 eventos no-compra con precio igual a cero. \`event_time\` fue validado como \`datetime64[ns, UTC]\` sin valores inválidos. No hay filas completamente duplicadas ni duplicados al excluir \`index\`.

| Aspecto | Estado / decisión |
|---|---|
| \`category_code\` | 98.35% missing; ausencia estructural a nivel producto. No imputar ni usar como categoría principal. |
| \`category_id\` | 100% completo; referencia categórica principal. |
| \`brand\` | 42.56% missing; conservar nulos, sin imputación. |
| \`user_session\` | 506 missing (0.02%); conservar por ahora y tratar explícitamente al agregar por sesión. |
| Identificadores | 46,038 productos, 508 categorías y 163,936 usuarios en la validación de calidad. Sin ceros ni negativos. |
| Precio | Analizar revenue solo desde eventos \`purchase\`; no hay compras con precio cero tras limpieza. |

## 4. Decisiones metodológicas transversales

- Separar siempre **evidencia**, **hipótesis**, **acción** y **validación**.
- Las métricas agregadas describen asociaciones; no prueban causas.
- Usar \`user_session\` como unidad de análisis del Customer Journey. Es la sesión proporcionada por la fuente y su reasignación con una regla de 30 minutos alteraría sustancialmente los resultados.
- No usar la diferencia entre primer y último evento como duración de sesión: existen sesiones de hasta ~151 días y no representa navegación real.
- \`remove_from_cart\` es una señal de fricción, no abandono por sí misma.
- Revenue = suma de \`price\` en eventos \`purchase\`. No llamar AOV al valor medio por evento de compra, porque no existe \`order_id\`.
- Al priorizar oportunidades, combinar tasa, volumen y potencial económico; no ordenar solo por un porcentaje extremo con pocas observaciones.

## 5. Customer Journey — trabajo completado

El notebook \`notebooks/03_customer_journey_analysis.ipynb\` tiene completados:

- radiografía de sesiones;
- funnel y KPIs de tráfico, conversión, fricción y facturación;
- análisis mensual, semanal e intradía;
- abandono de carrito y recuperación posterior;
- abandono por producto y categoría;
- evolución temporal de abandono;
- interpretación de negocio e insights CRO;
- exploración inicial de correlaciones de revenue.

### Línea base de KPIs

| KPI | Valor | Definición / nota |
|---|---:|---|
| Sesiones | 446,054 | \`user_session\` únicas |
| Usuarios | 163,781 | \`user_id\` únicos en el análisis de journey |
| Sesiones por usuario | 2.72 | Sesiones / usuarios |
| View rate | 94.41% | Sesiones con al menos un \`view\` |
| View-only rate | 75.57% | Sesiones con solo \`view\` |
| Cart rate | 21.78% | Sesiones con al menos un \`cart\` |
| Purchase rate | 3.46% | Sesiones con al menos un \`purchase\` |
| View → Cart | 23.07% | Sesiones con cart / sesiones con view |
| Cart → Purchase | 15.91% | Sesiones con purchase / sesiones con cart |
| Cart remove rate | 49.46% | Sesiones con remove / sesiones con cart |
| Purchase events | 127,564 | Eventos \`purchase\` tras limpieza |
| Compradores | 11,040 | Usuarios con purchase |
| Sesiones con compra | 15,452 | Sesiones con purchase |
| Revenue | Bs 621,549.60 | Suma de precios de eventos \`purchase\` |
| Revenue por comprador | Bs 56.30 | Revenue / compradores |
| Valor medio por evento de compra | Bs 4.87 | No equivale a AOV por orden |

### Lectura consolidada

- El tráfico es mayoritariamente superficial: 75.57% de las sesiones contiene exclusivamente views.
- La principal oportunidad del funnel es \`View → Cart\`: disminuyó durante el período, mientras que \`Cart → Purchase\` fue relativamente más estable.
- El funnel no debe modelarse como una secuencia estricta: se observan recorridos como \`view → cart → view\` y \`cart → view → cart\`.
- Noviembre de 2019 fue el mes con mayor revenue (~Bs 140,000); diciembre cayó (~Bs 100,000) y luego hubo recuperación. El valor medio por evento permaneció estable (~Bs 4.77–4.97), por lo que el revenue parece variar sobre todo con el volumen de eventos de compra.
- La actividad y el revenue se concentran más entre martes y jueves; jueves tuvo el mayor revenue y purchase rate. Sábado tuvo menor actividad y conversión.
- Intra-día: \`View → Cart\` es mayor aproximadamente entre 21:00–01:00, mientras que \`Cart → Purchase\`, tráfico, revenue y sesiones con compra se concentran en el período diurno.

## 6. Abandono y recuperación

Definición de abandono intra-sesión: sesión con al menos un \`cart\` y sin \`purchase\` en esa misma \`user_session\`.

| Métrica | Resultado |
|---|---:|
| Sesiones abandonadas | 84,581 |
| Usuarios que abandonaron | 35,791 |
| Tasa de abandono intra-sesión | ~87% |
| Usuarios recuperados posteriormente | 6,525 |
| Recovery rate | 18.23% |

Un usuario recuperado tuvo una sesión abandonada y posteriormente al menos un evento \`purchase\`. Esto no prueba que haya comprado el mismo producto ni que la compra haya sido causada por una acción de recuperación.

Resultados adicionales:

- Existen productos con abandono muy alto (hasta 100%), pero la tasa aislada no basta para priorizar: debe combinarse con carritos, precio, categoría, marca y compras.
- En categorías, el abandono alto suele coincidir con menor volumen. Usar al menos \`abandonment rate + cart volume\` para priorizar.
- La tasa mensual de abandono se movió aproximadamente entre 82.45% y 87.25%. No se observó relación lineal clara entre tasa de abandono y revenue.
- El conteo de sesiones abandonadas sí se asocia positivamente a revenue, pero probablemente por actividad general (\`más tráfico → más carritos y más compras\`); no interpretarlo como efecto causal.

## 7. Oportunidades CRO vigentes

Estas son hipótesis priorizadas, no causas demostradas.

| Prioridad | Evidencia | Hipótesis / siguiente validación |
|---|---|---|
| Alta | \`View → Cart\` de 23.07% y deterioro temporal | Auditar páginas de producto, priorizando alto view, bajo paso a cart y abandono alto. Evaluar propuesta de valor, información, precio, disponibilidad y CTA. |
| Alta | ~87% de abandono intra-sesión | Auditar cualitativamente \`Cart → Checkout → Pago → Confirmación\`: pasos, costos, confianza, errores, disponibilidad, pagos y experiencia móvil. |
| Media-alta | 18.23% de abandonadores compra después | Antes de remarketing, medir tiempo hasta compra, producto/categoría abandonados, sesiones posteriores y comportamiento posterior. |
| Variable | Diferencias por producto y categoría | Priorizar con tasa, volumen de carritos y potencial económico. |
| Por validar | Intención nocturna y conversión diurna | Confirmar a nivel individual antes de diseñar intervenciones horarias. |

El marco requerido para recomendaciones CRO es:

\`Evidencia → Hipótesis → Intervención → Experimento → Resultado\`

## 8. Customer Analysis — estado vigente

El notebook \`notebooks/04_customer_analysis.ipynb\` está iniciado. Su objetivo es
trasladar el análisis de **evento → sesión → usuario** para comprender conversión,
recurrencia, comportamiento entre sesiones, recuperación e intención de compra.
RFM, cohortes, LTV y forecasting permanecen reservados para notebooks posteriores.

### Preparación y tratamiento de sesiones nulas

La fase de carga está completada: se utilizó el parquet limpio sin aplicar nuevas
transformaciones. Se construyó \`customer_summary\`, con una fila por \`user_id\` y
las variables \`known_sessions\`, \`events\`, \`active_days\`,
\`products_interacted\`, \`cart_events\`, \`purchase_events\`, \`revenue\` y
\`events_without_session\`.

\`known_sessions\` cuenta solo sesiones identificables; no equivale a ausencia de
actividad cuando vale cero. Hay 506 eventos (0.02%) con \`user_session\` nulo,
pertenecientes a 146 usuarios (0.089%): 417 son \`cart\`, 85
\`remove_from_cart\`, 4 \`view\` y ninguno \`purchase\`. De ellos, 130 usuarios
tienen además sesiones válidas y 16 solo actividad sin sesión identificable.

**Decisión:** no imputar \`user_session\`. Conservar estos eventos en análisis a
nivel usuario mediante \`user_id\`, pero excluirlos de métricas que requieran una
sesión específica.

### Radiografía de clientes completada

| Métrica | Valor |
|---|---:|
| Usuarios únicos | 163,781 |
| Usuarios compradores | 11,040 |
| Usuarios no compradores | 152,741 |
| User conversion rate | 6.74% |
| Usuarios con una sesión conocida | 108,362 |
| Usuarios con 2+ sesiones conocidas | 55,403 |
| Single-session rate | 66.16% |
| Repeat user rate | ~33.8% |

Se debe verificar una discrepancia de 16 usuarios entre el total y la suma de
usuarios de una sesión y usuarios recurrentes antes de cerrar esa métrica.

Las distribuciones son fuertemente asimétricas: la media frente a la mediana es
2.72 vs. 1 en sesiones conocidas, 12.67 vs. 2 en eventos, 6.22 vs. 1 en productos
interactuados, 3.51 vs. 0 en carts, 0.78 vs. 0 en purchases y Bs 3.80 vs. 0 en
revenue. Una minoría de usuarios altamente activos eleva las medias; el usuario
típico interactúa poco.

### Concentración de revenue

La concentración debe calcularse **solo entre compradores**, no sobre todos los
usuarios: como solo 6.74% compra, el top 10% de todos los usuarios contiene por
definición a todos los usuarios con revenue positivo y produce un resultado inútil
de 100%.

Entre los 11,040 compradores, el top 10% (1,104 usuarios) generó Bs 263,768.62,
equivalente al **42.44%** de los Bs 621,549.60 de revenue. Es una concentración
descriptiva relevante, pero no prueba fidelidad, valor futuro, rentabilidad ni una
dependencia estructural. La clasificación es retrospectiva y usa revenue acumulado
del período.

### Próximos análisis priorizados

1. Completar la curva de concentración entre compradores: top 1%, 5%, 10%, 20% y 50%.
2. Comparar usuarios compradores vs. no compradores.
3. Analizar distribución de sesiones por usuario, recurrencia y comportamiento entre sesiones.
4. Validar la hipótesis **intención nocturna → compra diurna** a nivel individual,
   usando \`user_id\`, \`user_session\`, \`event_time\`, \`event_type\` y, cuando
   aporte valor, \`product_id\` y \`category_id\`.

Para la hipótesis nocturna, medir proporción de usuarios con \`view\`/\`cart\`
nocturno que compra después, tiempo hasta la compra, ocurrencia en la misma o en
otra sesión y coincidencia de producto o categoría cuando sea posible.

Después, evaluar segmentación RFM, cohortes, retención, recompra, LTV (solo cinco
meses y sin \`order_id\`) y análisis de productos/venta cruzada según viabilidad.

## 9. Machine Learning y forecasting

No existe un problema de ML predefinido. Su implementación depende de que el análisis demuestre valor y permita una validación temporal robusta.

Línea exploratoria vigente: forecasting de volumen de compras y, después, estimación de revenue. La correlación diaria entre \`purchase_events\` y revenue fue 0.969, pero es principalmente estructural (\`purchase events × precio ≈ revenue\`) y no demuestra capacidad predictiva futura. Evitar data leakage: los predictores deben estar disponibles antes del período objetivo.

Antes de modelar, investigar tendencia, estacionalidad, autocorrelación, outliers, predictores disponibles y validación temporal fuera de muestra. Otras alternativas solo deben considerarse si la evidencia lo justifica: propensión de compra, churn o recomendación.

## 10. Estructura de trabajo

\`\`\`text
data/raw/ecommerce.db                  # fuente inmutable
data/interim/master_events.db          # consolidación de tablas mensuales
data/processed/ecommerce_clean.parquet # fuente analítica principal
notebooks/01_data_understanding.ipynb
notebooks/02_data_quality.ipynb
notebooks/03_customer_journey_analysis.ipynb
notebooks/04_customer_analysis.ipynb   # próxima prioridad
notebooks/05_product_analysis.ipynb
notebooks/06_rfm_segmentation.ipynb
notebooks/07_cohort_analysis.ipynb
notebooks/08_ltv_analysis.ipynb
notebooks/09_advanced_analytics.ipynb
notebooks/10_ml_solution.ipynb
src/                                   # funciones reutilizables
reports/business_report.md             # síntesis ejecutiva final
\`\`\`

## 11. Checklist al reiniciar el trabajo

1. Cargar \`data/processed/ecommerce_clean.parquet\`; no repetir limpieza salvo que se encuentre un problema nuevo.
2. Confirmar el estado del notebook que se va a continuar antes de modificarlo.
3. Mantener las definiciones de KPI anteriores para comparabilidad.
4. Documentar nuevas decisiones, resultados, limitaciones y próximo paso en este archivo, sustituyendo estado superado en lugar de añadir actualizaciones cronológicas duplicadas.
