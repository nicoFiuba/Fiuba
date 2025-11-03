import java.math.BigInteger;

public class Ejercicio11 {
    
    public static BigInteger karatsuba(BigInteger x, BigInteger y) {
        
        int signo = x.signum() * y.signum();
        x = x.abs();
        y = y.abs();
            
        if (x.compareTo(BigInteger.TEN) < 0 || y.compareTo(BigInteger.TEN) < 0) {
            return x.multiply(y).multiply(BigInteger.valueOf(signo));
        }
        
        int longitud = Math.max(x.toString().length(), y.toString().length());
        
        if (longitud % 2 != 0) {
            longitud++; 
        }
            
        int longMedia = longitud / 2; 
    
        BigInteger a = x.divide(BigInteger.TEN.pow(longMedia));
        BigInteger b = x.remainder(BigInteger.TEN.pow(longMedia));
        BigInteger c = y.divide(BigInteger.TEN.pow(longMedia));
        BigInteger d = y.remainder(BigInteger.TEN.pow(longMedia));
    
        BigInteger ac = karatsuba(a, c); 
        BigInteger bd = karatsuba(b, d); 
        BigInteger abcd = karatsuba(a.add(b), c.add(d)); 
    
        BigInteger adPlusBc = abcd.subtract(ac).subtract(bd);
    
        BigInteger resultado = ac.multiply(BigInteger.TEN.pow(2 * longMedia)).add(adPlusBc.multiply(BigInteger.TEN.pow(longMedia))).add(bd);
    
        return resultado.multiply(BigInteger.valueOf(signo));
    }
        
    public static void main(String[] args) {
        
        BigInteger num1 = new BigInteger("12345678901234567890");
        BigInteger num2 = new BigInteger("98765432109876543210");
    
        BigInteger resultado = karatsuba(num1, num2);
            
        System.out.println("Resultado de Karatsuba: " + resultado);
    
    }

}
