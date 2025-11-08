import pandas as pd
from bertopic import BERTopic
from sklearn.feature_extraction.text import CountVectorizer
pd.set_option("display.max_columns", None)
import nltk
from nltk.corpus import stopwords #nltk es la librería de procesamiento de lenguaje natural más usada
#.corpus es el archivo
nltk.download("stopwords")


print ("Iniciando el Projecto 2 - Topic Modeling....")

#Descargar del excel ya creado los datos
print ("Cargando datos desde el archivo Excel del Análisis de Gentrificación en la CDMX...")
df= pd.read_excel("Analisis_Reddit_Gentrificacion_CDMX.xlsx")

#Limpio los datos quitando las filas vacías y lo convierto en una lista
print("Limpiando datos...")
df.dropna(subset=["Frase"], inplace=True) #df.dropna() "dropea" (borra) las filas con valores NaN
#subset=["Frase"] es para que pandas solo se fije en la columna "Frase" para eliminar filas vacías
#inplace=True hace que el cambio se aplique directamente al Data Frame original (Si fuera False se crearía una copia)

comentarios = df["Frase"].astype(str).tolist() #Todos los elementos de la columna aquí se convierten a string
#.tolist() convierte la columna de strings a una lista de python

print (f"Se cargaron {len(comentarios)} comentarios para anazlizar.")

print("\n" * 2)
print("Creando filtro de stop words con lista personalizada...")

custom_stop_words=["removed",
                   "comment",
                   "https",
                   "www",
                   "com",
                   "cdmx",
                   "jajaj",
                   "jajaja",
                   "jajajjaja",
                   "jaja",
                   "jeje",
                   "jejeje",
                   "pues",
                   "gente",
                   "pensé",
                   "pongan",
                   "digo",
                   "xd",
                   "si",
                   "lol"
]

lista_stop_words_espanol = stopwords.words('spanish')
lista_stop__words_total= lista_stop_words_espanol + custom_stop_words
vectorizer = CountVectorizer(stop_words=lista_stop__words_total)
#CountVectorizer convierte el texto en una matriz de conteo de palabras
#Quita las palabras vacías en español usando la lista de stopwords de nltk (de "relleno")


#Ahora sí, a hacer Topic Modeling con el AI

print("Cargando el modelo de Topic Modeling.......")
print("Esto puede tardar varios minutos")

#Aquí se crea el modelo
topic_model=BERTopic(language="multilingual", 
                     vectorizer_model=vectorizer,
                     calculate_probabilities=True, 
                     verbose=True, 
                     min_topic_size=5) #Éste lo agregué porque había muchos sin tema, entonces reduje el tamaño mínimo de tema a 5 comentarios en lugar de 10
#topic_model=Bertopic() crea el modelo de IA para Topic Modeling y lo guarda en la variable
#Calculate_probabilities=True hace que el modelo sea más detallado, que no sólo diga "esto es de tal tema" sino que calcule la probabilidad de "esto tiene un 80% de tal tema y un 20% de tal otro tema"
#verbose=True hace que el modelo imprima en la Terminal frases para saber en qué parte del proceso va y si no se trabó


#Aquí se entrena el modelo con los comentarios
print("Entrenando el modelo con los comentarios...")
topics, probabilities= topic_model.fit_transform(comentarios)
#.fit() lee los comentarios y entrena al modelo. Comparando los comentarios entre sí, el modelo encuentra patrones y temas comunes
#.transform() aplica el modelo entrenado (.fit) a los comentarios y les asigna un numero de tema
#Devuelve dos listas: topics y probabilities 
#topics es una lista con el número de tema asignado a cada comentario
#probabilities es una lista con la probabilidad de que el comentario pertenezca a ese tema. Como le pedí calculate_probabilities=True arriba, esta lista guarda esas probabilties y se genera
print("Modelo entrenado! Tópicos asignados.")

#Ahora a ver los temas encontrados
#El tópico -1 es para comentarios que no se pudieron agrupar en ningún tema
print("\n" * 2)
print("Modelos de Tópicos")
print(topic_model.get_topic_info()) #topic_ es el número de tema y Count es el número de comentarios en ese tema
#Representation es una lista de palabras clave que describen el tema
print("\n" * 2)
print("Los temas que tienen -1 son comentarios que no se pudieron agrupar en ningún tema.")

#Los guardo en un excel
topic_model.get_topic_info().to_csv("topics_summary.csv", index=False)
#topic_model.get_topic_info() recolecta la tabla de temas
#.to_csv() la guarda en un archivo CSV llamado "topics_summary.csv"
#index=False hace que no se guarde una columna extra de índices en el archivo
print("\n" * 2)
print("Guardando los resultados en un archivo Excel...")

#Grafico de Barchart
barchart = topic_model.visualize_barchart(top_n_topics=10) #Enseña los 10 tópicos principales
barchart.write_html("visualizacion_barchart.html") #.write_html guarda el gráfico en un archivo HTML (página web)

#Heat map (No hubo temas suficientes para hacer un heatmap)
#heatmap = topic_model.visualize_heatmap(n_clusters=5, top_n_topics=10) 
#n_clusters=5 agrupa los temas similares en 5 grupos
#top_n_topics=10 muestra los 10 temas principales en el heatmap
#heatmap.write_html("visualizacion_heatmap.html")

print("\n" * 2)
print("Análisis de Topic Modeling completado!")
print("\n" * 2)
print("Revisa los archivos 'topics_summary.csv', 'visualizacion_barchart.html' y 'visualizacion_heatmap.html' en tu carpeta.")
print("Abre los archivos HTML en tu navegador para ver las visualizaciones interactivas.")
print("\n" * 2)

#Conclusión
print("CONCLUSIÓN:")
resumen_temas=pd.read_csv("topics_summary.csv") #Lee el archivo CSV que guardé antes con los temas
tema_reales=resumen_temas[resumen_temas.Topic != -1] #Quita el tema -1 (sin tema) #!= sinifica que no es igual a, entonces compara uno por uno
tema_principal=tema_reales.loc[tema_reales['Count'].idxmax()] #.loc accede a una fila específica
#.idxmax() encuentra el índice de la fila con el valor máximo en la columna 'Count' (el tema con más comentarios)
nombre_tema_principal = tema_principal['Name']
conteo_tema_principal = tema_principal['Count']
print("\n" * 2)
print("Análisis basado en el tema más común encontrado por la IA:")
print("\n")

id_tema = tema_principal['Topic']
if id_tema == 0: 
    print("Se puede inferir que la opinión NEGATIVA es debido a que el tema central es la CONFRONTACIÓN SOCIOECONÓMICA.")
    print("Las palabras clave (mexicanos, gringos, negocios) sugieren un conflicto que no es solo cultural, sino que está directamente ligado a los negocios y al impacto económico.")

elif id_tema == 1: 
    print("La conclusión es NEUTRAL. El tema central (hacemos, wendy, five) parece ser una conversación fuera de tema (off-topic) y no relevante para el análisis.")

else:
    print("No se pudo decidir una conclusión específica para este tema.")

print("\n")
print("Fin del Projecto 2 - Topic Modeling.")
print("\n")



