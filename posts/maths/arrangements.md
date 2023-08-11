---
title: "arrangements"
description: ""
date: 2023-01-05
categories: [ maths ]
---

::: {.callout-note icon=false}
## Définition

On définit $A_{n}^{k}$ (lire "$A$, $n$, $k$"), les arrangements de $k$ objets d'un ensemble de $n$ objets, comme **le nombre de $k-uplets$ d'éléments d'un ensemble à $n$ éléments**.

On a : $\displaystyle A_{n}^{k} = \frac{n!}{(n-k)!}$

**Note :** on dit aussi parfois "arrangements dans $n$ de $k$ éléments" pour $A_{n}^{k}$

C'est le nombre de $k$-uplets d'éléments d'un ensemble à $n$ éléments
:::

# Interprétation

On peut interpréter $A_{n}^{k}$ comme le nombre de façons de choisir $k$ éléments dans un ensemble de $n$ éléments, si l'ordre des éléments compte.

::: {.callout-tip collapse=true}
## Exemples
Voici quelques questions de combinatoire dont la réponse passe par des arrangements :

 - Combien y a-t-il de nombres avec 3 chiffres distincts ?
     - autrement dit : combien de façons de choisir 3 chiffres parmi les 10 qui existent (si l'ordre est important) ?
     - $A_{10}^{3} = 720$

:::

# Formule

Si on choisit $k$ éléments, et que l'ordre compte, alors :

 - pour le premier élément, on a $n$ possibilités
 - pour le deuxième élément, on a $n - 1$ possibilités, car on ne peut pas choisir deux fois le premier élément
 - pour le troisième, $n - 2$ possibilités
 - pour le $4^{\text{ème}}$, $n-3$ possibilités
 - $\vdots$
 - pour le $k-1^{\text{ème}}$, $n-k + 2$ possibilités
 - pour le $k^{ème}$ élément, $n - k + 1$ possibilités

Donc, en tout, on a $n \times (n-1) \times (n-2) \times \cdots \times (n-k+1)$ possibilités.

On peut exprimer cela comme le produit des nombres de $n-k+1$ jusqu'à $n$ : $\prod\limits_{i = n-k+1}^{n} i$.

Puisqu'on veut le produit jusqu'à $n$ (donc $n!$), mais sans les nombres de $1$ à $n-k$ inclus (donc $(n-k)!$), comme $\dfrac{n!}{(n-k)!}$

On a donc bien la formule : $\boxed{A_{n}^{k} = \frac{n!}{(n-k)!}}$

