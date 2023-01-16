---
title: "vim tips - leader"
description: "présentation du raccourci &#60;leader&#62; dans vim"
date: 2023-01-03
categories: [ vim, tips  ]
image: "images/vim.excalidraw.svg"
toc: true
---

Dans Vim, on peut changer les raccourcis pour absolument toutes les touches.

Justement, un des raccourcis que l'on peut changer, c'est `<leader>`.

Quand il s'agit de `<space>` (touche espace), `<tab>`, `<cr>` (carriage return, pour la touche entrée), on arrive à deviner.
Mais pour `<leader>`, c'est plus difficile.

En fait, `<leader>` peut être n'importe quel raccourci que vous choisissez !
Quand vous créez un raccourci, `<leader>` sera remplacé par la valeur dans la variable `g:mapleader`.

Cela peut être intéressant :

 - on peut avoir une touche que l'on utilise souvent dans nos raccourcis
 - on peut changer cette touche facilement
     - si on change de clavier
     - si on change de layout (`azerty`, `qwerty`...)
     - si on veut changer sa position (changer la touche assignée à `<leader>`)

# Comment utiliser `<leader>`

Par défaut, `<leader>` est assigné à la touche `\` (anti-slash). C'est parce que cette touche est facilement accessible sur un clavier `qwerty`.

## Changer la touche assignée

Comme je l'ai dit plus haut, `<leader>` est défini par la variable `g:mapleader`

Par exemple, si on souhaite utiliser la touche `,` pour leader :

```vimscript
let g:mapleader = ","
```

Si on souhaite utiliser une touche qui est représentée entre `<...>`, comme la touche espace (`<space>`), il ne faut pas oublier le `\` avant le nom de la touche :

```vim
let g:mapleader = "\<space>"
```

Si vous oubliez le `\`, il faudra taper toutes les touches : `<`, `s`, `p`, `a`, `c`, `e`, `>` pour déclancher `<leader>`


## Cas d'utilisation

Un des usages principaux de `<leader>` est comme préfixe (d'où le nom, leader, en anglais).

Par préfixe, je veux dire une touche qui est au début de plein de raccourcis. C'est utile car Vim assigne déjà beaucoup de raccourcis, et donc ne laisse pas beaucoup de place pour que l'utilisateur définisse les siens.
C'est pour cette raison que `<leader>` est utile : vous pouvez faire commencer plein de vos raccourcis par leader. Par exemple, j'ai défini les raccourcis `<leader>j`, `<leader>k`, `<leader>m`, `<leader>ul`...


### Exemples d'utilisation

Voici quelques exemples d'utilisation :

 - `<leader>m` pour `:make<cr>`, si vous utilisez des [makefiles](https://shiftcode.fr/comprendre-les-makefiles/ "https://shiftcode.fr/comprendre-les-makefiles/")
 - `<leader>k` pour sauvegarder (c'est bizarre mais c'est ce que j'utilise)
 - `<leader>w` ou bien `<leader>q` pour `<c-w>`, afin d'éviter la touche contrôle quand on manipule les fenêtres
 - `<leader>t` pour `:tabnew<cr>` (créer un nouvel onglet)
 - `<leader>!` pour `:term ++curwin` (ouvrir un terminal dans la fenêtre actuelle)

<br/> <br/> <br/>
<br/> <br/> <br/>

---

Mon .vimrc est disponible ici : [github.com/OsKaR31415/config](https://github.com/OsKaR31415/config/blob/master/.vimrc) avec le reste de ma configuration.


