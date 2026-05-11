def juntarNumeros(lista: List[Int]): List[Int] = {
    // 1. Agrupamos por el número en sí
    // 2. Nos quedamos solo con los "valores" (las listas de repetidos)
    // 3. Aplastamos las listas internas en una sola
    // 4. Lo forzamos a ser List (porque .values devuelve un Iterable genérico)
    
    lista.groupBy(identity).values.flatten.toList
}