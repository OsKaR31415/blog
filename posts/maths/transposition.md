---
title: "transposition"
date: 2023-01-19
categories: [ maths ]
css: "../../css/permutations.css"
---

::: {.callout-note icon=false}
## Définition

Une **transposition** est une [permutation](permutation.md) qui n'échange que $2$ éléments.

Une transposition est donc un [2-cycle](p cycle.md) 

Formellement, une [permutation](permutation.md) $\sigma \in\mathfrak{S}_{n}$ est une transposition si et seulement si :

 - il existe $2$ éléments distincts $a$ et $b$ tels que $\sigma(a)=b$ et $\sigma(b)=a$
 - $\forall i \notin \{ a; b \}, \quad \sigma(i)=i$ (tous les autres éléments sont invariants par $\sigma$)

:::


::: {.callout-tip icon=false collapse=true}
## Exemples

$\sigma = \begin{pmatrix}1&2&3\\1&3&2\end{pmatrix}$ est une transposition

$\sigma=\begin{pmatrix}1&2&3&4\\3&2&1&4\end{pmatrix}$ est une transposition

$\sigma=\begin{pmatrix}1&2&3&4&5\\2&4&1&5&3\end{pmatrix}$ n'est **pas une transposition**


Voici la visualisation d'une transposition :


```{=html}
<div class="container">
    <div class="permutation">
        <div class="parenthesis">(</div>
        <div class="lines">
            <div class="text">
                <div>1</div>
                <div>2</div>
                <div>3</div>
                <div>4</div>
                <div>5</div>
            </div>
            <div class="text">
                <div>1</div>
                <div class="perm shift-of-3">2</div>
                <div>3</div>
                <div>4</div>
                <div class="perm shift-of-3 reverse">5</div>
            </div>
        </div>
        <div class="parenthesis">)</div>
    </div>
</div>
```
:::




