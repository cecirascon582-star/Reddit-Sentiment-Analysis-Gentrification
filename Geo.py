import pandas as pd
import geopandas
from shapely.geometry import Point #para traducir coordenadas a puntos geográficos
import folium
from folium.plugins import HeatMap

print("Iniciando el Proyecto 3 - Análisis Geoespacial....")

try:
    df= pd.read_csv("listings.csv")
    print(f"Se cargaron {len(df)} registros del archivo listings.csv")
except FileNotFoundError:
    print("Error: No se encontró el archivo listings.csv. Asegúrate de que el archivo esté en el directorio correcto.")
    exit()

#Limpiar datos, sólo necesito columnas de latitud, longitud y precio
print("Limpiando datos...")
df_limpio=df[["latitude", "longitude", "price"]].copy()
df_limpio.dropna(inplace=True) #Elimino las filas que no me sirven

#El precio viene como string(texto), lo convierto a número (float)
df_limpio["price"]=df_limpio["price"].replace(r"[\$,]","", regex=True).astype(float)
#df_limpio["price"] seleccionas la columna "price"
#regex=True le dice a pandas que interprete el patrón como una expresión regular
#El patrón [\$,] busca el símbolo de dólar y las comas en los números
#.astype(float) toma los valores limpios y los convierte a float (número con decimales)

#Convertir la latitud y longitud a puntos geográficos
print("Convirtiendo coordenadas a puntos geográficos...")
geometry=[Point(xy) for xy in zip (df_limpio["longitude"], df_limpio["latitude"])]
#df_limpio["longitude"], df_limpio["latitude"] juntas las dos columnas en pares de coordenadas (longitud, latitud)
#Point(xy) convierte cada par de coordenadas en un punto geográfico
#for xy in zip (...) itera sobre cada par de coordenadas y crea una lista de puntos

#Toma mi tabla limpia y la mezcla con la nueva lista de coordenadas para crear una súper tabla gdf
gdf= geopandas.GeoDataFrame(df_limpio, geometry=geometry)
#geopandas.GeoDataFrame(...): crea una nueva tabla geográfica
#df_limpio para que la nueva tabla tenga los datos de éste
#geometry= es el nombre de la columna "especial" que va a tener los puntos del mapa
#=geometry es la variable de arriba

print("Los datos se han limpiado y fueron convertidos a Geo Data Frame")

#Centrar mapa en la CDMX
mapa_cdmx=folium.Map(location=[19.4326, -99.1332], zoom_start=11) #folium.Map crea un nuevo mapa de folio
#location=[19.4326, -99.1332] le dice al mapa donde centrarse; esas son las coordenadas del zócalo
#zoom_start=11 pone el zoom inicial

#Heatmap (enseña la densidad de los AirBnb)
#El heatmap de folium requiere que los datos de las coordenadas estén en el formato [latitud, longitud], y no en el estánda de (x,y)
heat_data=[[point.y, point.x] for point in gdf.geometry]
#for point in gdf.geometry recorre cada uno de los puntos en el gdf en la columna de geometry
#cada "point" guarda coordenadas y=latitud, x=longitud
#eat_data = [...] el resultado es una lista grande (eat_data) con una bola de coordenadas en el formato []

HeatMap(heat_data, radius=7).add_to(mapa_cdmx)
#folium.plugins.HeatMap(...) crea el heatmap
#heat_data lista de coordenadas del paso de arriba
#radius=12 controla el tamaño en pixeles de la mancha de calor de cada punto individual (si lo haces más grande se mezclan los puntos y se pierden)
#.add_to(mapa_cdmx) agarra el mapa de calor y lo pone encima del mapa_cdmx de arriba

#Mapa con puntos de precios
for _, row in gdf.iterrows(): #for...in... hace un loop que recorre la geotabla fila por fila
    #gdf.iterrows() recorre las filas, y en cada loop te da dos cosas: el # de índice de la fila y todos los datos de la fila completa ("price", "latitud".. y todo en un objeto)
    #_, row guarda esas dos cosas
    #row Es una variable que en cada vuelta guarda todos los datos de la fila actual. Puedes acceder a ellos con row['price'] o row['geometry'].
    # _ (guion bajo) Se usa como nombre de variable cuando no te importa ese valor. En este caso, no me importa el número de índice (0, 1, 2...) solo importan los datos de la fila.
    texto_popup = f"Precio: ${row['price']}" #Texto de pop up por separado
    popup_obj = folium.Popup(texto_popup) #objeto de pop up de folium
    folium.CircleMarker( #hace un círculo en el mapa con tamaño ya determinado
        location=[row["latitude"], row["longitude"]], #pone el círculo en las coordenadas dela fila que está siendo procesada
        radius=2, #define el tamaño del círculo, en su caso es chico
        color="red" if row["price"] > 5000 else 'blue', # Puntos rojos si el precio en esta fila es mayor a 5000.
        popup=popup_obj, # Uso el objeto pop up 
        tooltip=texto_popup # Agregamos un tooltip (para ver al pasar el mouse)
    ).add_to(mapa_cdmx)

#Guardar mapa en html
mapa_cdmx.save("mi_heatmap.html")

print("\n")
print("Fin del Proyecto 3 - Heatmap")
print("\n")