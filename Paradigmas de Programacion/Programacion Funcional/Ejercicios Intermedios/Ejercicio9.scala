def topK(numeros: List[Int], k: Int, f: (Int, Int) => Int): List[Int] = {
    // 1. Ordenamos usando nuestra función 'f' como árbitro
    // 2. Nos quedamos con los primeros 'k'
    numeros.sortWith((a, b) => f(a, b) > 0).take(k)
}