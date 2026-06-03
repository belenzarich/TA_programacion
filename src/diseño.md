# Diseño del Sistema PulseLab

## Descripción General

El sistema PulseLab permite analizar señales fisiológicas registradas en archivos CSV. El programa carga los datos experimentales, realiza validaciones defensivas, calcula métricas descriptivas y genera visualizaciones para facilitar el análisis de los participantes.

El proyecto posee dos formas de ejecución:

* **main.py**: ejecución por consola.
* **app.py**: dashboard web desarrollado con Streamlit.

---

## Arquitectura del Sistema

### Frontend

* Streamlit (`app.py`)
* Interfaz web para carga de archivos CSV.
* Visualización de métricas mediante tarjetas KPI.
* Visualización de gráficos generados por el backend.

### Backend

Implementado mediante módulos independientes dentro de `src/`.

#### carga_datos.py

Responsable de:

* Cargar archivos CSV.
* Validar estructura y contenido.
* Detectar valores inválidos.
* Retornar DataFrames de Pandas.

#### procesamiento_datos.py

Responsable de:

* Filtrar registros por participante.
* Preparar subconjuntos de datos para análisis.

#### metricas.py

Responsable de:

* Calcular promedio de señal.
* Calcular máximos y mínimos.
* Detectar picos QRS.
* Estimar frecuencia cardíaca.

#### visualizaciones.py

Responsable de:

* Generar gráficos de barras por condición experimental.
* Generar gráficos temporales de la señal.
* Exportar imágenes en la carpeta `graficos/`.

---

## Flujo de Ejecución

1. El usuario carga un archivo CSV.
2. El sistema valida los datos.
3. Si existe un error, se muestra un mensaje mediante `st.error()`.
4. Si los datos son válidos:

   * Se muestran los primeros registros.
   * Se selecciona un participante.
   * Se calculan métricas descriptivas.
   * Se generan gráficos.
   * Se muestran KPIs y visualizaciones en la interfaz.

---

## Tecnologías Utilizadas

* Python
* Pandas
* Matplotlib
* Streamlit

---

## Estructura del Proyecto

```text
TA_programacion/
│
├── app.py
├── main.py
├── prompts_dashboard.txt
├── README.md
├── datos/
├── diagramas/
├── graficos/
└── src/
    ├── diseño.md
    ├── carga_datos.py
    ├── procesamiento_datos.py
    ├── metricas.py
    └── visualizaciones.py
```
