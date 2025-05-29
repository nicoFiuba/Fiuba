import doctest

def aprobo_cursada(puntajes_maximos, puntajes_otorgados):
    """
    >>> print(aprobo_cursada([10, 10, 10, 10, 10], [6, 6, 6, 6, 6, 6]))
    True
    >>> print(aprobo_cursada([10, 10, 10, 10, 10, 10], [1, 6, 6, 6, 6, 6, 6]))
    False
    """
    aprobo = True

    i= 0
    while i < len(puntajes_maximos) and aprobo:
        if puntajes_otorgados[i] < puntajes_maximos[i]* 0.6:
            aprobo = False
        i += 1
    return aprobo

print(aprobo_cursada([10, 20, 15], [6, 15,12])) # True
print(aprobo_cursada([10, 20, 15], [6, 8,12])) # False
print(aprobo_cursada([10, 20, 15, 30], [6, 12, 9, 12])) # False
print(doctest.testmod())