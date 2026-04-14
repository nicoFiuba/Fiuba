def merge[A](list1: List[A], list2: List[A]): List[A] = {
    list1 ::: list2
}

// La función merge es pura porque siempre devuelve el mismo resultado para los mismos argumentos y no tiene efectos secundarios, ya que retorna una nueva lista concatenada dejando las listas originales intactas (respeta la inmutabilidad).