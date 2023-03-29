# TESIS M4

En este repositorio se almacenan los códigos empleados para mi tesis de titulación relacionada a analisis de valor extremo de respuestas dinamicas estocastiscas de una turbina eolica onshore de 5MW sometida a viento turbulento.

Exiten cuatro carpetas:

1.  **RENALI:** los códigos en esta carpeta sirven para buscar términos en las bases de datos RENATI/ALICIA y obtener un  listado resumen con los metadatos de todos los items encontrados.
2.  **TSFAST:** e esta carpeta estan los codigos para generar archivos de entrada de TurbSim y FAST de manera automatica con solo definir las velocidades de viento y las semillas aleatorias. Tambien hay scripts para lanzar simulaciones en grupo de manera automatizada. Tambien contienen algunos archivos de entrada base correspondientes a la definicion de la turbina eolica NREL de 5 MW.
3.  **m-Scripts:** Las simulaciones en FAST arrojan un archivo de salida en formato binario (\*.outb), los cuales se leen en MATLAB. Esta carpeta tiene scripts para cargar los archivos de salida de las simulaciones, procesarlos, y obtener archivos excel que resumen parametros de interes a partir de las series de tiempo de las respuestas dinamicas como por ejemplo: valores maximos, valores promedio, desviaciones estandar, etc.
4.  **PostProc:** Contiene diferentes cuadernos para hacer gráficos y hacer el calculo de valores extremos de corto y largo plazo.
