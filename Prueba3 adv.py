import os
from dotenv import load_dotenv

# Cargar las variables del archivo .env
load_dotenv()
# Lee el otro f
eresmid = os.getenv("REDi")
midrec = os.getenv("REDDit")

import praw
import pandas as pd
from pysentimiento import create_analyzer  # Nueva librería para análisis de sentimiento
pd.set_option('display.max_columns', None)
from deep_translator import GoogleTranslator  # Nueva librería para traducción que si es moderna
import time

reddit = praw.Reddit(
    client_id=eresmid,
    client_secret=midrec,
    user_agent="Difficult_Stable4929"
)

#Analizar el post específico

post_url = "1ba7cx4"
post = reddit.submission(id=post_url)

print("Conectando a Reddit y obteniendo comentarios sobre la gentrificación en la CDMX...")


post.comments.replace_more(limit=None)  # Cargar todos los comentarios, incluyendo los escondidos
comments_list=[]

for comment in post.comments.list(): #Aplana la estructura de comentarios
    comments_list.append(comment.body) #Agregar solo el texto del comentario a la lista
print(f"Extracción completa! Yay! Se obtuvieron {len(comments_list)} comentarios.")

df=pd.DataFrame(comments_list, columns=["Frase"])  # Crear un DataFrame con los comentarios

print("Cargando el modelo de IA para análisis de sentimiento...")
analizer= create_analyzer(task="sentiment", lang="es")  # Crear el analizador de sentimiento en español (lang=language)
print ("Modelo cargado!")
Translator=GoogleTranslator(source='es', target='en')  # Configurar el traductor de español a inglés
#Definir una función que analiza UNA frase
def analizar_sentimiento(texto_en_español):
    resultado = analizer.predict(str(texto_en_español))  # Predecir el sentimiento de la frase en español

   #Convertimos a número la polaridad
#POS=1, NEU=0, NEG=-1
    if resultado.output == "POS":
        return 1
    elif resultado.output == "NEU":
        return 0
    elif resultado.output == "NEG":
        return -1         

def traducir_a_ingles(texto_espanol):
    try:
        return Translator.translate(str(texto_espanol))  # Translator es la varible que le dí arriba
    except Exception as e:
        return f"Error de traducción: (e)"
    
print("Analizando frases...")
df["Polaridad"]=df["Frase"].apply(analizar_sentimiento)
print("Traduciendo frases...")
df["Traducción"]=df["Frase"].apply(traducir_a_ingles)
print("Análisis completado!")

print(df)

#Calcular el promedio de polaridad
promedio_total=df["Polaridad"].mean()
print("\n" * 2)
print("Promedio Total de Polaridad:", promedio_total)

print("\n" * 2)

print("CONCLUSIÓN:")

umbral_neutro=0.1 #Definir un umbral para considerar neutralidad

if promedio_total > umbral_neutro:
    print("El sentimiento general es POSITIVO.")
    print("Por lo tanto, la gente está en general a favor de la gentrificación")
elif promedio_total < -umbral_neutro:
    print("El sentimiento general es NEGATIVO.")
    print("Por lo tanto, la gente está en general en contra de la gentrificación")
else:
    print("El sentimiento general es NEUTRO.")
    print("Por lo tanto, la gente no tiene una opinión clara a favor o en contra sobre la gentrificación")

df.to_excel("Analisis_Reddit_Gentrificacion_CDMX.xlsx", index=False)
print("\n" * 2)
print("Resultados guardados en 'Analisis_Reddit_Gentrificacion_CDMX.xlsx'")