# js-neural-networks

## Presentación

<b>¿Qué es una red neuronal?</b>
Es un modelo computacional basado en un gran conjunto de unidades neuronales simples de forma aproximadamente análoga al comportamiento observado en los axones de las neuronas en los cerebros biológicos.
Como se observa en la imágen la misma para entrenar el modelo el mismo recibe inputs, realiza un procesamiento y genera outputs, que luego se utilizarán para cambiar el estado interno de la misma. Una vez entrenada, el output ya se utiliza directamente como el resultado de lo que queremos predecir. 
![alt text](https://cdn-images-1.medium.com/max/800/1*fNAjKoWt21pdzlkTmlP3pw.png)

<b>Algunos usos en la vida real</b>
<br>
Detección de fraude con los movimientos de tarjeta de crédito usado por empresas como Eurocard Nederland, Mellon Bank, First USA Bank.
<br>
![alt text](https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSy_nL0-bVlWXjZfGyyByLio7Xv6pioDKbqHWKywnYF2S6P9bwu)
<br>
Detección de células cancerígenas utilizado por The US Food and Drug Administration.
![alt text](http://news.mit.edu/sites/mit.edu.newsoffice/files/images/2016/MIT-Cancer-Cell-Growth_0.jpg)
<br>
Caso interesante a nivel industrial
<br>
La empresa Fanuc, originaria de Japón, que produce y comercializa robots para diferentes aplicaciones industriales plantearon utilizar una red neuronal en vez de programar directamente lo que el robot tiene que hacer. Una gran ventaja de esto es que la información que los mismos aprenden puede estar centralizada en un sólo lugar y ser compartida por todos, por lo que lo que un robot aprende en 8 horas, 8 pueden aprenderlo en 1 hora. Ejemplo de uno de los robots en el cual aplicaron una red neuronal.
<br>
<br>
El robot tiene como aplicación recoger cilindros de un recipiente y moverlos a otro. Al principio comienza haciendolo al azár, tomando una foto antes de cada levantamiento, y clasificandola en éxito o fracaso. Al mismo tiempo la envía a una red neuronal para que sea entrenada.
![alt text](https://github.com/juanborssotto/js-neural-networks/blob/master/readme-imgs/fanuc-1.png)
<br>
Luego de 1000 intentos aprende que ciertas posiciones de los cilindros siempre llevan al fracaso, y luego de 5000 intentos cuáles son las posiciones que llevan al éxito.
![alt text](https://github.com/juanborssotto/js-neural-networks/blob/master/readme-imgs/fanuc-2.png)
<br>
Finalmente, como resultado, luego de 1000 intentos tiene un porcentaje de éxito del 60% y luego de 5000 intentos un porcentaje de éxito de 90%.
![alt text](https://github.com/juanborssotto/js-neural-networks/blob/master/readme-imgs/fanuc-3.png)
<br>
Link al video: https://www.youtube.com/watch?v=ydh_AdWZflA

<b>Entrenamiento de una red neuronal</b>
<br>
Inicialización del modelo: de manera aleatoria se generan los pesos de la red neuronal.
![alt text](https://yt3.ggpht.com/a-/AN66SAyk49uNWUtt2mDTTxOdMNy5afiVHK3dFIvPVQ=s900-mo-c-c0xffffffff-rj-k-no)
<br>
El primer paso es la propagación hacia adelante, que consiste en propagar valores de una capa hacia la siguiente que actúan como su entrada. 
<br>
Cada una de las neuronas de una capa tiene un valor interno y una conexión hacia cada una de las neurones de la siguiente capa. Cada conexión tiene un peso asociado. En la propagación el valor interno de una neurona de la siguiente capa se calcula como la suma del valor interno de cada una de las neurones de la capa anterior multiplicado por el peso de la conexión con esa neurona. 
<br>
Al valor generado mediante el cálculo anteriormente mencionado se le aplica una función de activación. Dicha función existe ya que como los valores son generados aleatoriamente sería difícil determinar cuales valores activan o no una neurona. Por ello por ejemplo una de las funciones más conocidas de activación es la función sigmoide que siempre genera resultados entre 0 y 1(más negativos se acercan a 0, más positivos se acercan a 1). Luego en base a esto se determina si se activa o no la neurona.
<br>
![alt text](https://github.com/juanborssotto/js-neural-networks/blob/master/readme-imgs/network-1.png)
<br>
El siguiente paso es calcular el error de nuestra red neuronal. Necesitamos saberlo para determinar como actualizar su estado interno(pesos) y que genere resultados más precisos.
<br>
Para ello aplicamos una función de pérdida. La más conocida es la suma de los cuadrados, en la cual calculamos el valor absoluto de el output deseado menos el output realmente obtenido al cuadrado. El error total sería la suma de todos los errores de cada una de las neuronas de la output layer.
![alt text](https://github.com/juanborssotto/js-neural-networks/blob/master/readme-imgs/network-2.png)
<br>
Lo siguiente es la propagacion hacia atrás, que consiste en recorrer la red hacia atrás recalculando los nuevos pesos.
<br>
Existen muchas formas de hacerlo, entre ellas, por fuerza bruta(cambiando los pesos y viendo si el error total disminuye), por diferenciación, donde a través de la diferenciación matemática, se puede calcular que tanto se deben cambiar los pesos para generar una variación en algún sentido del error total.
<br>
Otro concepto interesante en esta parte del proceso, es la del ratio de aprendisaje(learning rate), utilizado para que cuando se recalculen los pesos se reduzca la variación en el cambio, y no provocar que nunca se puede llegar al punto exacto donde el peso queda en su estado más acertado.
![alt text](https://github.com/juanborssotto/js-neural-networks/blob/master/readme-imgs/network-3.png)

## Proyecto
Para hacer el proyecto elegí una herramienta online https://beta.observablehq.com, ya que permite utilizando javascript generar una aplicación que esta constantemente pendiente de los cambios del código, así por ejemplo uno puede insertar un gráfico y el mismo se actualizará cada vez que cambien sus variables de entrada generadas en el código.
<br>
Como proyecto elegí construir una pequeña red neuronal sin utilizar librerías que clasifica puntos(x, y) en un plano como a un lado o al otro de una línea que lo cruza. Lo elegí debido a que me pareció un problema con una complejidad acorde a ser la primera red neuronal que hago "from scratch".
<br>
Link al proyecto: https://beta.observablehq.com/@juanborssotto/javascript-neural-network-project-1

## Descripción del proyecto
La red neuronal no cuenta con hidden layers. Contiene una capa de entrada con dos inputs(x, y) y una capa de salida con dos neuronas que representan cada uno de los lados de la línea que corta el plano. 
<br>
Generé un array de objetos con propiedades x, y que representan los puntos y de manera aleatoria los pesos asociados a cada conexión entre neuronas. Además generé un gráfico que calcula con cada punto y los pesos si está de un lado o del otro de la línea.
<br>
Para recalcular los pesos lo hago mediante fuerza bruta, acercandolos lo más cercano al punto correcto.
<br>
Finalmente se puede ver el resultado en el gráfico, para aumentar la cantidad de elementos de entrenamiento se puede modificar la constante TRAINED DATA, y para quitar la animación que muestra como cambia el estado de los puntos, comentar las líneas:
<br>
```
//await setTimeout(() => {}, 1000)
//yield { weights, biases }
```
