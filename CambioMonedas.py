def cambio_monedas(a, p):
    n = len(a)
    m = [[float('inf') for _ in range(p+1)] for _ in range(n)] # Guarda el número mínimo de todas las monedas utilizadas para lograr la cantidad p
    s = [[float('inf') for _ in range(p+1)] for _ in range(n)] # Guarda el número de monedas de la denominación i utilizadas para lograr la cantidad p con el mínimo número total de monedas
    resultado = [0 for _ in range(n)]  

    for j in range(p+1): # Solución al problema cuando solo se tiene la moneda de la primera denominación
        if j % a[0] == 0:
            m[0][j] = j // a[0]
            s[0][j] = j // a[0]
    
    for i in range(1, n):
        for j in range(p+1):
            if ((j >= a[i]) and (j % a[i] == 0)):
                m[i][j] = j // a[i]
                s[i][j] = j // a[i]
            
            elif (j > a[i]):
                for k in range(j//a[i]+1): # Complejidad O(n*p^2)
                    q = k + m[i-1][j - k*a[i]]
                    
                    if q < m[i][j]:
                        m[i][j] = q
                        s[i][j] = k
            
            else: # j < a[i]
                m[i][j] = m[i-1][j]
                s[i][j] = 0
            
    for i in range(n-1, -1, -1): # Construcción de la solución
        resultado[i] = s[i][p]

        if resultado[i] == float('inf'):
            return "No hay solución"
        
        p -= int(resultado[i] * a[i])
    
    return resultado
    

if __name__ == "__main__":
    a = [1, 7, 10]
    p = 34
    print(cambio_monedas(a, p))

