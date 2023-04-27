Esta carpeta contiene notebooks donde se desarrollan operaciones relacionadas a gráficos y cálculos de análisis de valor extremo de una turbina eólica onshore en base a simulaciones en FAST NREL.

a) La carpeta 'Numcalc' contiene dos cuadernos:<br>
-CV_table : aquí se hace un análisis de las velocidades de viento generadas en el programa TurbSim, las cuales luego son utilizadas como entrada para el programa FAST.<br>
-Gumbel_fitting: aquí se hace el análisis de valor extremo de las simulaciones de respuestas dinámicas obtenidas de FAST. Se obtienen los coeficientes de ajuste de una distribución Gumbel en base a valores máximos globales de las diferentes realizaciones de las respuestas dinámicas.

b) La carpeta 'Plots' contienen 4 cuadernos donde se desarrolla código para realizar diversos tipos de gráficos (boxplot, scatter, etc.) tanto del viento como de las respuestas dinámicas.

c) La carpeta 'data' contiene los datos básicos para realizar todos los análisis requeridos en la tesis. Hay cuatro archivos excel donde se tienen series de tiempo, estadísticas descriptivas de las realizaciones del viento y conjuntos de valores extremos de respuestas dinámicas.
