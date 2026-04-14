% Esta mal la base de conocimiento, al empezar con mayuscula se interpreta como una variable y en realidad se quiere representar un hecho.
% socio(Hernan, Atlanta).               % socio(hincha, club)
% socio(Juan, Ferro).

% asistio(Hernan, Atlanta, Almagro, 6). % asistio(hincha, club1, club2, nrofecha)
% asistio(Juan, Ferro, Brown, 5).
% asistio(Juan, Chacarita, Chicago, 8).

% Esta es la base de conocimiento corregida:

socio(hernan, atlanta).               % socio(hincha, club)
socio(juan, ferro).

asistio(hernan, atlanta, almagro, 6). % asistio(hincha, club1, club2, nrofecha)
asistio(juan, ferro, brown, 5).
asistio(juan, chacarita, chicago, 8).

puedeComprar(X, C1, _C2, _F) :- socio(X, C1).
puedeComprar(X, _C1, C2, _F) :- socio(X, C2).

puedeComprar(X, _C1, _C2, F) :- 
    F1 is F - 1,
    asistio(X, _, _, F1).

puedeComprar(X, _C1, _C2, F) :- 
    F2 is F - 2,
    asistio(X, _, _, F2).

