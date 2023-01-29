---
title: "formulaire d'analyse"
date: 2023-01-03
categories: [ maths, index ]
image: "_images/tableau_a_craie.png"
toc: true
number-sections: true
---


Voici une liste des formules importantes en analyse 

## Identités remarquables


$(a + b)^{2} = a^{2} + 2ab + b^{2}$

$(a - b)^{2} = a^{2} - 2ab + b^{2}$

$(a + b)(a - b) = a^{2} - b^{2}$


$(a + b)^{3} = a^{3} + 3a^{2}b + 3ab^{2} + b^{3}$

$(a - b)^{3} = a^{3} - 3a^{2}b + 3ab^{2} - b^{3}$

$a^{3} - b^{3} = (a - b)\left( a^{2} + ab + b^{2} \right)$

$a^{3} + b^{3} = (a + b)\left( a^{2} - ab + b^{2} \right)$


# Suites arithmétiques et géométriques

## Suites arithmétiques

Termes de la suite ($r$ désigne la raison):

$u_{n+1} - u_{n} = r$

$u_{n} = u_{0} + nr$

$u_{n} = u_{p} + (n-p)r$

Somme des termes :

$\displaystyle S_{n} = \sum_{k=0}^{n}u_{k} = \dfrac{(n+1)(u_{0}+u_{n})}{2}$


Cas général avec $n_{1} \leq n_{2}$ :


$\displaystyle S' = \sum_{k = n_{1}}^{n_{2}}u_{k} = \frac{(nombre\ de\ termes)(premier\ terme + dernier\ terme)}{2}$


Cas particulier :

$\displaystyle 1 + 2 + 3\ \cdots + (n - 1) + n = \frac{n(n + 1)}{2}$



## Suites géométriques


On suppose que la suite est non nulle. Termes de la suite (\(q\) désigne la raison) :

$\dfrac{u_{n+1}}{u_{n}} = q$

$u_{n} = u_{0} \times q^{n}$

$u_{n} = u_{p}\times q^{n-p}$

Somme des termes :

$S_{n} = \sum\limits_{k=0}^{n}u_{k}$

 - Si $q \neq 1$ : $S_{n} = u_{0}\times \frac{1-q^{n+1}}{1-q}$
 - Si $q=1$ : $S_{n}=u_{0}(n+1)$

Cas général avec $n_{1} \leq n_{2}$ :
$S'_{n} = \sum\limits_{k=0}^{n}u_{k}$

 - Si $q \neq 1$ : $\displaystyle S'_{n} = (\text{premier terme}) \times \frac{1- \left( q^{\text{nombre de termes}} \right)}{1-q}$
 - Si $q \neq 1$ : $\displaystyle S'_{n} = (\text{premier terme}) \times \frac{1- q ^{(\text{nombre de termes})}}{1-q} = u_0 \times \frac{1-q^{n+1}}{1-q}$
 - Si $q = 1$ : $S'_{n} = (\text{nombre de termes}) \times (\text{premier terme})$


# Formules de dérivation

## Formules générales

Dans ce qui suit, $u$ et $v$ désignent deus fonctions d'une variable réelle $x$, et $k$ une constante réelle.

$(u+v)' = u' + v'$

$(ku)' = ku'$

$(uv)' = u'v + uv'$

$\left( \dfrac{u}{v} \right)' = \dfrac{u'v - uv'}{v^{2}}$

$(v\circ u)' = u' \times (v'\circ u)$

$\displaystyle(u^{-1})' = \dfrac{1}{u' \circ u^{-1}}$

## Fonctions usuelles

### fonctions non composées

