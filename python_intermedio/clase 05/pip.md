# Cómo instalar módulos externos con PIP

PIP o Package Installer for Python, es un manejador de dependencias o bien, instalador de paquetes para Python. Por defecto ya está instalado dentro de Python.

Algunos módulos que no están dentro de Python pero que se suelen usar mucho para desarrollar son:

+ requests (para web scrapping)
+ pandas   (para data science)
+ numpy    (para data science)
+ pytest   (para testing)
+ flask    (para crear servidores)

Algunos comando básicos de pip son:

> ```pip freeze```                           (muestra todos los módulos instalados)
> ```pip install *nombre del modulo*```      (instala un nuevo módulo)
> ```pip freeze > **requirements.txt**```    (crea un archivo con las módulos instalados)
> ```pip install -r **requirements.text**``` (Instala las dependencias necesarias)