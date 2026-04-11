% 1. Definimos los dominios (siempre en minúscula para que sean átomos)
beca(25000).
beca(30000).
beca(35000).
beca(40000).

carrera(astronomia).
carrera(ingles).
carrera(filosofia).
carrera(fisica).

% 2. Regla principal que busca la solución
solucion(Estudiantes) :-
    % Definimos la plantilla de nuestra solución: [Nombre, Carrera, Beca]
    Estudiantes = [
        [carrie, CarreraCarrie, BecaCarrie],
        [erna,   CarreraErna,   BecaErna],
        [ora,    CarreraOra,    BecaOra],
        [tracy,  CarreraTracy,  BecaTracy]
    ],

    % --- ASIGNACIÓN DE BECAS ---
    beca(BecaCarrie), beca(BecaErna), beca(BecaOra), beca(BecaTracy),
    distintas([BecaCarrie, BecaErna, BecaOra, BecaTracy]),
    
    % Pista: Erna tiene 10.000 USD más que Carrie
    BecaErna is BecaCarrie + 10000,

    % --- ASIGNACIÓN DE CARRERAS ---
    carrera(CarreraCarrie), carrera(CarreraErna), carrera(CarreraOra), carrera(CarreraTracy),
    distintas([CarreraCarrie, CarreraErna, CarreraOra, CarreraTracy]),

    % Pista: Ora estudia Inglés o Filosofía (usamos el ';' que significa OR)
    (CarreraOra = ingles ; CarreraOra = filosofia),

    % --- PISTAS CRUZADAS ---
    
    % Pista: El estudiante de Física tiene una beca 5.000 USD mayor que Carrie
    member([_, fisica, BecaFisica], Estudiantes),
    % La estructura de member es: member(Elemento_A_Buscar, Lista_Donde_Buscar)
    
    BecaFisica is BecaCarrie + 5000,

    % Pista: El de Astronomía tiene una beca menor que Ora
    member([_, astronomia, BecaAstro], Estudiantes),
    BecaAstro < BecaOra,

    % Pista: Tracy tiene una beca mayor que el que estudia Inglés
    member([_, ingles, BecaIngles], Estudiantes),
    BecaTracy > BecaIngles.

% 3. Regla auxiliar para asegurar que no haya elementos repetidos en una lista
distintas(L) :- 
    sort(L, Sorted), 
    length(L, Longitud), 
    length(Sorted, Longitud).

