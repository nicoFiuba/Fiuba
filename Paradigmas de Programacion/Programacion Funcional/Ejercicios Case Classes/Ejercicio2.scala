case class Punto(x: Double, y: Double) {
    // La función vive adentro del punto. 'this' es el punto actual, 'otro' es el que le pasamos.
    def distanciaA(punto: Punto): Double = {
        Math.hypot(punto.x - this.x, punto.y - this.y)
    }
}
