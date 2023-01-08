---
title: "combinaisons"
date: 2023-01-05
categories: [ maths ]
image: "_images/combinaison_spatiale.png"
draft: false
---

::: {.callout-note icon=false} 
## Définition
$\displaystyle \binom{n}{k} = \frac{n!}{k!(n-k)!}$
Le nombre de façons de choisir $k$ éléments parmi un ensemble de $n$ éléments (sans ordre)

C'est le nombre d'ensembles à $k$ éléments contenus dans un ensemble à $n$ éléments
 - on utilise des ensembles car on a pas de répétitions d'un même élément, et que l'ordre n'est pas important
:::

# Interprétation

Comme dit dans la définition, $\displaystyle \binom{n}{k}$ est le nombre de façons de choisir $k$ éléments dans un ensemble de $n$ éléments.

::: {.callout-warning}
## Attention

Les combinaisons sont **sans répétition**, par opposition avec les [combinaisons avec répétitions](https://fr.wikipedia.org/wiki/Combinaison_avec_r%C3%A9p%C3%A9tition).

Cela veut dire que l'on ne peut choisir qu'une seule fois chaque élément.
:::

::: {.callout-tip collapse="true"}
## Exemples
Voici quelques questions de combinatoire dont la réponse passe par une combinaison :

 - Combien de nouvelles couleurs peut-on faire en mélangeant 2 couleurs parmi 5 couleurs de base (cyan, magenta, jaune, noir, blanc)
     - $\displaystyle \binom{5}{3} = 10$
 - Combien de "mains" de 5 cartes peut-on former avec un jeu de 52 cartes ?
     - $\dbinom{52}{5} = 2\,598\,960$
 - combien de "livres" différents peut-on former en choisissant 50 pages dans un dictionnaire de $100$ pages (sans considérer l'ordre de ces pages) ?
     - $\displaystyle \binom{100}{50} = 100\,891\,344\,545\,564\,193\,334\,812\,497\,256 \approx 10^{30}$ (beaucoup)
:::


# Formule

La formule pour les combinaisons vient de celle pour les [arrangements](arrangements.md).

Par définition, un arrangement considère l'ordre, quand une combinaison ne le considère pas (car l'un compte les $k$-uplets, quand l'autre compte les ensemble de cardinal $k$).

Or, on sait qu'il y à $k!$ façons d'arranger $k$ éléments.

Donc, on sait qu'il y à $k!$ fois plus d'arrangements que de combinaisons pour des mêmes coefficients : $\displaystyle \binom{n}{k} = k! \times A_{n}^{k}$

On en déduit : $\displaystyle \binom{n}{k} = k! \times \frac{n!}{(n - k)!}$, soit :

$\boxed{\binom{n}{k} = \frac{n!}{k!(n-k)!}}$


