## ⚙️ Configuración Pipeline de CI/CD con GitHub Actions

Una vez que el proyecto esté listo para integrarse con **GitHub Actions**, debemos crear un archivo de configuración llamado workflow. Este archivo se denominará: `.github/workflows/ci-cd.yml`.

---

## 📁 Creación de Repositorio

Para este proceso, utilizaremos las plataformas **Git** y **GitHub**, específicamente **GitHub Desktop**, que nos facilita el control de versiones y permite subir archivos al repositorio fácilmente.

### 🪜 Paso a paso:

#### 📌 Paso 1:
Dentro de **GitHub Desktop**, ve a la esquina superior izquierda, busca la sección de `Files` o `Archivos`, y selecciona **"New Repository"** para crear un nuevo repositorio.

#### 📌 Paso 2:
Ingresa el nombre del repositorio y una breve descripción. Luego, haz clic en **"Create Repository"**.

#### 📌 Paso 3:
Una vez creado el repositorio, accede a la carpeta generada (por defecto en "Documentos"). Para subir los archivos del proyecto, arrastra el código fuente dentro de esta carpeta del repositorio.

#### 📌 Paso 4:
Con los archivos cargados, selecciona la **rama (branch)** a la que deseas subir los cambios. Luego, realiza un **commit** y ejecuta el **push** para subir los archivos al repositorio remoto.

#### 📌 Paso 5:
Al hacer push, se abrirá una ventana donde podrás configurar opciones del repositorio, como su visibilidad (público o privado). Finalmente, haz clic en **"Publish Repository"**.

#### 📌 Paso 6:
Una vez subidos los cambios, podrás acceder al repositorio directamente desde la plataforma web de **GitHub**.

---

💡 **Recuerda:** Una vez tengas el archivo `ci-cd.yml` en la ruta `.github/workflows/`, GitHub Actions comenzará a ejecutar automáticamente los workflows definidos según los eventos configurados (como push o pull request).


## 🚀 Despliegue en Railway

Utilizando **[Railway](https://railway.app/)**, podremos realizar el despliegue de forma sencilla, sin complicaciones ni configuraciones innecesarias.

---

### 🪜 Paso a paso:

#### 📌 Paso 1:
Ingresa a la página de [Railway](https://railway.app/). Es importante **registrarte** previamente o **vincular una cuenta de correo** para acceder a las opciones gratuitas y básicas del despliegue.

#### 📌 Paso 2:
Una vez creada la cuenta, se abrirá un **espacio de trabajo** desde donde podrás comenzar a preparar y ejecutar el despliegue. Haz clic en **"Add a service"** para vincular tu repositorio de GitHub.

#### 📌 Paso 3:
Se abrirá un menú con diversas opciones. Selecciona **"GitHub Repo"** para continuar.

#### 📌 Paso 4:
Al enlazar tu cuenta de GitHub con Railway, tendrás acceso a todos tus repositorios. Selecciona el repositorio **`Pruebas_3`**, que contiene las configuraciones necesarias para desplegar el aplicativo.

#### 📌 Paso 5:
Una vez seleccionado el repositorio, **el despliegue se iniciará automáticamente**.

#### 📌 Paso 6:
Para acceder al aplicativo desplegado, es necesario **generar un dominio**. Dirígete a **"Settings"** y selecciona la opción **"Generate Custom Domain"**.

#### 📌 Paso 7:
Una vez generado el dominio, podrás acceder al aplicativo y **visualizar el contenido en línea** desde cualquier navegador.

---

✅ ¡Y listo! Tu aplicación está en la nube con Railway.