| Fonction $f$                            | $\mathscr{D}_{f}$                                                                             | Fonction dérivée $f'$              | $\mathscr{D}_{f'}$                                                                           |
|----:| --------------------------------------------------------------------------------------------- | ---------------------------------- | -------------------------------------------------------------------------------------------- |
| $k$                                     | $\mathbb{R}$                                                                                  | 0                                  | $\mathbb{R}$                                                                                 |
| $x$                                     | $\mathbb{R}$                                                                                  | $1$                                | $\mathbb{R}$                                                                                 |
| $\dfrac{1}{x}$                          | $\mathbb{R}^{*}$                                                                              | $-\dfrac{1}{x^{2}}$                | $\mathbb{R}^{*}$                                                                             |
| $\sqrt{ x }$                            | $\mathbb{R}^{+}$                                                                              | $\frac{1}{2\sqrt{ x }}$            | $\mathbb{R}^{+*}$                                                                            |
| $x^{n}$ avec $n \in\mathbb{Z}$ | $\mathbb{R}$ | $nx^{n-1}$ | $\mathbb{R} \text{ si } n \geq 0, \quad \mathbb{R}^{*} \text{ si } n < 0$ |
| $x^{\alpha}$ avec $\alpha \in\mathbb{R}$ | $\mathbb{R}^{+} \text{ si } \alpha \geq 0, \quad \mathbb{R}^{+*} \text{ si } \alpha<0$ | $\alpha x^{\alpha-1}$ | $\mathbb{R} \text{ si } n \geq 0, \quad \mathbb{R}^{*} \text{ si } \alpha < 1$
| $\ln \mid x \mid$                       | $\mathbb{R}^{+*}$                                                                             | $\dfrac{1}{x}$                     | $\mathbb{R}^{+*}$                                                                            |
| $\exp x$                                | $\mathbb{R}$                                                                                  | $\exp x$                           | $\mathbb{R}$                                                                                 |
| $\sin x$                                | $\mathbb{R}$                                                                                  | $\cos x$                           | $\mathbb{R}$                                                                                 |
| $\cos x$                                | $\mathbb{R}$                                                                                  | $-\sin x$                          | $\mathbb{R}$                                                                                 |
| $\tan x$                                | $\mathbb{R} \setminus \left\lbrace \dfrac{\pi}{2} + k\pi \right\rbrace$                                 | $1+\tan^2 x = \dfrac{1}{\cos^2 x}$ | $\mathbb{R} \setminus \left\lbrace \dfrac{\pi}{2} + k\pi \right\rbrace$                                |
| $\mathrm{sh} x$                                 | $\mathbb{R}$                                                                                  | $\mathrm{ch} x$                            | $\mathbb{R}$                                                                                 |
| $\mathrm{ch} x$                                 | $\mathbb{R}$                                                                                  | $\mathrm{sh} x$                            | $\mathbb{R}$                                                                                 |
| $\mathrm{th} x$                                 | $\mathbb{R}$                                                                                  | $1-\mathrm{th}^2 x = \dfrac{1}{\mathrm{ch}^2 x}$   | $\mathbb{R}$                                                                                 |


Les dérivées des fonctions réciproques des fonctions trigonométriques et hyperboliques figurent dans la section "trigonométrie réciproque

### Fonctions composées

