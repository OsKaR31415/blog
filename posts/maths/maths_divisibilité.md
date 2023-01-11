---
title: "Dibisibilité"
date: 2023-01-10
categories: [ maths ]
image: "_images/obele_division.png"
---

::: {.callout-note icon=false}
## Définitions

Soient $a$ et $b$ deux entiers relatifs (dans $\mathbb{Z}$)
$a$ est un **diviseur** de $b$ s'il existe un entier relatif $k$ tel que $\boxed{b = ka}$

On dit alors que :
 - $a\mid b$ soit _"$a$ divise $b$"_
 - $b$ est un multiple de $a$

:::

## Propriétés


::: {.callout-tip}
## avec $0$

 - $0$ ne divise aucun nombre (on ne peut pas diviser par $0$)
 - tous les nombres divisent $0$ (voir la définition, avec $k=0$)
:::

::: {.callout-tip}
## Nombres négatifs

Si $a \mid b$, on sait que :
 - $-a \mid b$
 - $a \mid -b$
 - $-a \mid -b$

En fait, le signe n'est pas important pour la divisibilité (on le voir en reprenant la définition : $k$ peut être positif ou négatif).
:::


::: {.callout-tip}
## Diviseur d'un diviseur

si $a \mid b$ et $b \mid c$, alors on sait que $a \mid c$

##### Exemples

 - $6 \mid 24$, or $3 \mid 6$, donc $3 \mid 24$
 - $4 \mid 12$, or $24$ est multiple de $12$, donc $4 \mid 12$
:::


::: {.callout-tip}
## Propriété des diviseurs

Tout nombre relatif $b$ possède nombre **fini** de diviseurs.

Tous les diviseurs de $b$ sont compris entre $-b$ est $b$

<br/>

C'est logique, puisqu'un nombre plus grand que $b$ (en valeur absolue) ne peut pas diviser $b$.
:::


::: {.callout-tip}
## Combinaison linéaire

Soient $a$, $b$ et $d$ des nombres relatifs, avec $d \mid a$ et $d \mid b$ ($d$ divise $a$ et $b$)

On sait que, quels que soient les entiers relatifs $u$ et $v$ :

$\boxed{d \mid au + bv}$

(on appelle $au + bv$ une "combinaison linéaire" de $a$ et de $b$)


##### Explication

Puisque $d \mid a$, on sait que $d \mid au$ (car $au$ est évidemment un multiple de $a$)

De même, $d \mid b$, donc $d \mid bv$

Alors, puisque $d$ divise $au$ et $bv$, on sait que 

:::


::: {.callout-tip}
## Lien avec la division euclidienne et la congruence

Soient $a$ et $b$ deux entiers relatifs

$a$ divise $b$ si et seulement si le reste de la division euclidienne de $b$ par $a$ est 0.

$a$ divise $b$ si et seulement si $a \equiv 0 [n]$
:::