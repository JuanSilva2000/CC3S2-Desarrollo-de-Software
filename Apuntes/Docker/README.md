## ¿Qué es Docker?
Es un proyecto de código abierto que automatiza el despliegue de aplicaciones dentro de contenedores de software. Hay que entender un contenedor como un recipiente donde se guardará la app con sus librerías y dependencias para que esta funcione.  
  
## ¿Qué es un contenedor?  
Es un unidad de software ligera y portátil que encapsula una app junto con todas sus dependencias y bibliotecas. (La instancia de una imágen).  
Los contenedores nacen de las imágenesy estas son plantillas solo de lectura, las imágenes se alojan en docker Hub.  
  
## ¿Qué es una imágen?  
Una imágen es una plantilla de solo lectura que contiene todos los elementos necesarios para crear un contenedor. Antes de crear un contenedor, se necesita una imágen , esto se puede hacer con un comando o con un archivo llamado Dockerfile. 
  
**Notas**  
- Cuando ejecutamos un contenedor y no está la imágen, docker los descarga automáticamente.  
- Para eliminar una imágen, primero se debe eliminar los contenedores de esa imágen.  
  
## Algunos comandos de docker:  
- Lista todas las imágenes instaladas
    ```powershell  
        docker image
    ```  
      
- Esto es para ejecutar un contenedor apartir de una imágen `hello-world`, pero luego se pausa 
    ```powershell  
        docker run hello-world
    ```  
      
- Muestra los contenedores activos 
    ```powershell  
        docker ps
    ```  
      
- Muestra todos los contenedores incluyendo los pausados 
    ```powershell  
        docker ps -a
    ```  
      
- Lista todas las imágenes de nginx encontradas en dockerhub 
    ```powershell  
        docker search nginx
    ```  
      
- Descarga la imágen nginx 
    ```powershell  
        docker pull nginx
    ```  
      
- Elimina un contenedor por su id 
    ```powershell  
        docker rm <<container_id>>
    ```  
      
- Eliminar una imágen por su nombre (también se puede por id) 
    ```powershell  
        docker rmi hello-world
    ```  
      
- Ejecutamos un contenedor pero con un nombre asociado, en este caso de nombre "contenedor1" (debe ser único) 
    ```powershell  
        docker run --name contenedor1 hello-world
    ```  
      
- Muestra información detallada de un contenedor 
    ```powershell  
        docker inspect contenedor1
    ```  
- Elimina todos los contenedores 
    ```powershell  
        docker container prune
    ```  
      
- Reanudar un contenedor que a sido pausado o detenido 
    ```powershell  
        docker start <id o name>
    ```  
     
- Inicia un contenedor en modo interactivo y asigna una terminal para ingresar al contenedor y trabajr con el
    ```powershell  
        docker run -it ubuntu
    ```  

- Incia un contenedor de ubuntu, el -d es para que se ejecute en segundo plano (regresa inmediatamente a la terminal) y el `tail -f /dev/null` es para que no se pause y mantenga en ejecución 
    ```powershell  
        docker run --name alwaysup -d ubuntu tail -f /dev/null
    ```  
      
- El `--rm` elimina automática el contenedor cuando se detiene, el `-p 8080:80` mapea el puerto host 8080 al puerto 80 del contenedor esto es, podré acceder al server de nginx en mi navegador en 8080 
    ```powershell  
        docker run -it --rm -d -p 8080:80 --name web nginx:latest
    ```  

- Pausa un contenedor activo
    ```powershell  
        docker stop "name/id"
    ```  
      
- Elimina un contenedor y el -f es para eliminarlo sin importar que esté activo
    ```powershell  
        docker rm -f <<container>>
    ```    
      
## ¿Qué es un Dockerfile?  
Un dockerfile es un archivo de texto plano que contiene un conjunto de instrucciones que docker utiliza para construir una imágen Docker.  
  
Ejemplo de un dockerfile:  (6 capas)  
  
```dockerfile  
    FROM ubuntu:latest  (1)
    RUN apt-get update && apt-get install -y curl wget vim git (2)  
    WORKDIR /app (3)  
    RUN echo "Hola Docker!" > saludo.txt  (4)  
    EXPOSE 80 (5)  
    CMD ["echo", "Este es un contenedor de ejemplo"] (6)
```  
  
(1) Indicamos qué imágen vamos a utilizar, en este caso es como si empezaramos con una computadora nueva que tiene ubuntu instalado.  
  
(2) Ejecuta comandos en la nueva computadora ubuntu.
  
(3) Crea un nuevo directorio app (si no existe) y cambia ese directorio para que los próximos comandos se ejecuten ahí.  
  
(4) Crea un archivo llamado saludo.txt en el directorio acutal (/app) y escribe "Hola docker!" en ella.  
  
(5) Indica que el contendor debería usar el puerto 80 para recibir conexiones  
  
(6) Define el comando que se ejecutará cuando el contenedor se inicie. En este caso ejecutará echo "Este es un contenedor de ejemplo" que imprime ese mensaje en la pantalla (puede ser sobreescrito, /bin/bash)  (*)
  
Para crear una imágen con ese dockerfile usamos el siguiente comando  
  Nota: `ubuntu-new` es el nombre de imágen y el punto le indicamos la ruta en donde esta el dockerfile  

```powerswell  
    docker build -t ubuntu-new .
```  
  
Para correr esa imágen:  
```powershell
    docker run -it -p 7070:70 ubuntu-new /bin/bash  
```  
*Nota: aqui le estamos diciendo a docker que cuando el contenedor está en funcionamiento, quieres que te dé a una terminal dentro del contenedor, si no está esto  se muestra el (\*) de la seción anterior (o sea incia una sesión de bash en terminal linux)* 
  
Para ejecutar un comando:  
```powershell  
    docker exec -it my-container ls /usr/shave/nginx/html
```  
  
*Nota: Lo que está después de my-container es el comando que se ejcuta dentro del contendor, ls es para listar los archivos*
  
    
## Redes en Docker  
Las redes son una funcionalidad fundamental que permite la comunicación entre contenedores, así como también la comunicación entre contenedores y el mundo exterior.  
  
- Lista todos las redes 
    ```powershell  
        docker network ls
    ```  
*La red bridges es la predeterminada que se usa cuando no se especifica la red a la que pertenece un contenedor*      

- Para crear una red 
    ```powershell  
        docker network create "name"
    ```  
      
- Para ver toda la info de la red "my-network"
    ```powershell  
        docker network inspect my-network
    ```  
      
- Lo que está después del name es el nombre del container y lo que esta después de network es la red a que pertenece (nginx:latest es la imágen)  
    ```powershell  
        docker run -d --name my-container --network my-network nginx:latest
    ```  
      
- Desconectamos de la red my-network el contenedor `my-container` 
    ```powershell  
        docker network disconnect my-network my-container
    ```  
      
- Elimina una red
    ```powershell  
        docker network rm my-network
    ```









    
