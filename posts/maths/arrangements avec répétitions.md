---
title: "arrangements avec répétitions"
description: "nombre de sacs à k éléments inclus dans un ensemble à n éléments"
date: 2023-01-06
categories: [ maths ]
---

::: {.callout-note icon=false}
## Définition

$\mathcal{A}_{n}^{k} = n^{k}$

Les **arrangements avec répétitions** dans $n$ de $k$ sont **le nombre de $k$-uplets d'éléments d'un ensemble à $n$ éléments**.

C'est donc le nombre de possibilités de mettre $n$ types d'objets dans $k$ emplacements.
:::


# Interprétation

::: {.callout-tip collapse=true}
## Exemples

Voici quelques questions dont la réponse passe par un arrangement avec répétitions :

 - le langage _toki pona_ possède 120 mots. Combien peut-on faire de phrases de 5 mots en _toki pona_ ?
     - $\mathcal{A}_{120}^{5} = 120^{5} = 24\,883\,200\,000$, soit ving-quatre milliards huit-cent quatre-vingt-trois millions deux-cent mille phrases différents
 - Combien de codes PIN à 4 chiffres peut-on faire ?
     - Arrangements avec répétitions de 4 chiffres parmi les 10 existants, soit $\mathcal{A}_{10}^{4} = 10^{4} = 10\,000$ codes possibles
         - Note : cela veut dire que, avec un ordinateur actuel, craquer un code à 4 chiffres est instantané (donc si vous vous faîtes voler un ordinateur avec un tel code, il ne sera pas protégé)
:::

# Formule

On peut mettre l'un des $n$ objets dans les $k$ positions :

 - $n$ possibilités dans la $1^{ère}$ position
 - $n$ possibilités dans la $2^{ème}$
 - $\vdots$
 - $n$ possibilités dans la $k^{ème}$ position

Donc, en tout, $\underbrace{n\times n\times \cdots \times n}_{k \text{ répétitions}} = n^{k}$

On a donc bien : $\mathcal{A}_{n}^{k} = n^{k}$



