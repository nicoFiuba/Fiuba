def primerosMilPrimos(): List[Int] = {
    LazyList.from(2).filter(n => (2 until n).forall(divisor => n % divisor != 0)).take(1000).toList
}