| forme de la fonction | forme de la dérivée                             |
| -------------------- | ----------------------------------------------- |
| $\dfrac{1}{u}$       | $-\dfrac{u'}{u^2}$                              |
| $\sqrt{u}$           | $\dfrac{u'}{2 \sqrt{u}}$                        |
| $u^{\alpha}$         | $\alpha u' u^{\alpha - 1}$                      |
| $\ln\mid u \mid $    | $\dfrac{u'}{u}$                                 |
| $\exp u$             | $u' \times \exp u$                              |
| $\sin u$             | $u'\times \cos u$                               |
| $\cos u$             | $-u' \times \sin u$                             |
| $\tan u$             | $u' \times (1+\tan^2 u) = \dfrac{u'}{\cos^2 u}$ |
| $\mathrm{sh} u$              | $u' \times \mathrm{ch} u$                               |
| $\mathrm{ch} u$              | $u' \times \mathrm{sh} u$                               |
| $\mathrm{th} u$              | $u' \times (1-\mathrm{th}^2 u) = \dfrac{u'}{\mathrm{ch}^2 u}$   |


# Fonctions trigonométriques et hyperboliques


##  Fonctions trigonométriques

$\cos^2 x + \sin^2 x = 1$

$\cos(a+b) = \cos a \cos b - \sin a \sin b$

$\cos(a-b) = \cos a \cos b + \sin a \sin b$

$\sin(a+b) = \sin a\cos b + \sin b \cos a$

$\sin(a-b) = \sin a \cos b - \sin b \cos a$

$\tan(a+b) = \dfrac{\tan a + \tan b}{1-\tan a \tan b}$

$\tan(a-b) = \dfrac{\tan a - \tan b}{1+\tan a \tan b}$

$\cos a \cos b = \dfrac{1}{2} \big( \cos(a+b)+\cos(a-b) \big)$

$\sin a\sin b = \dfrac{1}{2} \big( \cos(a-b) - \cos(a+b) \big)$

$\sin a \cos b = \dfrac12 \big( \sin(a+b) + \sin(a-b) \big)$

$\cos a + \cos b = 2\cos \dfrac{(a+b)}{2}\cos\dfrac{(a-b)}{2}$

$\cos a - \cos b = -2\sin\dfrac{a+b}{2}\sin\dfrac{a-b}{2}$

$\sin a + \sin b = 2\sin\dfrac{a+b}{2}\cos\dfrac{a-b}{2}$

$\sin a - \sin b = 2\sin\dfrac{a-b}{2} \cos\dfrac{a+b}{2}$

$\cos(2x) =\cos ^{2}x-\sin ^{2}x \quad= 2\cos ^{2}x-1 \quad= 1-2\sin ^{2}x \quad= \frac{1-\tan ^{2}x}{1+\tan ^{2}x}$


$\cos^2 x = \dfrac{1+\cos(2x)}{2}$

$\sin^2 x = \dfrac{1-\cos(2x)}{2}$

$\tan^2 x = \dfrac{1-\cos(2x)}{1+\cos(2x)}$

$\sin(2x) = 2\sin x\cos x \quad= 1+\tan ^{2}x$

$\tan(2x) = \dfrac{2\tan x}{1 - \tan^2 x}$


## Fonctions hyperboliques

$\mathrm{ch}^2 x - \mathrm{sh}^2 x = 1$

$\mathrm{ch}(a+b) = \mathrm{ch} (a) \;\mathrm{ch} (a) + \mathrm{sh} a \mathrm{sh} b$

$\mathrm{ch}(a-b) = \mathrm{ch} (a)\; \mathrm{ch} (b) - \mathrm{sh} a \mathrm{sh} b$

$\mathrm{sh}(a+b) = \mathrm{sh} (a)\; \mathrm{ch} (b) + \mathrm{sh} (b)\; \mathrm{ch} (a)$

$\mathrm{sh}(a-b) = \mathrm{sh} (a); \mathrm{ch} (b) - \mathrm{sh} (b) \mathrm{ch} (a)$

$\mathrm{th}(a+b) = \dfrac{\mathrm{th} a + \mathrm{th} b}{1 +  \mathrm{th} (a) \mathrm{th} (b)}$

$\mathrm{th}(a-b) = \dfrac{\mathrm{th} a - \mathrm{th} b}{1 - \mathrm{th} (a) \mathrm{th} (b)}$

$\mathrm{ch} (a) \;\mathrm{ch} (b) = \dfrac12 \big( \mathrm{ch}(a+b) + \mathrm{ch}(a-b) \big)$

$\mathrm{sh} (a)\; \mathrm{sh} (b) = \dfrac12 \big( \mathrm{ch}(a+b) - \mathrm{ch}(a-b) \big)$

$\mathrm{sh} (a)\; \mathrm{ch} (b) = \dfrac12 \big( \mathrm{sh}(a+b) + \mathrm{sh}(a-b) \big)$

$\mathrm{ch} (a) + \mathrm{ch} (b) = 2\mathrm{ch} \dfrac{a+b}{2} \mathrm{ch} \dfrac{a-b}{2}$

$\mathrm{ch} (a) - \mathrm{ch} (a) = 2\mathrm{sh} \dfrac{a+b}{2}\mathrm{sh}\dfrac{a-b}{2}$

$\mathrm{sh} (a) + \mathrm{sh} (b) = 2\mathrm{sh} \dfrac{a+b}{2}\mathrm{ch}\dfrac{a-b}{2}$

$\mathrm{sh} (a) - \mathrm{sh} (b) = 2\mathrm{sh}\dfrac{a-b}{2} \mathrm{ch}\dfrac{a+b}{2}$

$\mathrm{ch}(2x) = \mathrm{ch} ^{2}x + \mathrm{sh} ^{2}x \quad= 2\mathrm{ch} ^{2}x - 1 \quad= 1+2\mathrm{sh} ^{2}x \quad=\frac{1+\mathrm{th} ^{2}x}{1-\mathrm{th} ^{2}x}$

$\mathrm{ch}^2 x = \dfrac{1+\mathrm{ch}(2x)}{2}$

$\mathrm{sh}^2 x = \dfrac{\mathrm{ch}(2x) - 1}{2}$

$\mathrm{th}^2 x = \dfrac{\mathrm{ch}(2x) - 1}{\mathrm{ch}(2x) + 1}$

$\mathrm{sh}(2x) = 2\mathrm{sh}(x) \mathrm{ch}(x) \quad= \frac{2\mathrm{th}(x)}{1-\mathrm{th}^{2}(x)}$

$\mathrm{th}(2x) = \dfrac{2\mathrm{th} x}{1+\mathrm{th}^2 x}$



## Points sur le cercle trigonométrique

|        | $-x$      | $\frac{\pi}{2}+x$   | $\frac{\pi}{2}-x$  | $\pi+x$   | $\pi-x$   | $0$ | $\frac{\pi}{6}$        | $\frac{\pi}{4}$        | $\frac{\pi}{3}$        | $\frac{\pi}{2}$ |
| ------ | --------- | ------------------- | ------------------ | --------- | --------- | --- | ---------------------- | ---------------------- | ---------------------- | --------------- |
| $\sin$ | $-\sin x$ | $\cos x$            | $\cos x$           | $-\sin x$ | $\sin x$  | $0$ | $\frac{1}{2}$          | $\frac{\sqrt{ 2 }}{2}$ | $\frac{\sqrt{ 3 }}{2}$ | 1               |
| $\cos$ | $\cos x$  | $-\sin x$           | $\sin x$           | $-\cos x$ | $-\cos x$ | $1$ | $\frac{\sqrt{ 3 }}{2}$ | $\frac{\sqrt{ 2 }}{2}$ | $\frac{1}{2}$          | 0               |
| $\tan$ | $-\tan x$ | $-\frac{1}{\tan x}$ | $\frac{1}{\tan x}$ | $\tan x$  | $-\tan x$ | $0$ | $\frac{\sqrt{ 3 }}{2}$ | $1$                    | $\sqrt{ 3 }$           |                 |



## Trigonométrie réciproque

$\arcsin x + \arccos x = \dfrac{\pi}{2}$

$\arctan x + \arctan \dfrac{1}{x} = \text{sg}(x) \times \dfrac{\pi}{2}$ avec $\mathrm{sg}(x) = 1 \text{ si } x>0$ et $\mathrm{sg}(x) = -1 \text{ si } x < 0$

$(\arcsin x)' = \dfrac{1}{\sqrt{1-x^2}}$

$(\arccos x)' = -\dfrac{1}{\sqrt{1-x^2}}$

$(\arctan x)' = \dfrac{1}{1+x^2}$

$(\arcsin u)' = \dfrac{u'}{\sqrt{1-u^2}}$

