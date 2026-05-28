import matplotlib.pyplot as plt

#Gráfico de barras comparativo
def graficar_promedio_por_condicion(df):

    # Agrupar datos por condición experimental
    metricas_agrupadas = df.groupby("condicion_experimental")["valor"].mean()

    # Configuración del gráfico
    fig, ax = plt.subplots(figsize=(9,5))
    

    # Crear gráfico de barras
    metricas_agrupadas.plot(kind='bar',color='#1e3a8a',edgecolor='black',alpha=0.8, ax=ax)

    # Personalización
    ax.set_title('Promedio de Señal por Condición Experimental')

    ax.set_xlabel('Condición Experimental')

    ax.set_ylabel('Valor Promedio')

    ax.grid(True,linestyle='--',alpha=0.5,axis='y')

    return fig
    
#Gráfico de líneas continuas

def graficar_senal_temporal(datos_part):

    # Configuración del lienzo
    fig, ax = plt.subplots(figsize=(11,5))

    # Gráfico de líneas desde el DataFrame
    datos_part.plot(kind='line',x='tiempo',y='valor',color='#b45309',linewidth=1.5,ax=ax)

    # Personalización
    ax.set_title('Evolución Temporal de la Señal ECG')

    ax.set_xlabel('Tiempo')

    ax.set_ylabel('Valor de la Señal')

    ax.grid(True,linestyle=':',alpha=0.6)
    
    return fig
