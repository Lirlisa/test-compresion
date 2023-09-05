import unishox2
from dahuffman import HuffmanCodec
import zlib
from os import getenv
import numpy as np
from dotenv import load_dotenv

load_dotenv()


# texto para armar el arbol de huffman. Url: https://www.gutenberg.org/ebooks/29799.txt.utf-8
with open("texto_huffman.txt", encoding="utf-8") as file:
    codec_huffman = HuffmanCodec.from_data(file.read())

control = []
size_unishox2 = []
size_huffman = []
size_zlib = []
max_cant_palabras = int(getenv("MAX_CANT_PALABRAS"))
max_tests = int(getenv("TESTS_POR_CANT_PALABRAS"))
lineas_a_eliminar = int(getenv("LINEAS_A_ELIMINAR"))
contador_lineas = lineas_a_eliminar  # refleja en qué linea da error en caso de que algún caracter no se pueda manejar

# texto base para comprimir, modificado debido a caracteres no fuera del idioma español. Url: https://www.gutenberg.org/ebooks/29640.txt.utf-8
with open("texto.txt", "r", encoding="utf-8") as file:
    # eliminar primer lineas con contenido no deseado
    for i in range(lineas_a_eliminar):
        next(file)
    cant_palabras = 1
    contador = 0
    buffer = []

    for linea in file:
        contador_lineas += 1
        splitted = linea.split()
        if len(splitted) == 0:
            continue
        if len(splitted) + len(buffer) < cant_palabras:
            buffer.extend(splitted)
            continue
        else:
            remaining = cant_palabras - len(buffer)
            buffer.extend(splitted[:remaining])

            texto = " ".join(buffer)
            texto_bytes = texto.encode("utf-8")
            control.append(len(texto_bytes))
            try:
                size_huffman.append(len(codec_huffman.encode(texto)))
                size_unishox2.append(len(unishox2.compress(texto_bytes)[0]))
                size_zlib.append(len(zlib.compress(texto_bytes)))
            except Exception as e:
                print(e)
                print(f"{contador_lineas=}")
                print(f"{texto=}")
                print(f"{texto_bytes=}")
                print(len(texto_bytes))
                raise e

            buffer.clear()
            buffer.extend(splitted[remaining:])

            contador += 1
            if contador == max_tests:
                contador = 0
                cant_palabras += 1
                if cant_palabras > max_cant_palabras:
                    break

control = np.array(control)
size_unishox2 = np.array(size_unishox2)
size_huffman = np.array(size_huffman)

# huffman
dif_huffman = 1 - size_huffman / control
mean_huffman = np.mean(dif_huffman)
median_huffman = np.median(dif_huffman)
std_huffman = np.std(dif_huffman)
print("HUFFMAN")
print(f"{mean_huffman=}")
print(f"{median_huffman=}")
print(f"{std_huffman=}")
print("max size: ", np.max(size_huffman))
print("min size: ", np.min(size_huffman))
print("time to over 100 bytes: ", np.argmax(size_huffman > 100))
print()

# unishox2
dif_unishox2 = 1 - size_unishox2 / control
mean_unishox2 = np.mean(dif_unishox2)
median_unishox2 = np.median(dif_unishox2)
std_unishox2 = np.std(dif_unishox2)
print("UNISHOX2")
print(f"{mean_unishox2=}")
print(f"{median_unishox2=}")
print(f"{std_unishox2=}")
print("max size: ", np.max(size_unishox2))
print("min size: ", np.min(size_unishox2))
print("time to over 100 bytes: ", np.argmax(size_unishox2 > 100))
print()

# zlib
size_zlib = np.array(size_zlib)
dif_zlib = 1 - size_zlib / control
mean_zlib = np.mean(dif_zlib)
median_zlib = np.median(dif_zlib)
std_zlib = np.std(dif_zlib)
print("ZLIB")
print(f"{mean_zlib=}")
print(f"{median_zlib=}")
print(f"{std_zlib=}")
print("max size: ", np.max(size_zlib))
print("min size: ", np.min(size_zlib))
print("time to over 100 bytes: ", np.argmax(size_zlib > 100))

print("Cantidad de tests: ", len(size_unishox2))
