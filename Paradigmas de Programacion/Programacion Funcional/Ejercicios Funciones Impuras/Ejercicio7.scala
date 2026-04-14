import java.io.PrintWriter

def guardarEnArchivo(texto: String, ruta: String): Unit = {
    val escritor = new PrintWriter(ruta)
    try {
        escritor.write(texto)
        } finally {
            escritor.close()
            }
}

// La función guardarEnArchivo es impura porque tiene el efecto secundario de interactuar con el exterior, modificando el estado del sistema de archivos al escribir en el disco. 