def fecha(): String = {
    LocalDate.now.format(DateTimeFormatter.ofPattern("yyyyMMdd"))
}

// La función fecha es impura porque devuelve un resultado diferente cada vez que se llama, ya que depende de la fecha actual. Además, no tiene efectos secundarios, pero su resultado no es predecible.