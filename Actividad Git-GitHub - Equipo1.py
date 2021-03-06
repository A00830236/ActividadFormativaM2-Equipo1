# -*- coding: utf-8 -*-
"""M2-1-Equipo1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/11p5TNyiILGZSGZ9zTKtAieInZYuhaQ6t

##Actividad M2.1 Uso de Google Colab##

Daniela García A00830236

David Esquer Ramos A01114940

Arath Gonzalez A01655058

Daniel Saldaña A00829752

Tecnológico de Monterrey

"""

import pandas as pd

"""##Lectura de datos"""

from google.colab import drive
drive.mount('/content/drive')

data = pd.read_csv('/content/drive/MyDrive/AnalisisCienciasDeDatos/M2A2.1-Nube-GColab-Github/titanic.csv')
data

"""##Descripción de variables

1. Identifica el tipo de variables presentes en el dataset, y en una celda describe cuáles variables son categóricas y cuáles numéricas. Muestra esta información en forma de lista
"""

data.dtypes

"""2. Utiliza en diferentes celdas de código las funciones columns(), info() y describe() del dataframe. Muestra la información generada."""

data.columns

data.info()

data.describe()

"""3. Explica que hace cada una de estas funciones. 

*   data.columns
  * Esta función te dice el nombre de las columnas del dataframe.
*   data.info()
  * Esta función te dice de cada columna cuantos datos existentes tiene y que tipo de datos son.
*   data.describe()
  * Esta función te muestra las estadisticas descriptivas de cada columna en donde su valores son numéricos.

4. Indica cuántos registros se tienen en total, cuáles tienen valores nulos y cuáles no tienen valores nulos.
"""

#registros total:
data.info()

#valores nulos:
data_nulo = data.isnull().sum()
data_nulo

"""Se tienen 891 registros en total.

Las columnas que tienen valores nulos son:
* Age (177 valores nulos)
* Cabin (687 valores nulos)
* Embarked (2 valores nulos)

Las columnas que NO tienen valores nulos son:
* PassengerId
* Survived
* Pclass
* Name
* Sex
* SibSp
* Parch
* Ticket
* Fare

5. ¿Qué columnas aparecen en el resultado de describe? ¿Cuál es la tarifa más cara? ¿Cuál es el promedio de edad?
"""

data.describe()

"""¿Qué columnas aparecen en el resultado de describe? 
*   Las columnas que aparecen en el resultado siguen siendo las mismas columnas de las varibles, sin embargo ahora las filas son las que cambiaron a ser la estadisticas descriptivas de cada variables

¿Cuál es la tarifa más cara? 
* 512.329200 dlls

¿Cuál es el promedio de edad?
* 29.699118 años

6. Escribe el código necesario para indicar de las variables categóricas  cuantos valores diferentes se tiene por categoría. Puedes usar el método unique() para regresar los valores únicos de una columna.
"""

data.Sex.nunique()

data.Sex.unique()

data.Ticket.nunique()

data.Ticket.unique()

data.Cabin.nunique()

data.Cabin.unique()

data.Embarked.nunique()

data.Embarked.unique()

"""##Analisis de datos

Agrega el código para indicar cuánto es el total que se pagó sumando la tarifa de todos los pasajeros.
"""

total = data["Fare"].sum()
total

"""Crea un subconjunto de los datos de los que sobrevivieron y otro de los que no sobrevivieron usando df[condición]"""

#sobrevivieron
survivors = data[data["Survived"]==1]
survivors.head()

#murieron
perish = data[data["Survived"]==0]
perish.head()

"""Mostrar los datos de 5 personas de las que sobrevivieron y de las que no sobrevivieron."""

#5 sobreviviente
survivors_5sample = survivors.sample(5)
survivors_5sample

#5 fallecidos
perish_5sample = perish.sample(5)
perish_5sample

"""10. Guarda el cuaderno generado en drive y en tu computadora. Exportar también el archivo a PDF."""
