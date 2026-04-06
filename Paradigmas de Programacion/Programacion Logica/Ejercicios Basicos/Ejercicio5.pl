% palabra(PalabraEntera, L1, L2, L3, L4, L5, L6, L7)

palabra(astante, a, s, t, a, n, t, e).
palabra(astoria, a, s, t, o, r, i, a).
palabra(baratto, b, a, r, a, t, t, o).
palabra(cobalto, c, o, b, a, l, t, o).
palabra(pistola, p, i, s, t, o, l, a).
palabra(statale, s, t, a, t, a, l, e).

crucigrama(H1, H2, H3, V1, V2, V3) :-
    % Definimos las 3 horizontales, el _ indica que no nos importa qué letra va en esa posición, solo nos interesa las letras que cruzan con las verticales (X1, X2, X3, X4, X5, X6, X7, X8, X9)
    % Letras:    1  2   3  4   5  6   7
    palabra(H1, _, X1, _, X2, _, X3, _),
    palabra(H2, _, X4, _, X5, _, X6, _),
    palabra(H3, _, X7, _, X8, _, X9, _),
    
    % Definimos las 3 verticales ¡Cruzando las variables X!
    % V1 cruza con la 2da letra de H1, H2 y H3 (X1, X4, X7)
    palabra(V1, _, X1, _, X4, _, X7, _),
    % V2 cruza con la 4ta letra de H1, H2 y H3 (X2, X5, X8)
    palabra(V2, _, X2, _, X5, _, X8, _),
    % V3 cruza con la 6ta letra de H1, H2 y H3 (X3, X6, X9)
    palabra(V3, _, X3, _, X6, _, X9, _),
    
    % Evitamos que Prolog use la misma palabra dos veces
    H1 \= H2, H1 \= H3, H1 \= V1, H1 \= V2, H1 \= V3,
    H2 \= H3, H2 \= V1, H2 \= V2, H2 \= V3,
    H3 \= V1, H3 \= V2, H3 \= V3,
    V1 \= V2, V1 \= V3,
    V2 \= V3.