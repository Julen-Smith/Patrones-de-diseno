# Patrones creacionales

Los Patrones creacionales son aquellos que nos permiten crean objetos. Estos patrones encapsulan el procedimiento de creación de un objecto y suelen trabajar mediante interfaces:

Es posible también encontrarte como me ha pasado a mí con que algunos de los patrones de diseño se parecen mucho unos a otros, pero realmente no es así, son pequeños matices los que las diferencian.
Similitudes
Diferencias entre factory method y abstract method

## Factory Method :

1 - Define una clase abstracta o interface para que sus subclases creen objetos que extienden de la misma clase base.\
\
2 - Los objetos específicos son creados por una o más clases concretas que extienden de la clase abstracta. \
\
3 - La fábrica delega el trabajo de la creación del objeto concreto a una de sus subclases, la cual puede o no hacer uso de un parámetro. \
\
4 - Cada fábrica concreta se especializa en crear solo un tipo concreto de objeto. \
\
5 - Caso de uso: Crear un objeto que tiene muchas dependencias o configuración que debe hacerse al inicializarlo, o en donde hay diferentes formas o algoritmos para crear le objeto. \

## Abstract Method :

1 - Define una clase abstracta o interface para que sus subclases creen objetos que pertenecen a una familia de diferentes objetos relacionados entre sí.\
\
2 - Es una fábrica de fábricas, los objetos específicos son creados por una o más clases concretas que extienden de la clase abstracta. \
\
3 - Cada fábrica se especializa en crear un tipo de objeto. \
\
4 - Una fábrica generalizada contiene una o más fábricas especializadas donde cada una produce un tipo concreto de objeto. \
\
5 - Caso de uso: Crear múltiples objetos de distintos tipos pero que tienen una relación o dependencia con otros; esto es, crear una familia de objetos.


