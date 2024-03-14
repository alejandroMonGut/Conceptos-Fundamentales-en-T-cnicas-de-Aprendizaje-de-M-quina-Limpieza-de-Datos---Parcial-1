import pandas as pd
from sodapy import Socrata


def extraccion_datos_api (nombre_departamento):
    # Unauthenticated client only works with public data sets . Note 'None '
    # in place of application token , and no username or password :
    client = Socrata("www.datos.gov.co", None)

    #se trabajan con los primeros 1000 elementos para no saturar los datos por consulta
    results = client.get("gt2j-8ykr", departamento_nom=nombre_departamento, limit=1000 )

    # convierte a biblioteca y lo devuelve
    return pd.DataFrame.from_records(results)



