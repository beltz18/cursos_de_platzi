# Trabajar con archivos

Dentro de la programación es común interactuar con archivos, como:

+ Archivos de Texto:
  - json
  - txt
  - py
  - xml
  - css
  - js
  - csv
+ Archivos binarios:
  - png
  - jpg
  - mp3
  - avi
  - dll
  - mp4

Los archivos de texto, como su nombre lo indica, son archivos que contienen texto plano. Mientras que los binarios, contienen información más compleja, como imagenes, videos... etc.

Los archivos de texto son de fácil manipulación y se require de herramientas sencillas capaces de cambiar el texto que hay dentro de estos. Mientras que para los archivos binarios se requiere de programas o herramientas especializadas que sean capaces de entender el formato de información que manejan.

## Modos de apertura

+ R (read)   -> Lectura
+ W (write)  -> Escritura (sobreescribir)
+ A (append) -> Escritura (agregar al final)

El comando de Python que abre un archivo es el siguiente:

```python
with open('./ruta/del/archivo.txt', 'r') as file:
```

**with** es conocido en Python como un manejador contextual que nos permite manejar el archivo que estamos abriendo para realizar determinadas acciones con este.