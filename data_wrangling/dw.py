import pandas as pd

def infomacion_general_df (df):
    return df.info()

def sumario_df(df):
    return df.describe()

def informacion_valores_faltantes(df):
    #retorna columnas con datos faltantes
    return df.columns[df.isnull().any()].tolist()

def typecasting_datos_requeridos(df):
    df["fecha_inicio_sintomas"] = pd.to_datetime(df["fecha_inicio_sintomas"])
    df["edad"] = pd.to_numeric(df["edad"])


def imputacion_datos_faltantes(df):

    #si no aparece su país de origen, se presupone que es colombia
    df["pais_viajo_1_nom"] = df["pais_viajo_1_nom"].fillna("COLOMBIA")

    #si no tiene algún tipo de recuperación, es poque el individuo falleció
    df["tipo_recuperacion"] = df["tipo_recuperacion"].fillna("Fallecido")

    #aquellos que no tengan dato de su estado, serán eliminados del dataframe
    df.dropna(subset=["estado"])