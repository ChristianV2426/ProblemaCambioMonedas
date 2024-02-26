
# Problema del cambio de monedas

  
**Solución con programación dinámica**

**Entrada:**  $a = \{a_1, a_2, ..., a_n\}, \ p$ // Denominaciones disponibles y cantidad a cambiar

**Salida:**  $\{k_1, k_2, ..., k_n\}$ // Número de monedas de cada denominación requeridas para lograr la menor cantidad total de monedas

Sea $a_{1i} = \{a_1, a_2, ..., a_i\}$ la secuencia que representa las denominaciones de a que van desde $a_1$ hasta $a_i$, con $1 \lt i \lt n$.

**1) Caracterización de la estructura de la estructura de la solución óptima:**
La solución óptima al problema original $cambio(a_{1n}, \ p)$ pasa por la solución óptima del subproblema $cambio(a_{1{n-1}}, \ p - k * a_n)$, para algún $k \ \ (0  \le k \le  \frac{p}{a_n})$ que garantice que $k + cambio(a_{1{n-1}}, p - k * a_n)$ sea mínima. Por lo tanto el problema original se soluciona con soluciones óptimas a instancias más pequeñas del mismo.

**2) Definición recursiva del valor de la solución óptima:**
Sea $m[i, j]$ el mínimo número de monedas necesario para alcanzar la cantidad $j$ a partir de las denominaciones $a_{1i}$. Entonces teniendo en cuenta la subestructura óptima del problema, $m[i, j]$ se puede definir recursivamente como:

$$m[i, j] =
\begin{cases} 
    \frac{j}{a_i} & \ \text{si} \ j \ge a_i \wedge (j \ \text{mod} \ a_i) = 0 \\
    min_{0  \le \ k \ \le  \frac{j}{a_i}} \{ k + m[i-1, j -  (k * a_i)]\} & \ \text{si} \ j \gt a_i \wedge (j \ \text{mod} \ a_i) \ne 0 \\
    m[i-1, j] & \ \text{si} \ j < a_i
\end{cases}$$

**3) y 4) Cálculo del valor de la solución óptima y su construcción (algoritmo):**
Como la implementación recursiva de $m[i, j]$ generaría un algoritmo con complejidad exponencial, entonces se plantea la solución con programación dinámica que involucre memorización de soluciones óptimas de subproblemas más pequeños. El archivo CambioMonedas.py plantea una aproximación bottom-up.
