# Reddit-Sentiment-Analysis-Gentrification

**NLP sentiment analysis of Reddit discussions (Mexico City) on gentrification using PRAW and Pysentimiento.**

---



## Resumen del Proyecto



La gentrificación es uno de los fenómenos socioeconómicos más debatidos en la Ciudad de México. El sentimiento público está altamente polarizado, pero, en general, se basa en evidencia hablada, "tirada al aire".



Este proyecto intenta ir un paso más allá al **cuantificar el sentimiento público sobre el tema**, utilizando comentarios de una discusión en Reddit como un *proxy* (sustituto medible) de la opinión pública, capturando discusiones en tiempo real y sin filtros para analizar la percepción dominante.



## Hallazgos Clave



El análisis de los comentarios extraídos de la discusión reveló:



* Un sentimiento general ** NEGATIVO **.

* Una puntuación de polaridad promedio de ** -0.57 **.



Esto sugiere que dentro de esta comunidad digital del link de Reddit existe un claro descontento generalizado hacia el fenómeno de la gentrificación.



## Metodología y Herramientas



Este proyecto demuestra un flujo de trabajo completo de ciencia de datos sociales, desde la extracción hasta el análisis.



### 1. Herramientas Utilizadas



* **Python 3.9**

* **PRAW (Python Reddit API Wrapper):** Para autenticarse de forma segura y extraer datos en vivo de la API de Reddit.

* **Pandas:** Para limpiar, estructurar y transformar los comentarios en un DataFrame analizable.

* **Pysentimiento:** Un modelo de Procesamiento de Lenguaje Natural (NLP) pre-entrenado y optimizado para el español, usado para realizar el análisis de sentimiento.

* **Deep-Translator:** Para la traducción de frases (Su función era un objetivo secundario).

* **Dotenv / Gitignore:** Para una gestión segura de las credenciales de la API, siguiendo las mejores prácticas de seguridad.



### 2. Proceso



1.  **Extracción de Datos:** Conexión a la API de Reddit para extraer todos los comentarios (incluyendo respuestas anidadas) del hilo objetivo.

2.  **Análisis de Sentimiento:** Aplicación del modelo "pysentimiento" a cada comentario en español para asignar una puntuación de polaridad ("POS=1", "NEU=0", "NEG=-1").

3.  **Agregación:** Cálculo del promedio de todas las puntuaciones de polaridad para obtener el sentimiento general del hilo.



## Reflexión



Este proyecto sirve como una prueba de concepto y, como investigadora de ciencias sociales, reconozco que tiene **limitaciones**:



* **Sesgo de Muestra:** Los usuarios de Reddit no son representativos de *toda* la población de la CDMX.

  

* **Contexto Limitado:** Mi análisis es sólo una foto de un momento específico, no la película entera.



**Próximos Pasos:**



* **Análisis a Escala:** Expandir la extracción de datos sobre gentrificación en la Ciudad de México del último año, para un análisis longitudinal.

  

* **Modelado de Tópicos (Topic Modeling):** Usar LDA (Latent Dirichlet Allocation) o BERTopic para identificar *por qué* el sentimiento es negativo (ej. "aumento en las rentas", "odio entre culturas", "miedo a lo nuevo").
