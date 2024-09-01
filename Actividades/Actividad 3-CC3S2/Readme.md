# Actividad: Introducción a Git - conceptos básicos y operaciones esenciales  
  
## 1. git config: Preséntate a Git  
Para asignar el username y el correo asociando debemos usar los siguientes comandos:  
  
```
$ git config --global user.name "Juan Silva"
$ git config --global user.email "juan.silva.r@uni.pe"
```  
  
Para verificar que tu presentación se ha registrado, puedes comprobarlo con el comando `git config --list`  
  
![](img/1.1.png)  
  
## 2. git init: Donde comienza tu viaje a código
Creamos un directorio de trabajo, en nuestro caso lo llamamos  `Actividad 3-CC3S2` .Usando el comando `git init` inicializamos un nuevo repositorio de Git y comenzar a rastrear directorios existentes, además se crea un directorio .git que tiene todo lo necesario para el control de versiones
  
![](img/2.1.png)  
  
## 3. git add: Prepara tu código
Con el comando `git add` podemos pasar los archivos a un estado de tracked (rastreado), primero debemos crear algun archvio dentro de nuestro directorio, en mi caso ya lo hice al momento de escribir y este readme, por lo tanto al poner git status para ver el estado del archivo:  
![](img/3.1.png)  
Si queremos pasarlo a uns estado de rastreado podemos usar una opción de git add el cual es `git add .` esto rastrea todos los archivos:  
  
![](img/3.2.png)  
  
## 4. git commit: Registra cambios  
Con el git commit registramos los cambios que previamente se preparamos con el git add, el commit viene con una bandera -m es para añadir un mensaje corto y descriptivo que especifique los cambios hechos