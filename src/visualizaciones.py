import matplotlib.pyplot as plt

#Gráfico de barras comparativo
def graficar_promedio_por_condicion(df):

    # Agrupar datos por condición experimental
    metricas_agrupadas = df.groupby("condicion_experimental")["valor"].mean()

    # Configuración del gráfico
    plt.figure(figsize=(9, 5))

    # Crear gráfico de barras
    metricas_agrupadas.plot(kind='bar',color='#1e3a8a',edgecolor='black',alpha=0.8)

    # Personalización
    plt.title('Promedio de Señal por Condición Experimental')

    plt.xlabel('Condición Experimental')

    plt.ylabel('Valor Promedio')

    plt.xticks(rotation=0)

    plt.grid(True,linestyle='--',alpha=0.5,axis='y')

    plt.tight_layout()

    # Guardar gráfico
    plt.savefig('graficos/comparacion_categorias.png',dpi=300)

    plt.close()
    
#Gráfico de líneas continuas

def graficar_senal_temporal(datos_part):

    # Configuración del lienzo
    plt.figure(figsize=(11, 5))

    # Gráfico de líneas desde el DataFrame
    datos_part.plot(kind='line',x='tiempo',y='valor',color='#b45309',linewidth=1.5,ax=plt.gca())

    # Personalización
    plt.title('Evolución Temporal de la Señal ECG')

    plt.xlabel('Tiempo')

    plt.ylabel('Valor de la Señal')

    plt.grid(True,linestyle=':',alpha=0.6)

    plt.tight_layout()

    # Guardar gráfico
    plt.savefig('graficos/evolucion_temporal.png',dpi=300)

    plt.close()
