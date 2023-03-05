---
title: "Permutation comme produit de cycles disjoints"
date: 2023-01-20
categories: [ maths ]
draft: true
---

::: {.callout-note icon=false}
## Théorème

Toute [permutation](permutation.md) peut être décomposée en un [produit](composition-de-permutations) de [cycles](p cycle.md) disjoints (c'est-à-dire qui ne modifient pas les mêmes éléments)

:::

# Visualisation

Si on considère la permutation $\begin{pmatrix}1&2&3&4&5&6\\3&4&1&6&5&2\end{pmatrix}$, on se rend compte que l'elle "_contient_" deux [cycles](p cycle.md) : $\begin{pmatrix}1&2&3&4&5&6\\3&2&1&4&5&6\end{pmatrix}$ (une [transposition](transposition.md)) et $\begin{pmatrix}1&2&3&4&5&6\\ 1&4&3&6&5&2\end{pmatrix}$

Ces deux cycles sont bien **disjoints** : l'un permute les éléments $\{ 1, 3 \}$, et l'autre les éléments $\{ 2, 4, 6kl k \}$

![](_images/permutations/decomp_proc_cycles_disjoints.gif)

