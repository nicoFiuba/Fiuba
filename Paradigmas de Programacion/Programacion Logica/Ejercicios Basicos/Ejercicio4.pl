progenitor(a,b).  
progenitor(a,c). 
progenitor(b,d).
progenitor(b,e). 
progenitor(c,f).

hermano(X, Y) :- progenitor(Z, X), progenitor(Z, Y), X \= Y. % El  \= significa distinto, es decir, que X e Y no pueden ser iguales.
% Los hermanos son aquellos que comparten al mismo progenitor, por lo tanto, para determinar si X e Y son hermanos, se verifica si existe un Z que sea progenitor de ambos X e Y, y además se asegura que X e Y no sean la misma persona.

primo(X, Y) :- progenitor(Z, X), hermano(Z, W), progenitor(W, Y).
% Los primos son aquellos que tienen padres que son hermanos, por lo tanto, para determinar si X e Y son primos, se verifica si existe un Z que sea progenitor de X, y un W que sea hermano de Z, y además W debe ser progenitor de Y.

nieto(X, Y) :- progenitor(Z, X), progenitor(Y, Z).
% Los nietos son aquellos que tienen un abuelo o abuela como progenitor, por lo tanto, para determinar si X es nieto de Y, se verifica si existe un Z que sea progenitor de X, y Y debe ser progenitor de Z.

descendiente(X, Y) :- progenitor(Y, X).
descendiente(X, Y) :- progenitor(Y, Z), descendiente(X, Z).
% Los descendientes son aquellos que tienen un ancestro como progenitor, por lo tanto, para determinar si X es descendiente de Y, se verifica si Y es progenitor directo de X, o si existe un Z que sea progenitor de X y Y es progenitor de Z, lo que implica que X es descendiente de Y a través de Z.