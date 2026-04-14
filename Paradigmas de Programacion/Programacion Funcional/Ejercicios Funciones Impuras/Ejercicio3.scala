def contar(l: List[Int], e: Int): Int = {
    var cont = 0;
    l.foreach(elemento => {
        if (elemento == e) {
            cont = cont + 1
        }
    })

    cont
}

// La función contar es impura porque utiliza una variable mutable (cont) para contar las ocurrencias de e en la lista l. Además, tiene un efecto secundario al modificar el valor de cont durante la ejecución de la función.
