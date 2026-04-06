cursa(emiliano, paradigmas).
cursa(camila, algo2).
cursa(ramiro, tda).
cursa(micaela, paradigmas).

dicta(martin, algo2).
dicta(martin, tda).
dicta(mati, paradigmas).
dicta(fede, paradigmas).
dicta(nacho, paradigmas).

profesor(X,Y) :- dicta(X, Z), cursa(Y, Z).


% 1) ?- cursa(emiliano, algo2).
% Rta: false. La consulta pregunta si Emiliano cursa el curso de algo2, pero según la base de conocimientos, Emiliano cursa el curso de paradigmas, no algo2. Por lo tanto, la respuesta es falsa.

% 2) ?- cursa(emiliano, paradigmas).
% Rta: true. La consulta pregunta si Emiliano cursa el curso de paradigmas, y según la base de conocimientos, Emiliano sí cursa ese curso. Por lo tanto, la respuesta es verdadera.

% 3) ?- cursa(emiliano, algo3).
% Rta: false. La consulta pregunta si Emiliano cursa el curso de algo3, pero según la base de conocimientos, Emiliano no cursa ese curso. Por lo tanto, la respuesta es falsa.

% 4) ?- dicta(mati, paradigmas).
% Rta: true. La consulta pregunta si Mati dicta el curso de paradigmas, y según la base de conocimientos, Mati sí dicta ese curso. Por lo tanto, la respuesta es verdadera.

% 5) ?- dicta(fede, X).
% Rta: X = paradigmas. La consulta pregunta qué curso dicta Fede, y según la base de conocimientos, Fede dicta el curso de paradigmas. Por lo tanto, la respuesta es que X es igual a paradigmas.

% 6)  ?- dicta(X, paradigmas).
% Rta: X = mati ; X = fede ; X = nacho. La consulta pregunta quiénes dictan el curso de paradigmas, y según la base de conocimientos, Mati, Fede y Nacho dictan ese curso. Por lo tanto, la respuesta es que X puede ser igual a Mati, Fede o Nacho. Para que se muestren todas las opciones, hay que apretar ";" después de cada respuesta porque sino el programa se queda esperando infinitamente.

% 7) ?- profesor(martin, emiliano).
% Rta: false. La consulta pregunta si Martin es profesor de Emiliano, pero según la base de conocimientos, Martin dicta los cursos de algo2 y tda, mientras que Emiliano cursa el curso de paradigmas. Por lo tanto, la respuesta es falsa.

% 8)  ?- profesor(nacho, X).
% Rta: X = emiliano ; X = micaela. La consulta pregunta quien es alumno de Nacho, y según la base de conocimientos, Nacho dicta el curso de paradigmas, que es cursado por Emiliano y Micaela. Por lo tanto, la respuesta es que X puede ser igual a Emiliano o Micaela. Para que se muestren todas las opciones, hay que apretar ";" después de cada respuesta porque sino el programa se queda esperando infinitamente.
