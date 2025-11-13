# Un Análisis de Métodos Mixtos (NLP + Geoespacial) en la CDMX

**Análisis de Social Data Science (NLP, Topic Modeling y GIS) sobre el discurso (Reddit) y el fenómeno físico (Airbnb) de la gentrificación.**

Éste portafolio es un proyecto de investigación interactivo
---


## Resumen del Proyecto


La gentrificación es uno de los fenómenos más debatidos en la Ciudad de México. Es ruidoso y se basa principalmente en **evidencia anectódica**, evidencia "tirada al aire". Ésta investigación es un intento de ir un paso más allá al aprovechar los recursos disponibles y **triangular** los datos para responder tres preguntas:

1. **¿Qué?:** Cuantificar el *sentimiento* usando NLP
2. **¿Por qué?:** Identificar la *causa* de ese sentimiento con Topic Modeling
3. **¿Dónde?:** Localizar éste *fenómeno* con Mapeo Geoespacial

## Proyecto 1: Análisis de Sentimiento ("¿Qué?")

* **Método:** Se usó la API de Reddit (Praw) y `Pysentimiento` (NLP) para analizar un pedacito de debate.
* **Hallazgos:** El sentimiento público fue indiscutiblemente **negativo** con un puntaje de polaridad promedio de **-0.57**.


## Proyecto 2: Modelado de Tópicos ("¿Por Qué?")


El Proyecto 1 estableció que el sentimiento es en su mayoría **NEGATIVO** (-0.57). En éste segundo análisis profundiza con un modelo `BERTopic` (basado en Transformers) y una *lista de **stopwords personalizada*** para eliminar el "ruido" (palabras cómo `jajaj`, `removed`, `xd`...) y encontrar la raíz de la causa. 

### Hallazgo Clave: Conflicto Socioeconómico


El modelo de IA identificó un tópico "ruido" (fuera de tema) y, el **Tópico 1**, la explicación del sentimiento negativo.

* Tópico **1**, Conteo [19], Inferencia de la Causa [**CONFRONTACIÓN CULTURAL**], Palabras Clave Dominantes [mexicanos, gringos, negocios, misma, mismo]
* Tópico **0**, Conteo [18], Inferencia de la Causa [Off-topic], Palabras Clave Dominantes [hacemos, wendy, conoce, creer, five]
* Tópico -1 , Conteo [7], Inferencia de la Causa [No Clasificado], Palabras Clave Dominantes [-]


**Conclusión:**
La polaridad negativa es impulsada por una **fricción socioeconómica** clara. El conflicto (`mexicanos`, `gringos`) está ligado directamente a los `negocios` y al impacto económico percibido.

![Barchart de Tópicos](Barchart.png)

## Proyecto 3: Mapeo Geoespacial ("¿Dónde?")

Pregunta que nos debemos de hacer ¿Es éste un conflicto sólo una "plática" (Reddit) o un "fenómeno físico"?

* **Método:** Se analizaron *26, 401* listados de **Inside AirBnb** (una fuente de datos académicos) usando `Geopandas` para el análisis espacial.
* **Visualización:** Se generó un mapa interactivo con `Folium` que incluye un **Mapa de Calor** para la *densidad*, y **Círculos de Precios** para los *costos*.

## Hallazgos Clave:

El mapa de calor prueba que el fenómeno **es físico**. Los "clusters" de más alta densidad y precio de Airbnb se superponen perfectamente con las zonas de las que la gente se queja (ej. Roma, Condesa), validando que el "discurso" de Reddit está anclado a una realidad tangible.

**Demo del Mapa Interactivo (Demo Interactivo):**
(Muestra el *heatmap* de densidad y los *pop-ups* de precios)

![Demo del Mapa Interactivo](mapa_demo.gif) 

## Conclusión: El Poder de los Métodos Mixtos (La unión hace la fuerza)

* **P1+P2 (Reddit):** Nos dicen que la gente *percibe* un conflicto socioeconómico (`gringos` + `negocios`).
* **P3 (Airbnb):** Nos *prueba* que este conflicto se concentra en "clusters" geográficos específicos y caros.

Juntos, estos 3 proyectos demuestran cómo la Ciencia de Datos Sociales puede transformar un debate anecdótico en **evidencia estructurada** (Qué, Por Qué y Dónde).


## Reflexión


Éste proyecto sirve como una prueba de concepto y, como investigadora de ciencias sociales reconozco que tiene **limitaciones**:



* **Sesgo de Muestra:** Los usuarios de Reddit no son representativos de *toda* la población de la CDMX.

  

* **Contexto Limitado:** Mi análisis es sólo una foto de un momento específico, no la película entera.

  

## Reproducibilidad

Este análisis es 100% reproducible. Cualquiera puede verificar los hallazgos de **los 3 proyectos** (Sentimiento, Tópicos y Mapeo) siguiendo estos pasos:


1. Este análisis es 100% reproducible.

1.  **Clona** el repositorio:
    ```bash
    git clone [https://github.com/cecirascon582-star/Reddit-Sentiment-Analysis-Gentrification.git](https://github.com/cecirascon582-star/Reddit-Sentiment-Analysis-Gentrification.git)
    ```
    
2.  Crea un archivo `.env` con tus credenciales de Reddit (`REDi`, `REDDit`).

   
3.  Descarga el `listings.csv` de [Inside Airbnb](http://insideairbnb.com/get-the-data/) y ponlo en la carpeta raíz.

  
4.  Instala **todas** las dependencias (`bertopic`, `geopandas`, `folium`, etc.):
    ```bash
    pip3 install -r requirements.txt
    ```

    
5.  Ejecuta los scripts **en orden**:
    ```bash
    python3 "Prueba3 adv.py"        # Proyecto 1: Sentimiento
    python3 "Parte 2/Topic.py"      # Proyecto 2: Tópicos
    python3 "Geo.py"                # Proyecto 3: Mapa
    ```
