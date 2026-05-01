'''
-----------------------------------------------------------------------------
EJERCICIO 1: REDES DE FLUJO (La topología de la red)
-----------------------------------------------------------------------------
Enunciado:
Como parte del equipo técnico de una competencia de programación, diseñaste una red de servidores locales interconectados para que los participantes puedan subir su código. Existe un servidor principal (Fuente S) que provee la conexión general, y un servidor de evaluación (Sumidero T) donde se testean los proyectos. En el medio hay decenas  de routers interconectados mediante cables bidireccionales. Te preocupa la robustez de esta red ante posibles sabotajes o caídas de tensión. Se te pide diseñar un algoritmo que, dada la red, determine cuál es la cantidad MÍNIMA de routers (nodos intermedios) que se pueden apagar para que sea IMPOSIBLE que cualquier paquete de datos llegue desde S hasta T, dejando el evento incomunicado.
(Asumir que los servidores S y T están blindados y no se pueden apagar).

Se pide:
1. Explicar detalladamente cómo modelar este problema usando Redes de Flujo (Detallar quiénes son los nodos, las aristas y cuáles son las capacidades).
2. Indicar qué algoritmo clásico utilizarías para resolverlo.
3. Mencionar y explicar qué teorema teórico garantiza que tu solución es correcta.

-----------------------------------------------------------------------------
RESOLUCIÓN ESPERADA:


'''

