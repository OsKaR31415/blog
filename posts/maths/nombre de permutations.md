---
title: "permutations (combinatoire)"
date: 2023-01-19
categories: [ maths ]
---

::: {.callout-note icon=false}
## Définition

On définit $P_{n}$ le nombre de permutations de $n$ éléments.

C'est donc le nombre d'éléments de $\mathfrak{S}_{n}$ : $P_{n} = \text{card} (\mathfrak{S}_{n})$

Mais surtout, on obtient la formule : $\boxed{P_{n}= n!}$
:::


# Interprétation

L'interprétation du nombre de permutations est immédiate, puisque $P_{n}$ compte le nombre de façons de "mélanger" (permuter) $n$ objets.

::: {.callout-tip}
## Exemples

Voici quelques questions de combinatoire dont la réponse passe par des permutations :

 - Combien y a-t-il de mélanges différents d'un jeu de 54 cartes ?
     - $P_{54} = 54! \approx 2.3 \cdot 10^{71}$
 - Combien de phrases peut-on former avec 10 mots différents
     - par exemple, avec "madame la marquise, vos beaux yeux me font mourir d'amour"
         - qui peut être permuté en "vos beaux yeux d'amour mourir me font, madame la marquise", ou bien "vos beaux yeux, madame la marquise, me font mourir d'amour" etc...
     - $P_{10} = 10! = 3628800$
:::


# Formule

Faire une permutations de $n$ éléments, c'est placer ces $n$ éléments dans $n$ emplacements.

On veut donc compter le nombre de façons de choisir ces placements

 - pour le $1^{\text{er}}$ élément, il y à $n$ emplacements possibles (ils sont tous libres)
 - pour le $2^{\text{ème}}$ élément, il y à $n-1$ emplacements possibles (un des emplacements est pris par le $1^{\text{er}}$ élément)
 - pour le $3^{\text{ème}}$ élément, il y à $n-2$ emplacements possibles
 - $\vdots$
 - pour le $n-2^{\text{ème}}$ élément, $3$ emplacements possibles
 - pour le $n-1^{\text{ème}}$, $2$ emplacements possibles
 - pour le $n^{\text{ème}}$ (et dernier), $1$ emplacement possible

Donc, le nombre de façons de placer ces $n$ éléments (le nombre de permutations de $n$ éléments) est $n\times (n-1)\times(n-2)\times\cdots \times 3 \times2\times 1 = n!$

D'où la formule : $\boxed{P_{n} = n!}$

