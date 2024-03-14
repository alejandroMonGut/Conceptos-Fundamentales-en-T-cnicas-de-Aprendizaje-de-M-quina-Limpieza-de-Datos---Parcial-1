from api import api_gov_data_covid as api
from ui import user_interface as ui
from data_wrangling import dw

print("\nDataFrame filtrado por el departamento de Risaralda (1000 primeros datos)\n\n")

#se trabaja con los datos extraidos filtrados por el departamento de risaralda.
libreria_datos_extraidos = api.extraccion_datos_api("RISARALDA")
ui.impresion_datos_extraidos(libreria_datos_extraidos)

#se realiza el primer paso del data wrangling que es entender los datos
ui.imprimir_informacion_general_y_sumario_df(libreria_datos_extraidos)

#se realiza una imputación de datos para poder manejarlos mejor
dw.imputacion_datos_faltantes(libreria_datos_extraidos)

#se usa typecasting en algunos datos del dataframe para poder ser usados en las funciones plot de pandas y matplotlib
dw.typecasting_datos_requeridos(libreria_datos_extraidos)

print("\nDataFrame después de ser pasado por un proceso de imputación y typecasting\n\n")
#se vuelve a imprimir el dataframe con los valores imputados
ui.impresion_datos_extraidos(libreria_datos_extraidos)

#se vuelve a realizar el primer paso del data Wrangling
ui.imprimir_informacion_general_y_sumario_df(libreria_datos_extraidos)

#se visualizan resultados mediante plots
ui.visualizar_datos_graficas(libreria_datos_extraidos)