from tabulate import tabulate
from data_wrangling import dw
import matplotlib.pyplot as plt
import pandas as pd
#solo admite bibliotecas
def impresion_datos_extraidos (results_df):

    print(tabulate(results_df, tablefmt="github", headers=results_df.keys()))

def imprimir_informacion_general_y_sumario_df (df):

    print("\nInformación general del dataframe:\n")
    print(dw.infomacion_general_df(df))

    print("\nColumnas con valores faltantes: \n" )
    print(dw.informacion_valores_faltantes(df))



    print("\nSumario del dataframe:\n")
    sumario = dw.sumario_df(df)
    print(tabulate(sumario, tablefmt="github", headers=sumario.columns.values.tolist()))
    print("\n")

def visualizar_datos_graficas (df):


    df[["edad","fecha_inicio_sintomas"]].plot.scatter(x="fecha_inicio_sintomas", y="edad", color="blue")
    plt.xlabel("Fecha de inicio de sintomas")
    plt.ylabel("Edad del individuo")

    plt.title("Gráfico de inicio de contagio y edad")


    plt.show()

    conteo_valores = df["estado"].value_counts()

    plt.pie(conteo_valores, labels=conteo_valores.index, autopct="%1.1f%%", colors=["green","orange","red"])
    plt.axis("equal")

    plt.title("Grafico estado de individuos")

    plt.show()

    df["ciudad_municipio_nom"].hist(color="green", xrot=90)
    plt.title("Distribución de los datos en municipios")

    plt.show()