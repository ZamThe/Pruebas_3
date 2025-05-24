CONFIGURACIÓN PIPELINE DE CI/CD CON GITHUB ACTIONS
Una vez que el proyecto esté listo para integrarse con GitHub Actions, debemos crear un archivo de configuración llamado workflow. Este archivo se denominará ci-cd.yml.

CREACIÓN DE REPOSITORIO
Para este punto, utilizaremos las plataformas Git y GitHub, específicamente GitHub Desktop, que nos facilitará el control de versiones y nos permitirá subir los archivos del proyecto al repositorio de manera sencilla.
Paso a paso:
Paso1: Dentro de GitHub Desktop, debemos ir a la esquina superior izquierda y buscar la sección de Files o Archivos, luego seleccionar la opción New Repository para crear un nuevo repositorio.
Paso2: Debemos ingresar el nombre del repositorio, así como una breve descripción que lo explique, luego de ingresar los datos damos clic en crear repositorios.
Paso3: Una vez creado el repositorio debemos ir a la carpeta que se creo del mismo, en este caso se creó en la capeta documentos, para subir los archivos al repositorio debemos arrastrar los archivos del código fuente al repositorio.
Paso4: Una vez subidos los archivos a el repositorio, debemos seleccionar la rama a la cual deseamos subir los archivos, realizar un comid y por último enviar la orden de push para que los archivos sean subidos al repositorio.
Paso5: Para subir los cambios a los repositorios debemos dar clic en el push , se abrirá una nueva ventana donde podremos configurar las opciones del repositorio, como decidir si será público o privado, además de contar con el botón para publicar el repositorio.
Paso6: Una vez subido los cambios a el repositorio podremos acceder a el mismos desde la plataforma de GitHub


DESPLIEGUE EN RAILWAY 
Utilizando Railway, podremos realizar esta acción de forma sencilla, sin complicaciones ni configuraciones innecesarias.
Paso1: Ingresar a la pagina de rayway, es importante registrarnos previamente o vincular una cuenta de correo para poder utilizar las opciones gratuitas y básicas del despliegue.
Paso2: Una vez creada la cuenta, se abrirá un espacio de trabajo desde donde podremos comenzar a preparar y ejecutar el despliegue, debemos dar clic en ‘Add a service’ para poder vincular nuestro repositorio git.
Paso3: Se abrirá un menú que nos dará diversas opciones a escoger, en este caso se utilizará la opción de GitHub Repo
Paso4: Al enlazar mi cuenta de GitHub con la aplicación de Railway, tendrás acceso a todos los repositorios que hayas subido previamente, seleccionare el repositorio Pruebas_3, ya que este contiene las configuraciones necesarias para desplegar el aplicativo.
Paso5: Una vez seleccionado el repositorio del aplicativo, el despliegue se iniciará de forma automática.
Paso6: Debemos generar el dominio para acceder al aplicativo. Para ello, vamos a Configuraciones y seleccionamos la opción Generar dominio personalizado.
Paso 7: Una vez generado el dominio, podremos acceder al aplicativo y visualizar el contenido extraído.
