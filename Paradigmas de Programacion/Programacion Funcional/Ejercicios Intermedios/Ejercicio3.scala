def diferenciaMayor10(lista: List[Int], n: Int): List[Int] = {
    lista.map(elemento => elemento - n).filter(elemento => elemento > 10)
}

// Otra forma
// def diferenciaMayor10(lista: List[Int], n: Int): List[Int] = {
//     val listaDiferencias = lista.map(elemento => elemento - n)
//     listaDiferencias.filter(elemento => elemento > 10)
// }