$(\arccos u)' = -\dfrac{u'}{\sqrt{1-u^2}}$

$(\arctan u)' = \dfrac{u'}{1+u^2}$


\columnbreak
## Trigonométrie hyperbolique réciproque

$\arg\mathrm{sh} x = \ln \left( x + \sqrt{ 1+x^2 } \right)$

$\arg\mathrm{ch} x = \ln \left( x + \sqrt{ 1 - x^2 } \right)$

$\arg\mathrm{th} x = \dfrac12 \ln \left( \dfrac{1+x}{1-x} \right)$

$(\arg\mathrm{sh} x)' = \dfrac{1}{\sqrt{ x^2 + 1 }}$

$(\arg\mathrm{ch} x)' = \dfrac{1}{\sqrt{x^2 - 1}}$

$(\arg\mathrm{th} x)' = \dfrac{1}{1-x^2}$

$(\arg\mathrm{sh} u)' = \dfrac{u'}{\sqrt{ u^2 + 1 }}$

$(\arg\mathrm{ch} u)' = \dfrac{u'}{\sqrt{ u^2 - 1}}$

$(\arg\mathrm{th} u)' = \dfrac{u'}{1 - u^2}$



# Limites usuelles

## Comportement à l'infini

$\displaystyle\lim_{x\to+\infty} \ln x = +\infty$

$\displaystyle\lim_{x\to+\infty}\exp x = +\infty$

$\displaystyle\lim_{x\to-\infty}\exp x = 0$



