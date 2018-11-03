# js-neural-networks

## Presentación

<b>¿Qué es una red neuronal?</b>
Es un modelo computacional basado en un gran conjunto de unidades neuronales simples de forma aproximadamente análoga al comportamiento observado en los axones de las neuronas en los cerebros biológicos.
Como se observa en la imágen la misma para entrenar el modelo el mismo recibe inputs, realiza un procesamiento y genera outputs, que luego se utilizarán para cambiar el estado interno de la misma. Una vez entrenada, el output ya se utiliza directamente como el resultado de lo que queremos predecir. 
![alt text](https://cdn-images-1.medium.com/max/800/1*fNAjKoWt21pdzlkTmlP3pw.png)

<b>Algunos usos en la vida real</b>
<br>
Detección de fraude con los movimientos de tarjeta de crédito usado por empresas como Eurocard Nederland, Mellon Bank, First USA Bank.
![alt text](https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSy_nL0-bVlWXjZfGyyByLio7Xv6pioDKbqHWKywnYF2S6P9bwu)
<br>
Detección de células cancerígenas utilizado por The US Food and Drug Administration.
![alt text](http://news.mit.edu/sites/mit.edu.newsoffice/files/images/2016/MIT-Cancer-Cell-Growth_0.jpg)
<br>
Caso interesante a nivel industrial
<br>
La empresa Fanuc, originaria de Japón, que produce y comercializa robots para diferentes aplicaciones industriales plantearon utilizar una red neuronal en vez de programar directamente lo que el robot tiene que hacer. Una gran ventaja de esto es que la información que los mismos aprenden puede estar centralizada en un sólo lugar y ser compartida por todos, por lo que lo que un robot aprende en 8 horas, 8 pueden aprenderlo en 1 hora. Ejemplo de uno de los robots en el cual aplicaron una red neuronal.
<br>
El robot tiene como aplicación recoger cilindros de un recipiente y moverlos a otro. Al principio comienza haciendolo al azár, tomando una foto antes de cada levantamiento, y clasificandola en éxito o fracaso. Al mismo tiempo la envía a una red neuronal para que sea entrenada.
![alt text](https://github.com/juanborssotto/js-neural-networks/blob/master/readme-imgs/fanuc-1.png)
Luego de 1000 intentos aprende que ciertas posiciones de los cilindros siempre llevan al fracaso, y luego de 5000 intentos cuáles son las posiciones que llevan al éxito.
![alt text](https://github.com/juanborssotto/js-neural-networks/blob/master/readme-imgs/fanuc-2.png)
Finalmente, como resultado, luego de 1000 intentos tiene un porcentaje de éxito del 60% y luego de 5000 intentos un porcentaje de éxito de 90%.
![alt text](https://github.com/juanborssotto/js-neural-networks/blob/master/readme-imgs/fanuc-3.png)
Link al video: https://www.youtube.com/watch?v=ydh_AdWZflA

![alt text](https://github.com/juanborssotto/js-neural-networks/blob/master/readme-imgs/network-1.png)
![alt text](https://github.com/juanborssotto/js-neural-networks/blob/master/readme-imgs/network-2.png)
![alt text](https://github.com/juanborssotto/js-neural-networks/blob/master/readme-imgs/network-3.png)
