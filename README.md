# Test Compresion
Programa que compara el desempeño de los algoritmos unishox2, huffman coding y zlib.

Para probar localmente es necesario tener instalado python 3.10 y la librería pipenv.
Para instalar las librerías y correr el programa se debe:
<li>Posicionarse en el directorio del proyecto</li>
<li>Ejecutar el comando "pipenv shell"</li>
<li>Instalar las librerías con "pipenv install"</li>
<li>Ejecutar compresion.py</li>
<br><br>

En el archivo .env hay variables que se pueden editar a gusto:
<li>TESTS_POR_CANT_PALABRAS: es la cantidad de pruebas para realizar por cada cantidad de palabras, por ejemplo si la cantidad actual de palabras es 4, y TESTS_POR_CANT_PALABRAS es 10, entonces se realizarán 10 pruebas de 4 palabras.</li>
<li>MAX_CANT_PALABRAS: es la cantidad máxima de palabras a probar.</li>
<li>LINEAS_A_ELIMINAR: es la cantidad de lineas a purgar del texto de prueba, puesto que el texto elegido tiene tiene una introducción insertada por el sitio de donde se sacaron los textos.</li>
