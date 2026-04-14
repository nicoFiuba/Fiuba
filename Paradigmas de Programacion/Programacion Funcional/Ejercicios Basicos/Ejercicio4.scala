def aplicar(lista: List[Int], f: (Int, Int) => Int): List[Int] = {
    lista.map(elemento => f(elemento, elemento))
}