Si $\alpha > 0$, $\displaystyle\lim_{x\to+\infty}x^{\alpha} = +\infty$

Si $\alpha < 0$, $\displaystyle\lim_{x\to+\infty}x^{\alpha} = 0$

Si $\alpha > 0$, $\displaystyle\lim_{x\to+\infty}\dfrac{\exp x}{x^\alpha} = \lim_{x\to+\infty}\dfrac{e^x}{x^\alpha} = +\infty$

Si $\alpha > 0$, $\displaystyle\lim_{x\to+\infty}x^\alpha\times\exp(-x) = \lim_{x\to+\infty}x^\alpha e^{-x} = 0$



## Comportement à l'origine


$\displaystyle\lim_{x \rightarrow 0} \ln x = + \infty$

Si $\alpha > 0$, $\displaystyle\lim_{x \rightarrow 0^+} x^\alpha = +\infty$

Si $\alpha < 0$, $\displaystyle\lim_{x \rightarrow 0^+} x^\alpha = +\infty$

Si $\alpha > 0$, $\displaystyle\lim_{x \rightarrow 0^+} \left( x^\alpha \ln x \right) = 0$ propriété de croissance comparée

$\displaystyle \lim_{x \rightarrow 0} \dfrac{\ln (1+x)}{x} = 1$

$\displaystyle \lim_{x \to 0} \dfrac{e^x - 1}{x} = 1$

$\displaystyle \lim_{x \rightarrow 0} \dfrac{\sin x}x = 1$




# Formules d'intégration


## Intégration par parties

$\displaystyle \int_{a}^{b} f(x)g'(x) \, dx = \big[ f(x)g(x) \big]_{a}^{b} - \int_{a}^{b}  f'(x)g(x) \, dx$


## Primitives usuelles


Si $\alpha \neq -1$, $\displaystyle \int x^\alpha \mathrm{d} x = \dfrac{1}{\alpha + 1}x^{\alpha +1} + \text{cte}$

$\displaystyle\int \dfrac{1}x \mathrm{d} x = \ln |x|+\text{cte}$

$\displaystyle\int \dfrac{1}{x+\alpha }\mathrm{d} x = \ln |x+\alpha |+\text{cte}$

$\displaystyle\int e^x \mathrm{d} x = e^x + \text{cte}$

Si $\alpha > 0$ et $\alpha \neq 1$, $\displaystyle\int \alpha^x \mathrm{d} x= \dfrac{1}{\ln \alpha }\times \alpha^x + \text{cte}$

$\displaystyle\int \cos x \mathrm{d} x = \sin x + \text{cte}$

$\displaystyle\int \sin x \mathrm{d} x = -\cos x + \text{cte}$

Si $\alpha \neq 0$, $\displaystyle\int \cos \alpha x \mathrm{d} x = \dfrac{1}{\alpha} \sin \alpha x + \text{cte}$

Si $\alpha \neq 0$, $\displaystyle\int \sin \alpha x \mathrm{d} x = \dfrac{1}{\alpha} \cos \alpha x + \text{cte}$


$\displaystyle \int \dfrac{1}{\cos ^2 x} \mathrm{d} x = \tan x + \text{cte}$

$\displaystyle\int 1 + \tan ^2 x \mathrm{d} x = \tan x + \text{cte}$

$\displaystyle\int \dfrac{1}{\sin ^2 x} \mathrm{d} x = -\mathrm{cotan} x + \text{cte} \quad= -\dfrac{1}{\tan x} + \text{cte}$

$\displaystyle\int \dfrac{1}{1+x^2} \mathrm{d} x = \arctan x + \text{cte}$

$\displaystyle\int \mathrm{ch} x \mathrm{d} x = \mathrm{sh} x + \text{cte}$

$\displaystyle\int \mathrm{sh} x \mathrm{d} x = \mathrm{ch} x + \text{cte}$

$\displaystyle\int \dfrac{1}{\mathrm{ch}^2 x} \mathrm{d} x = \mathrm{th} x + \text{cte}$

$\displaystyle\int \dfrac{1}{\mathrm{sh}^2 x} \mathrm{d} x = \dfrac{1}{\mathrm{th} x} + \text{cte}$



## Primitives de fonctions composées

$\displaystyle\int \frac{u'(x)}{u(x)} \, dx = \ln(u) + \text{cte}$


