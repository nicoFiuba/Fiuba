def filtrar(lista: List[List[Int]], n: Int): List[Int] = {
    lista.flatten.filter(elemento => elemento > n)
}