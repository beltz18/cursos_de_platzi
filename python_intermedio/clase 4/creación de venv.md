# Creación de módulos virtuales

Para crear un nuevo entorno virtual dentro de un proyecto, debemos crear un directorio, posicionarnos dentro de éste y correr el siguiente comando en la terminal:

>> ```python3 -m venv *nombre del entorno*```
en Linux
>> ```py -m venv *nombre del entorno*```
en Windows

+ python3 es el comando que inicializa Python
+ La flag -m le indica a Python que se está llamando un módulo
+ venv es el módulo que nos permite crear entornos virtuales

Luego de crear el entorno virtual, debe activarse, para ello se usa el siguiente comando:

>> ```source venv/bin/activate```
en Linux
>> ```.\venv\Scripts\activate```
en Windows

Para desactivar el entorno virtual:

>> ```deactivate```
para cualquier OS