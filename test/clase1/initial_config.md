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
4-