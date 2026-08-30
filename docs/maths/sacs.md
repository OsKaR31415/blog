---
title: "sacs (multi-ensembles)"
description: "ensemble avec répétition"
date: 2023-01-04
categories: [ maths ]
image: "_images/sac_ecole.png"
---


::: {.callout-note icon=false}
## Définition

Un sac, ou multi-ensemble, est un ensemble dans lequel on autorise la répétition d'éléments.

Cela signifie que, contrairement aux ensembles, un élément peut être contenu plusieurs fois dans un sac.

**Notation :** $\{\!\!\{ a, a, a, b, c, c, d, d, d, d \}\!\!\}$
:::


::: {.callout-note icon=false collapse=true}
## Définition formelle

On définit un sac $B$ comme un couple $(E, f)$, où :
 - $E$ est l'ensemble des éléments du sac (sans répétitions)
     - $E$ est appelé le **support** de $B$
 - $f : E \to \mathbb{N}$ est la fonction qui, à un élément de $E$, associe son nombre de répétitions 
     - $f$ est appelée la **multiplicité** de $B$

Par exemple, le sac $\{\!\!\{ a, a, a, b, c, c \}\!\!\}$
Se définit avec :
 - $E = \{ a, b, c \}$
 - $f$ telle que :
     - $f(a) = 3$
     - $f(b)=1$
     - $f(c)=2$
:::


# Propriétés

Soit $B$ un sac

 - on appelle **support** de $B$ l'ensemble des éléments de $B$ (donc, sans répétition)
     - Par exemple, le support de $\{\!\!\{ a, a, a, b, c, c, d, d, d, d \}\!\!\}$ est $\{ a, b, c, d \}$
 - on appelle **multiplicité** de $B$ la fonction qui, à un élément de $B$, associe le nombre de répétitions de cet élément
     - Par exemple, si $f$ est la multiplicité de $\{\!\!\{ a, a, a, b, c, c, d, d, d, d \}\!\!\}$, alors $f(a) = 3$, $f(b) = 1$, $f(c) = 2$ et $f(d)=4$

<br/>
Si $E$ et $f$ sont le support et la multiplicité de $B$

 -  $\text{card}(B) = \sum\limits_{x \in E} f(x)$
     - le cardinal est la somme des multiplicités de chaque valeur de $E$
     - c'est évident, puisque la multiplicité est le nombre de répétitions de chaque élément


# Utilité

En combinatoire, les sacs permettent d'exprimer la possibilité de répéter un élément un certain nombre de fois.



