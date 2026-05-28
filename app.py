import streamlit as st

from src.carga_datos import cargar_datos_streamlit

from src.procesamiento_datos import (filtrar_por_participante_pandas)

from src.metricas import (
    calcular_senal_promedio_pandas,
    calcular_maximo_senal_pandas,
    calcular_minimo_senal_pandas,
    calcular_fc_desde_datos_pandas)

from src.visualizaciones import (
    graficar_promedio_por_condicion,
    graficar_senal_temporal)

# ---------------------------------------------------
# CONFIGURACION PAGINA
# ---------------------------------------------------

st.set_page_config(
    page_title="Dashboard ECG",
    layout="wide")

# ---------------------------------------------------
# TITULO
# ---------------------------------------------------

st.title("Dashboard de Análisis ECG")

st.sidebar.title("Panel de Control")

# ---------------------------------------------------
# SUBIR CSV
# ---------------------------------------------------

archivo = st.file_uploader(
    "Suba un archivo CSV",
    type=["csv"]
)

# ---------------------------------------------------
# SI HAY ARCHIVO
# ---------------------------------------------------

if archivo is not None:

    try:

        datos = cargar_datos_streamlit(archivo)

    except Exception as e:

        st.error(
            f"Error al cargar archivo: {e}"
        )

    else:

        st.success(
            "Archivo cargado correctamente"
        )

        # ---------------------------------------------------
        # VISTA PREVIA
        # ---------------------------------------------------

        st.subheader("Vista previa de datos")

        st.dataframe(datos.head())

        # ---------------------------------------------------
        # INPUT PARTICIPANTE
        # ---------------------------------------------------

        id_participante = st.sidebar.number_input(
            "Ingrese ID del participante",
            min_value=1,
            step=1
        )

        # ---------------------------------------------------
        # BOTON
        # ---------------------------------------------------

        if st.sidebar.button("Calcular métricas"):

            datos_part = (
                filtrar_por_participante_pandas(
                    datos,
                    id_participante
                )
            )

            # ---------------------------------------------------
            # VALIDAR FILTRADO
            # ---------------------------------------------------

            if datos_part.empty:

                st.error(
                    "No se encontraron datos para ese participante"
                )

            else:

                # ---------------------------------------------------
                # METRICAS
                # ---------------------------------------------------

                try:

                    promedio = (
                        calcular_senal_promedio_pandas(
                            datos_part
                        )
                    )

                    maximo = (
                        calcular_maximo_senal_pandas(
                            datos_part
                        )
                    )

                    minimo = (
                        calcular_minimo_senal_pandas(
                            datos_part
                        )
                    )

                    frecuencia = (
                        calcular_fc_desde_datos_pandas(
                            datos_part
                        )
                    )

                    st.subheader("Indicadores Clave (KPIs)")

                    col1, col2 = st.columns(2)

                    with col1:

                        st.metric(
                            "Promedio ECG",
                            round(promedio, 2)
                        )

                        st.metric(
                            "Máximo ECG",
                            round(maximo, 2)
                        )

                    with col2:

                        st.metric(
                            "Mínimo ECG",
                            round(minimo, 2)
                        )

                        st.metric(
                            "Frecuencia Cardíaca",
                            round(frecuencia, 2)
                        )

                except ValueError as e:

                    st.error(
                        f"Error en métricas: {e}"
                    )

                # ---------------------------------------------------
                # GRAFICOS
                # ---------------------------------------------------

                st.subheader("Visualizaciones")

                try:

                    fig1 = (
                        graficar_promedio_por_condicion(
                            datos
                        )
                    )

                    st.image(
    "graficos/comparacion_categorias.png"
)

                    fig2 = (
                        graficar_senal_temporal(
                            datos_part
                        )
                    )

                    st.image(
    "graficos/evolucion_temporal.png"
)

                except ValueError as e:

                    st.error(
                        f"Error al generar gráficos: {e}"
                    )
