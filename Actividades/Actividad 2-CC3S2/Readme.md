# 1. Preguntas de reflexión  
- **Pregunta 1: ¿Qué significa "desplazar a la izquierda" en el contexto de DevSecOPs y por qué es importante?**  
Teniendo en cuenta que la izquierda es el inicio y la derecha el final (como comunmente de grafican las líenas de tiempo) desplazar a la izquierda hace alusión a poner al inicio algo. En el contexto de DevSecOps se refiere a ver los temas se seguridad desde el principio y no al inicio como tradicionalmente se hacia antes, la importancia de esto es que puedes tomar medidas de seguridad desde que el software está siendo creado reduciendo así el costo si es que se hace al final con todo el software ya creado, peor aun con la gran variedad de tecnologías que hay, puede ser ineficiente, muy diferente a tomar los temas de seguridad desde el principio y durante el proceso de desarrollo (menos costo y mas seguro).  
  
- **Pregunta 2: Explica cómo laC mejora la consistencia y escalabilidad en la gestión de infraestructura**  
Cuando hablamos de infraestructura como CÓDIGO, hacemos referencia a automatizar el proceso de configuración de la infraestructura, es decir el código de la automatización cada vez que se ejecute siempre construirá y configurará todo por ti y siempre de la misma manera reduciendo los errores a comparacion de hacerlo manualmente esto favorece la consistencia, en cuanto a la escalabilidad, al ser todo automático agiliza dicho proceso, por ejemplo podremos crear varios servidores con sus respectivas configuraciones con un solo comando,además esto evita que gastemos tiempo haciendo tareas repetitivas.  
  
- **Pregunta 3: ¿Cuál es la diferencia entre monitoreo y observabilidad? ¿Por qué es crucial la observabilidad en sistemas complejos?**  
Monitoreo se refiere a vigilar problemas conocidos buscando garantizar que el software esté funcionando correctamente, no obstante tiene limitancias y es que podremos saber hay un problema pero no por qué, aspecto que si cubre la observabilidad, pues aquí puedes saber donde y por qué surgió algun error, esmas profundo en la vigilancia. Es crucial en sistemas complejos porque al ser complejo probablemente los problemas sean mas delicados de solucionar, mas aún el tratar de entender el por qué de ese problema, es ahi donde juega un papel crucial la observabilidad.  
  
- **Pregunta 4: ¿Cómo puede la experiencia del desarrollador impactar el éxito de DevOps en una organización?**  
La experiencia de desarrollador es básicamente crear un entorno donde los dev. puedar hacer su trabajo mejor, y si desarrollan bien, el producto es bueno, ya que lo se busca es que el equipo sea productivo y esten satisfecho con el trabajo, si el entorno es positivo entonces no hay silos dentro de la organización y el dialogo fluye garantizanco el éxtio del DevOps y de la organización.  
  
- **Pregunta 5: Describe cómo InnerSource puede ayudar a reducir silos dentro de una organización**  
Los silos son básicamente todas las barreras en el equipo, con InnerSource esto se rompe ya que permite la colaboración entre diferentes equipos, y no asilarse entre los miembros de uno solo equipo, y si se aplica bien con todos los pilares del InnerSource se garantiza una mejor experiencia del desarrollador, y como se respondió en la pregunta anterior esto favorece al producto final y a la organización.  
  
- **Pregunta 6: ¿Qué rol juega la ingeniería de plataformas en mejorar la eficiencia y la experiencia del desarrollador?**  
Al haber un equipo de plataformas, ellos preparán el entorno de trabajo con todas los servicios y herramientas necesarias, esto evita que el mismo desarrollador tenga que estar configurando dicho entorno manualmente, mejorando asi su comodidad de trabajo, es como si le dieras todos los materiales a un alabañil para trabajar evitando que este gaste tiempo en ir a comprarlar, si ya le das todo lo que necesita ahorrarás tiempo y esto juega a favor para la eficiencia.  
  
  
# 2. Poniendo en Práctica lo aprendido  
## 2.1 Configuración del entorno
### 1. Inicializa el proyecto de Node.js  
Creamos nuestro archivo de trabajo e inicializamos un proyecto node  

![](img/2.1.png)  
  
### 2. Intalar dependencias necesarias  
  
![](img/2.2.png)  
  
### 3. Crea la estructura del proyecto
Usanso los comandos de `mkdir src tests` y `touch src/app.js tests/app.test.js`, la estrcutura del proyecto debría ser tal que asi:  

![](img/2.3.png)  
  
### 4. Implementa la API REST en src/app.js  
Creamos una api donde al hacer una solicitud GET con un nombre como parametro, nos devolverá un texto saludando.

![](img/2.4.png)  
  
### 5 Escribe un test básico en test/app.test.js  
El test simula una solicitud para un name Silva, en teoría deberia mostrarme en panalla "Hello Silva" y este test es báscimanete para comprobar eso.  

![](img/2.5.png)
  
### 6. Configura el  script de test en package.json  
Con esta configuración cada vez que pongamos `npm run dev` y `npm run test` se nos mostrará en el puerto asignado con su parámetro el saludo y correrá el test respectivamente

![](img/2.6.png)  
 
Si todo ha salido bien entonces al abrir el puerto desde nuestro navegador con algun parámetro por ejemplo `http://localhost:3000/Silva` debería salir algo como esto:
![](img/2.6.1.png)  
    
Y al ejecutar los test debería pasar satisfactoriamente:  

![](img/2.6.2.png)  
  
## 2.2 Implementación de DevSecOps  
  
### 1. Integración de Seguridad:  
Configura una herramienta de análisis de seguridad estática como npm audit para encontrar vulnerabilidades en las dependencias:  
Si sale como en la imágen de abajo significa que todas las dependencias están actualizadas o que no contienen problemas de seguridad que sean conocidos en la base de datos de vulnerabilidades de npm. :

![](img/2.2.1.png)  
  
### 2. Automatiza el análisis de seguridad en GitHub Actions  
Para ello se crea un archivo yml en nuestro workflow .github/workflows/ci.yml   
![](img/2.2.2.png)  
Lo que hace esto es definir unas acciones que se hará al momento de hacer push o pull request a la rama main, dichas acciones son configurar e instalar todas las dependencias necesarias para node, ejecutar los test y escanear las dependencias buscando si hay alguna vulnerabilidad, como vemos desde un inicio estamos viendo la seguridad, aspecto a tener en cuenta en DevSecOps pues hay un desplazamiento a la izquierda en la seguridad.