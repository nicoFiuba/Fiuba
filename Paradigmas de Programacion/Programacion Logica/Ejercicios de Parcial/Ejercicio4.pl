% Esta mal la base de conocimiento, al empezar con mayuscula se interpreta como una variable y en realidad se quiere representar un hecho.
% socio(Hernan, Atlanta).
% socio(Juan, Ferro).
% La forma correcta es: socio(hincha, club).

% asistio(Hernan, Atlanta, Almagro, 6).
% asistio(Juan, Ferro, Brown, 5).
% asistio(Juan, Chacarita, Chicago, 8).
% La forma corerrecta es: asistio(hincha, club1, club2, nrofecha).


% Esta es la base de conocimiento corregida:
socio(hernan, atlanta).
socio(juan, ferro).

asistio(hernan, atlanta, almagro, 6).
asistio(juan, ferro, brown, 5).
asistio(juan, chacarita, chicago, 8).

puedeComprar(X, C1, _, _) :- % Verifico si X es socio de C1, en cuyo caso puede comprar entradas para este partido.
    socio(X, C1).

puedeComprar(X, _, C2, _) :- % Verifico si X es socio de C2, en cuyo caso puede comprar entradas para este partido.
    socio(X, C2).

puedeComprar(X, _, _, F) :- % Verifico si X asistió a un partido en la fecha anterior a F, en cuyo caso puede comprar entradas para este partido. 
    asistio(X, _, _, F1),
    F is F1 + 1.

puedeComprar(X, _, _, F) :- % Verifico si X asistió a un partido en la fecha dos fechas antes de F, en cuyo caso puede comprar entradas para este partido.
    asistio(X, _, _, F2),
    F is F2 + 2.
