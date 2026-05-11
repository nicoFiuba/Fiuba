% 1) Indicar si las siguientes consultas dan true o false. Justificar.

% 1. 2 is 2.
% TRUE. El operador 'is' evalúa matemáticamente el lado derecho (da 2) y lo unifica con el lado izquierdo (2).

% 2. 2 is 1 + 1.
% TRUE. El operador 'is' evalúa matemáticamente el lado derecho (1+1 da 2) y lo unifica con el lado izquierdo (2).

% 3. 2 = 2.
% TRUE. El operador '=' realiza unificación. Como ambos lados son átomos idénticos, unifican con éxito.

% 4. 2 = 1 + 1.
% FALSE. El operador '=' NO evalúa matemáticas, solo unifica estructuras. El átomo '2' no es estructuralmente idéntico al término compuesto '1 + 1' (o +(1,1)).

% 5. 3 + 2 = 3 + 2.
% TRUE. Aunque el operador '=' no sabe sumar, la estructura del lado izquierdo es idéntica carácter por carácter a la estructura del lado derecho, por lo que unifican.

% 6. 4 =:= 4.
% TRUE. El operador '=:=' evalúa matemáticamente AMBOS lados y luego compara sus resultados numéricos (4 es igual a 4).

% 7. 4 =:= 2 + 2.
% TRUE. El operador '=:=' evalúa ambos lados. El izquierdo evalúa a 4 y el derecho a 4. Como los resultados numéricos son iguales, es verdadero.

% 8. 2 < 6.
% TRUE. Operador de comparación aritmética estándar. 2 es menor que 6.

% 9. 3 > 4.
% FALSE. Operador de comparación aritmética estadar. 3 no es mayor que 4.

% 10. 2 =/= 2.
% FALSE. El operador '=/=' evalúa y compara si los valores numéricos son distintos. Como 2 y 2 valen lo mismo, la desigualdad es falsa.

% 11. 6 =/= 100.
% TRUE. Al evaluar, el valor numérico 6 es distinto del valor numérico 100.
