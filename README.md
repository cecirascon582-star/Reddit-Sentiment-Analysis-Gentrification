# Reddit-Sentiment-Analysis-Gentrification

**NLP sentiment analysis of Reddit discussions (Mexico City) on gentrification using PRAW and Pysentimiento.**

---



## Resumen del Proyecto



La gentrificación es uno de los fenómenos socioeconómicos más debatidos en la Ciudad de México. El sentimiento público está altamente polarizado, pero, en general, se basa en evidencia hablada, "tirada al aire".



Este proyecto intenta ir un paso más allá al **cuantificar el sentimiento público sobre el tema**, utilizando comentarios de una discusión en Reddit como un *proxy* (sustituto medible) de la opinión pública, capturando discusiones en tiempo real y sin filtros para analizar la percepción dominante.



## Hallazgos Clave



El análisis de los comentarios extraídos de la discusión reveló:



* Un sentimiento general **NEGATIVO**.

* Una puntuación de polaridad promedio de **-0.57**.



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


## Proyecto 2: Modelado de Tópicos (El "¿Por Qué?")

El Proyecto 1 estableció que el sentimiento es en su mayoría **NEGATIVO** (-0.57). Éste segundo análisis profundiza para identificar las **causas subyacentes** de ese descontento.

### Metodología Avanzada

Después de múltiples intentos para eliminar el "ruido" (stop words gramaticales y contextuales como 'jaja' o 'removed'), se aplicó un modelo final con una **lista de stop-words personalizada**.

Este "hack" forzó al modelo de IA (BERTopic) a ignorar el ruido y enseñarnos la verdadera causa del descontento.

### Hallazgo Clave: Conflicto Socioeconómico

El modelo de IA identificó un tópico irrelevante (fuera de tema) y, el **Tópico 0**, el central, que explica el sentimiento negativo.

* Tópico **0**, Conteo [19], Inferencia de la Causa [**CONFRONTACIÓN CULTURAL**], Palabras Clave Dominantes [mexicanos, gringos, negocios, misma, mismo]
* Tópico **1**, Conteo [18], Inferencia de la Causa [Off-topic], Palabras Clave Dominantes [hacemos, wendy, conoce, creer, five]
* Tópico -1 , Conteo [7], Inferencia de la Causa [No Clasificado], Palabras Clave Dominantes [-]


**Conclusión:**
La polaridad negativa es impulsada por una **fricción socioeconómica** clara. Las palabras clave dominantes (`mexicanos`, `gringos`, `negocios`) sugieren que el conflicto no es solo cultural, sino que está **directamente ligado a los negocios** y al impacto económico que su llegada del extranjero a la Ciudad de México a tenido.

Ésto valida la necesidad de usar métodos de Social Data Science para transformar discusiones emocionales en evidencia estructurada.

## Reflexión


Éste proyecto sirve como una prueba de concepto y, como investigadora de ciencias sociales reconozco que tiene **limitaciones**:



* **Sesgo de Muestra:** Los usuarios de Reddit no son representativos de *toda* la población de la CDMX.

  

* **Contexto Limitado:** Mi análisis es sólo una foto de un momento específico, no la película entera.



## Próximos Pasos

* **Análisis a Escala:** Expandir la extracción de datos a múltiples fuentes sobre la gentrificación en la CDMX del último año, para un análisis longitudinal.
  
* **Análisis Geoespacial:** Hacer *web scraping* de precios de Airbnb/rentas para crear un mapa de calor (`GeoPandas`) y visualizar *dónde* se concentra el fenómeno en la CDMX.

  

## Reproducibilidad

Este análisis es 100% reproducible. Cualquiera puede verificar los hallazgos de **los dos proyectos** (Sentimiento y Tópicos) siguiendo estos pasos:


1.  **Clona** este repositorio en tu máquina local:
    ```bash
    git clone [https://github.com/cecirascon582-star/Reddit-Sentiment-Analysis-Gentrification.git](https://github.com/cecirascon582-star/Reddit-Sentiment-Analysis-Gentrification.git)
    ```


2.  Crea un archivo `.env` en la raíz del proyecto con tus credenciales de la API de Reddit. (El script busca `REDi` y `REDDit`).
    ```text
    REDi=TU_CLIENT_ID_DE_REDDIT
    REDDit=TU_CLIENT_SECRET_DE_REDDIT
    ```


3.  Instala **todas** las dependencias (`praw`, `bertopic`, `nltk`, etc.) automáticamente usando el archivo `requirements.txt`:
    ```bash
    pip3 install -r requirements.txt
    ```


4.  Ejecuta los scripts **en orden**:
    * **Proyecto 1 (Análisis de Sentimiento):**
        ```bash
        python3 "Prueba3 adv.py"
        ```
    * **Proyecto 2 (Modelado de Tópicos):**
        ```bash
        python3 "Parte 2/Topic.py" 
        ```

