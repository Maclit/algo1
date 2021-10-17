# Project

## Part 1

En suivant le master theorem :

a = 2
b = 2
d = 1

On a T(n) = 2T(n/2) + O(n)

a = b**2, la complexité est donc O(n log(n))

## Part 2

L'heuristic utilisée est le nombres d'edges sur chaque node.

## Part 3

Un chemin Eulerian est présent quand chaque node à un nombre de connexions égales.
Ce chemin passe par chaque edge du graph une fois.
Le line graph d'un tel graph va convertir ces edges en nodes.
On aura donc un chemin qui passe par chaque node une fois.
Cela correspond un chemin Hamiltonian.
On conclue donc que le line graph d'un graph Eulerian est un graph Hamiltonian.