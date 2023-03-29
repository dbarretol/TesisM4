# m-Scripts

Para utilizar estos scripts primero se debe comprender que cuando se hace un análisis estocástico se tienen varias realizaciones (muestras) para una misma condición ambiental (por ejemplo viento). Entonces para usar estos scripts los archivos de salida de FAST (\*.outb) deben estar en una misma carpeta por cada condición ambiental especifica.

Esta carpeta contiene dos scripts de MATLAB:

1.  **procesar\_viento.m**: sirve para cargar archivos \*.outb y devuelve archivos excel con parámetros resumen de las velocidades de viento, como son el valor medio, la desviación estándar, valores pico máximos y mínimos.
2.  **get\_extremes.m**: sirve para cargar todos los archivos \*.outb contenidos en una carpeta y devuelve valores medios, desviación estándar y valores máximos de las respuestas dinámicas que el usuario establezca dentro del script.

Nota: estos scripts dependen de la función ReadFASTBinary, la cual puede obtenerse del siguiente [enlace.](https://github.com/OpenFAST/matlab-toolbox/blob/main/Utilities/ReadFASTbinary.m)
