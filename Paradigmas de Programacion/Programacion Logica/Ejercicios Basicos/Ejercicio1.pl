% 1. Hechos (verdades absolutas e incondicionales que le damos al motor)
vehiculo(auto).
vehiculo(bicicleta).
vehiculo(moto).

tieneMotor(auto).
tieneMotor(moto).

% 2. Reglas de Inferencia (lógica condicional que relaciona hechos)
vehiculoConMotor(X) :- vehiculo(X), tieneMotor(X).


% --- CONSULTAS ---
% Son las preguntas que le hacemos al motor directamente en la consola de Prolog para obtener respuestas basadas en los hechos y reglas que hemos definido.
% Ejemplo: ?- vehiculoConMotor(auto).
% Esto le preguntará al motor si "auto" es un vehículo con motor, y la respuesta será "true" porque hemos definido que "auto" es un vehículo y tiene motor.
% Ejemplo: ?- vehiculoConMotor(bicicleta).
% Esto le preguntará al motor si "bicicleta" es un vehículo con motor, y la respuesta será "false" porque aunque "bicicleta" es un vehículo, no tiene motor según nuestros hechos.

% Ejemplo: ?- vehiculoConMotor(X).
% Esto le preguntará al motor qué vehículos tienen motor.
% El motor evalúa de arriba hacia abajo y se pausa en la primera respuesta válida:
% X = auto 
% IMPORTANTE: Para pedirle al motor que siga buscando más respuestas, 
% debemos presionar la tecla punto y coma (;). 
% Al hacerlo, el motor hará "backtracking" y nos dará la siguiente opción:
% X = moto. 
% Y como no hay más opciones posibles, finaliza la consulta.