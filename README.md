# Object oriented project hands on

## Radar
El objetivo de esta sesion es realizar una simulación de un radar usando para ello un diseño orientado a objetos.

Inicialmente deben bajar todos los archivos .py en su home. El proyecto cuenta con varios archivos  **python**, que corresponden a las diversas clases utilizadas en la simulación. Las clases son: radar, generador de señal, receptor de señal, medio y blanco.

Un radar es un equipo genera y transmite señales hacia un medio donde pueden o no existir blancos. En caso de que la señal encuentre en su camino un blanco, éste puede reflejar la misma hacia el radar. La señal es recepcionada en el equipo para luego ser procesada por el detector. La clase detección determina si existe un blanco o no.
 
## Tareas

1. Completar la implementación de los métodos faltantes en las diferentes clases.

2. Completar el modulo main con la construcción de un radar e implementar algunos ejemplos 

3. Existe un tipo especial de blanco denominado Clutter. Estos son blancos estaticos que en el momento de ser iluminados por el radar reflejan grandes cantidades de energia lo que puede "cegar" al radar impidiendo la detección de otros blancos presentes. Un ejemplo de Clutter es una montaña. Se pide rediseñar la simulación de manera que se cree una subclase de blanco denominada blanco_clutter. Cuando el Clutter refleja una onda incidente, produce una señal de mayor amplitud que supera a la señal transmitida. 


4. Implementar el método del radar plotear_senal() para visualizar las senales antes y despues de impactar en un blanco


