# Taller Predio
## Julian David TIque Arias - Aprendiz Sena 
## Como Ejecutar El Proyecto:

* Descarga El Proyecto Desde El Repositorio De Github
  
    ![image](https://github.com/julian79110/taller_predio/assets/128442954/661e079b-6e53-4f29-b327-91f2c46fe813)

* Una vez Decargado Extraer El Proyecto, con la app que tenga o con el mismo explorador de windows:

    ![image](https://github.com/julian79110/taller_predio/assets/128442954/33f0d873-f447-432a-b58a-6379da99bcd4)

* Cuando haya extraido el archivo zip dejara la carpeta del proyecto, abre la carpeta:
  
  ![image](https://github.com/julian79110/taller_predio/assets/128442954/04dc75a1-0284-427a-af49-b7e56e74e696)
  
* una vez abierta abrir el cmd y dirigirse a la ruta de la carpeta:

    ![image](https://github.com/julian79110/taller_predio/assets/128442954/8201f5d7-4802-4827-8926-c0e029d329f8)
  
* Ahora procederemos a instalar las dependencias necesarias para ejecutar el proyecto con el comando: pip install -r requirements.txt

  ![image](https://github.com/julian79110/taller_predio/assets/128442954/83525d39-de30-4dba-ab7a-733b89424e87)

* Luego procedemos a crear la base de datos con el gestor de base de datos pgAdmin4 si no lo tiene instalado lo puede encontrar aqui: https://www.postgresql.org/download/

    ![image](https://github.com/julian79110/taller_predio/assets/128442954/56a02004-04e0-4dc6-b72d-474fec6327b3)

Seleccionamos postgres y abrimos una query tool dandole al primer boton en 'Object Explorer' o le podemos dar a alt + shift + q:

  ![image](https://github.com/julian79110/taller_predio/assets/128442954/48c7bd13-6fa5-4250-850b-a97cba991206)

* Esto abrira una query tool para poder digitar nuestro codigo sql para crear la base de datos 'predios'

Digitamos la Sentencia: create database predios

  ![image](https://github.com/julian79110/taller_predio/assets/128442954/cd9cad4f-cc51-4757-bfb2-5907a3fe9959)
  
* Una vez la base de datos este creada ejecutaremos el comando: python manage.py makemigrations.
  
  Esto permitira revisar si hay cambios en el modelo del proyecto

    ![image](https://github.com/julian79110/taller_predio/assets/128442954/30587833-bf75-4d53-8fb4-73e947e4bf7e)
  
* Despues ejecutaremos: python manage.py migrate

    Esto Permitira migrar las clases de django a la base de datos predios

    ![image](https://github.com/julian79110/taller_predio/assets/128442954/5e548de1-ff9b-4241-9192-c955bd8eef56)

* Una vez hecho esto podremos ejecurtar el proyecto con el comando: python manage.py runserver

    ![image](https://github.com/julian79110/taller_predio/assets/128442954/aa07ed3e-f50a-4596-a90b-383488e74d6d)

* Cuando ejecutemos ese comando abriremos el navegador y en la url escribiremos localhost:8000

    ![image](https://github.com/julian79110/taller_predio/assets/128442954/1aa8eed9-39c9-4be9-a98a-77be9ef3fc8d)

* Esto Abrira el index del proyecto:

    ![image](https://github.com/julian79110/taller_predio/assets/128442954/0ff494a4-0bc6-4810-91e8-be24bf7aa49d)

  ## Gracias por la atencion - Julian David Tique Arias






