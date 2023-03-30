---
title: "Le langage APL"
date: 2023-03-23
categories: [ informatique ]
image: "_images/APL_logo.svg.png"
---


APL est mon langage de programmation préféré, parce qu'il est assez mathématique, très agréable à utiliser, et qu'il change vraiment votre façon d'approcher les problèmes (comme [Alan Perlis](https://en.wikipedia.org/wiki/Alan_Perlis) l'a dit : ["A language that doesn’t affect the way you think about programming, is not worth knowing."](https://cpsc.yale.edu/epigrams-programming)).
Ce langage à apporté beaucoup de concepts en programmation qui sont très intéressants.
Notamment, son créateur, Kenneth Iverson, à obtenu le prix Turing en 1979, pour ses travaux sur la notation mathématique, qui ont mené a la création du langage APL, pour l'utilisation éducative d'APL, et pour sa recherche sur la théorie et la pratique des langages.

APL signifie "A Programming Language", et il à été créé en 1962 (ou un peu plus tard selon comment on compte), c'est-à-dire avant le C, et 4 ans après le LISP. Pourtant, même les premières versions intègrent des concepts qui sont toujours novateurs et très intéressants (et, bien sûr, de nombreux dialectes et dérivés ont émergés depuis).

La plupart des langages ou librairies qui manipulent des tableaux généralisés sont très inspirés par APL (on les appelle parfois des "Iverson ghosts"), notamment numpy (on retrouve par exemple `iota` dans beaucoup de langages, pour générer les nombres de `1` à `n`).

Les principaux avantages d'APL sont :

 - le paradigme "[programmation array](https://en.wikipedia.org/wiki/Array_programming)"
    - les opérations sont généralisées le plus possible sur les tableaux (donc faire une addition de tableaux est comme faire une addition de nombres)
 - la programmation avec des [primitives](https://mlochbaum.github.io/BQN/commentary/primitive.html)
    - cela permet de combiner des fonctions de façon très riche, et assez facilement
    - c'est une façon de penser que j'adore : on a beaucoup moins de travail de traduction pour l'ordinateur à faire : pas de boucles, rarement des conditions explicites, et plutôt des opération que l'on applique de différentes manières sur des listes ou tableaux
        - Encore une fois, commme [Alan Perlis](https://en.wikipedia.org/wiki/Alan_Perlis) l'a dit : "A programming language is low level when its programs require attention to the irrelevant."
 - L'utilisation de symboles
    - chaque primitive est représentée par un symbole, ce qui évite d'avoir du code illisible comme quand on utilise numpy
 - Les Dfns
    - APL permet de définir des fonction anonymes assez puissantes
    - elles incluent la possibilité de faire de la récursion anonyme, ce qui est incroyable
 - La concision
    - APL est très concis (par exemple, voici le code pour le jeu de la vie : `life ← {⊃1 ⍵ ∨.∧ 3 4 = +/ +/ ¯1 0 1 ∘.⊖ ¯1 0 1 ⌽¨ ⊂⍵}`)
 - la facilité d'apprentissage
    - comme les primitives sont assez simples à apprendre, et pourtant très riches, on arrive rapidement à faire beaucoup de choses
    - il n'y a qu'un nombre assez petit de primitives, plus quelques variables et fonctions système
 - la notation comme outils pour la pensée
    - Iverson à notamment créé un concept (et écrit un papier pour l'expliciter en APL) : "Notation as a tool of thought" (https://www.eecg.utoronto.ca/~jzhu/csc326/readings/iverson.pdf)
    - Cela inclut notamment des "design patterns for a programming language" :
        - Ease of expressing constructs arising in problems.
            - primitives plutôt que boucles ou concepts bas niveau
            - symboles pour les écrire facilement
        - Suggestivity
            - comme "serendipity", le fait de permettre la découverte de nouvelles choses en les suggérant
            - les symboles et les façons riches de les combiner permettent des manipulations symboliques qui font que l'on découvre de nouvelles façons d'exprimer la même chose assez facilement
            - cela fait que golfer un code APL (le rendre le plus court possible) revient souvent à le simplifier (contrairement à beaucoup d'autres langages où il est très facile de _trop_ golfer, et que tout devienne illisible).
        - Ability to subordinate detail
            - ne surtout pas confondre avec "ability to hide detail" : les fonctions font cela dans tous les langages
            - plutôt que de cacher les détails dans une fonction à un autre endroit, il est plus pratique de mettre les détails à un endroit du programme où on les voit mais où on comprends qu'ils sont subordonnés
            - La syntaxe APL (qui fonctionne de droite à gauche) permet de faire cela très facilement
            - par exemple, le calcul de la moyenne d'une liste est `+/÷≢`. Il est plus pratique d'intégrer ce morceau de code directement dans notre code plus grand, plutôt que de définir une fonction `mean` ou `average`, qu'il faudra de toute façon consulter pour connaître les détails de son fonctionnement
        - Economy
            - les primitives sont représentées par un seul symbole, et les symboles sont même souvent polysémiques selon leur nombre d'arguments
            - par exemple, `⌈` est le plafond quand ses arguments sont seulement à droite, et le maximum de ses deux arguments quand l'un est à droite, l'autre à gauche (ce qui fait que la réduction par `⌈`, notée `⌈/` donne le maximum d'une liste)
        - Amenability to formal proofs
            - aujourd'hui, on je cherche plus nécessairement à avoir des programmes dont on démontre formellement qu'ils fonctionnent (on utilise plutôt une approche empirique, avec des tests), mais le fait qu'APL soit proche de la notation mathématique fait que les démonstrations se font assez bien.


De nombreux dialectes d'APL sont apparus depuis sa création, notamment le J, qui n'utilise que des symboles ASCII (mais parfois deux symboles pour une seule primitive), et qui à apporté les combinateurs (des fonctions qui combine des fonctions de façon assez riches) et les trains (ce qui permet d'écrire la moyenne littéralement comme "somme divisée par longueur" : `+/ ÷ ≢`). Plus récemment, le BQN est apparu, qui est plus fonctionnel, et qui apporte des primitives différentes, ainsi que des symboles parfois un peu mieux choisis.

APL est vraiment un langage très particulier, la quasi totalité des gens qui l'apprennent adorent programmer avec, car il est très agréable à utiliser, mais il faut vraiment sortir de la façon "habituelle" de coder : il faut accepter que les symboles sont plus lisibles que des noms, que faire une longue ligne est plus lisible que de séparer le code en fonctions etc...


::: {.callout-note}
# Introduction au langage APL

J'ai filmé 4 vidéos qui présentent quelques bases du langage APL sur un exemple simple : comment calculer des [triplets pythagoriciens](https://fr.wikipedia.org/wiki/Triplet_pythagoricien).

[Voir a playlist complète](https://www.youtube.com/playlist?list=PL5ZGZlm-yp_xQfzsBtD66HIMW1M97wCsE)

 - [Vidéo 1](https://www.youtube.com/watch?v=6J0Au6AKGWw&list=PL5ZGZlm-yp_xQfzsBtD66HIMW1M97wCsE&index=2)
 - [Vidéo 2](https://www.youtube.com/watch?v=tax604gMJvA&list=PL5ZGZlm-yp_xQfzsBtD66HIMW1M97wCsE&index=3)
 - [Vidéo 3](https://www.youtube.com/watch?v=iS26PGxl_oI&list=PL5ZGZlm-yp_xQfzsBtD66HIMW1M97wCsE&index=4)
 - [Vidéo 4](https://www.youtube.com/watch?v=yTMfEhadmyg&list=PL5ZGZlm-yp_xQfzsBtD66HIMW1M97wCsE&index=5)


:::
