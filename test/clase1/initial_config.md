En este archivo se seguira el ejemplo de la carpeta y entorno virtual test, 
reemplazar por el nombre que fuese la carpeta o entorno que se quiere utilizar

1- Instalar python y pip en la pc
2- Crear un nuevo entorno virtual llamado como la carpeta dentra de django-projects
    pythonX -m venv {nombre_carpeta}
    por ejemplo:
    python3.2 -m venv test
    Preferentemente utilizar siempre la misma version de python para los proyectos
    Esto no borra nada de los archivos necesarios (codigo fuente), pero si permite crear
    un entorno propio para trabajar en el sistema operativo y maquina que se desee
3- Activar el entorno virtual para usar django.
    windows 
        test/bin/activate
        Aca puede que haya algunos problemas para la ejecucion, por lo que se recomienda
        si no funciona este comando, ejecutar lo siguiente
            Set-ExecutionPolicy RemoteSigned -Scope CurrentUser
        Se puede hacer tambien 
            Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope LocalMachine
        pero no es muy recomendado por la seguridad. Una vez hecho eso volver a ejecutar
    UNIX
        source test/bin/activate

    Obs: para desactivar entorno virtual en se ejecuta deactivate desde cualquier lado
         Siempre que se vaya a trabajar en el proyecto se tiene que estar dentro del entorno virtual
4- ejecutar pip install django y pip install psycopg2 para usar django con postgresql
5- Si no se tiene instalado postgresql, instalar postgresql en el puerto especificado, con el
nombre de usuario, host y contraseñas respectivos, ya que hoy por hoy (02/2023) no se hace 
por variables de ambiente, ver para cambiar eso y crear un archivo .env para esas configuraciones
6- Correr los migrations pyhton manage.py migrate
7- Crear super usuario python manage.py createsuperuser
8- Luego ya se puede iniciar el proyecto haciendo python  manage.py runserver