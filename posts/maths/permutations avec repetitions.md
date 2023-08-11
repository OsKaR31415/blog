---
title: "permutations avec répétitions"
description: "Nombre de façons de placer tous les éléments d'un ensemble dans un $n$-uplet."
date: 2023-01-21
categories: [ maths ]
draft: true
---


::: {.callout-note icon=false}
## Définition

Soit $B = \{\!\!\{ \underbrace{a_1, a_1, a_1, a_1}_{n_1}, \underbrace{a_2, a_2}_{n_2}, \underbrace{a_3, a_3, a_3}_{n_3}, \dots, \underbrace{a_{k}, a_{k}, a_{k}, a_{k}}_{n_{k}} \}\!\!\}$ un [sac](sacs.md), avec $(n_{i})$ la multiplicité de $B$.

On note $N = \sum\limits_{i=1}^{k} n_{i}$ le nombre d'éléments de $B$ (la somme des multiplicités de chaque élément)

Le nombre de permutations (avec répétitions) des éléments de $B$ est le nombre de façons de placer **tous les éléments** de $B$ dans un $n$-uplet (de façon ordonnée).

$\boxed{\mathcal{P} = \frac{N!}{n_1! \times n_2! \times n_3! \times \cdots \times n_k!}}$

:::

# Formule

La formule est en quelque sorte déduite de celle des [permutations](permutation.md) : On a un ensemble à $N$ éléments, il y a donc $N!$ permutations de ces éléments. 

Mais comme on est dans un sac (on autorise des éléments répétés), il faut considérer que mélanger des éléments qui sont identiques ne change rien.

Par exemple, si un élément est répété 2 fois, inverser les positions de cet élément répété ne change pas la disposition : $(a, b, c, \overline{a}) = (\overline{a}, b, c, a)$ (ici, on met une barre pour montrer que la position des deux $a$ a été échangée, mais ils sont identiques, donc la configuration est la même).

Il faut donc considérer le nombre de permutations que l'on aurait s'il n'y avait pas de répétitions, pour éliminer ces configurations répétées :

Comme un élément $a_{i}$ est répété $n_{i}$ fois, il y à $n_i!$ mélanges possibles qui ne changent rien à la configuration (car ils ne mélangent que des éléments $a_{i}$)

On sait donc qu'il va faloir diviser par des $n_{k}!$ :

 - l'élément $a_{1}$ est répété $n_1$ fois, il faut donc diviser par $n_1!$
 - l'élément $a_2$ est répété $n_2$ fois, il faut donc diviser par $n_2!$
 - $\vdots$
 - l'élément $a_{k}$ est répété $n_{k}$ fois, il faut donc diviser par $n_{k}!$

On obtient donc bien la formule pour les permutations avec répétitions sur un [sac](sacs.md) de [multiplicité](sacs.md) $(n_{i})$ :

$\boxed{\mathcal{P} = \frac{N!}{n_1! \times n_2! \times n_3! \times \cdots \times n_{k}!}}$

Ou bien, avec la notation $\prod\limits$ pour les produits :

$\boxed{\mathcal{P} = \frac{N!}{\prod\limits_{i=1}^{k} \Big(n_{i}!\Big)}}$



