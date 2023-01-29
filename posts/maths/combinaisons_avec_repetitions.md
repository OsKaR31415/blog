---
title: "combinaisons avec répétitions"
date: 2023-01-06
categories: [ maths ]
---

::: {.callout-note icon=false}
## Définition
$K _{n}^{k} = \dbinom{n+k-1}{k}$

On note $K{n}^{k}$ les **combinaisons avec répétitions** dans $n$ de $k$.

C'est le **nombre de [sacs](sacs.md) à $k$ éléments inclus dans un ensemble à $n$ éléments**
 - on utilise des sacs car on autorise la répétition mais que l'ordre n'est pas important
:::


::: {.callout-note collapse=true}
##  Autres notations
Les combinaisons avec répétitions sont aussi notées $\Gamma _{n}^{k}$.

Une notation que j'apprécie particulièrement est $\begin{pmatrix}\begin{pmatrix}k\\n\end{pmatrix}\end{pmatrix}$, car c'est une notion similaire aux [combinaisons](combinaisons.md), mais avec des [sacs](sacs.md) plutôt que des ensembles (et que les sacs sont notés avec des doubles accolades : $\{\!\!\{ a, a, a, b, \dots \}\!\!\}$)
:::


::: {.callout-note icon=false collapse=true}
Définition

$K_{n}^{k}$ est le nombre de [sacs](sacs.md) de cardinal $k$ distincts dont le support est inclus dans un ensemble de cardinal $n$
:::


# Formule 

On peut représenter un [sac (ou multi-ensemble)](sacs.md) par une liste de points cercles par des barres.

Par exemple, le [sac](sacs.md) $\{\!\!\{ a; a; c; c; c; d \}\!\!\}$ avec des éléments pris dans $\{ a; b; c; d \}$ est représenté comme $\bigcirc \bigcirc \mid \; \mid \bigcirc \bigcirc \bigcirc \mid \bigcirc$ (avec un espace vide, car il n'y à aucun $b$).

Si on part d'un ensemble avec $n$ éléments, et qu'on forme des [sacs](sacs.md) de taille $k$. Dans la liste équivalente, on sait alors qu'il y aura $k + n - 1$ emplacements : $k$ cercles $+$ $n - 1$ barres. Alors, le nombre de [sacs](sacs.md) que l'on peut former ainsi correspond au nombres de façon de placer les $k$ cercles parmi les $k + n - 1$ emplacements, soit $\dbinom{k+n-1}{k}$.

Or, on sait que le nombre de sacs à $k$ éléments pris dans un ensemble à $n$ éléments est justement $K _{n}^{k}$ (Voir définition). Donc, on a démontré la formule :

$\boxed{K _{n}^{k} = \dbinom{n + k - 1}{k}}$


