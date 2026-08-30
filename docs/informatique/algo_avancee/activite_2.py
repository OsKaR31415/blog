class Node:
    def __init__(self, valeur, suivant: 'Node' =None):
        self.valeur = valeur
        self.suivant = suivant

class Liste:
    def __init__(self, head: Node):
        self.head = head

    def __str__(self) -> str:
        return "<" + ",".join(map(lambda e: str(Liste(e) if isinstance(e, Node) else e),
                                  self.to_list())) + ">"

    def to_list(self) -> list:
        if self.head is None:
            return []
        return [self.head.valeur] + self.cdr().to_list()

    def __len__(self) -> int:
        """Longueur de la liste.
        """
        if self.head is None:
            return 0
        return 1 + len(self.head.suivant)

    def append(self, valeur) -> None:
        """Ajouter une valeur à la fin de la liste.
        """
        # cas de base :
        # on doit s'arrêter dès que la liste est terminer
        if self.head.suivant is None:
            # on créé un nouveau Node
            self.head.suivant = Node(valeur)
        # récursion pour atteindre la fin de la liste
        self.cdr().append(valeur)

    def car(self):
        """Récupérer la valeur en tête de liste
        """
        return self.head.value

    def cdr(self) -> 'Liste':
        """Récupérer la liste sans son premier élément.
        """
        if self.head is None:
            return None
        return Liste(self.head.suivant)

    def last(self):
        """Récupérer le dernier élément de la liste.
        """
        if self.head.suivant is None:
            return self.last(Liste(self.head.suivant))
        return self.head.valeur


##################################################

# 1. Quelle est l'instruction pour créer une liste vide nommée `p` ?

p = None

# 2. Quelle est l’instruction pour créer une liste d’entiers p ne contenant
# qu’un seul élément (par exemple la valeur 1) ?

p = Node(1)

# 3. Quelles sont les instructions pour créer une liste d’entiers contenant
# exactement les valeurs 1, 2 et 3 dans cet ordre ?

p = Node(1, Node(2, Node(3)))

# 4. On considère désormais la liste `L = (1(23)(45(678)))`. Comment récupérer
# les valeurs ou listes suivantes : 1, (3), 3, (5(678)) et enfin 6 ?

L = Node(1, Node(Node(2, Node(3)), Node(Node(4, Node(5, Node(Node(6, Node(7, Node(8)))))))))

print(L.valeur)
print(Liste(L.suivant.valeur.suivant))
print(L.suivant.valeur.suivant.valeur)
print(Liste(L.suivant.suivant.valeur.suivant))

################################################################################

# 1. une fonction init(L) de création d’un Node à partir d’une liste native Python

def init(L: list) -> Node:
    if L == []:
        return None
    return Node(L[0], init(L[1:]))

print(Liste(init([3, 1, 4, 1, 5, 9])))


# on peut modifier la fonction pour accepter aussi des listes "nichées"
# (_nested_), c'est-à-dire qui contiennent des sous-liste, des
# sous-sous-listes, etc.

def init_nested(L: list) -> Node:
    if L == []:
        return None
    if isinstance(L[0], (list, tuple)):
        value = init_nested(L[0])
    else:
        value = L[0]
    return Node(value, init_nested(L[1:]))

print(Liste(init_nested([1, 2, 1, [3, 4, 5], 6, [73, 74, 75, [76, 77, 78]]])))


# 2. une fonction print(L) qui affiche les éléments d’une liste entre
# parenthèse et séparés par une virgule

def Node_to_list(N: Node) -> list:
    """Convertir une liste chaînée en liste python.
    Args:
        N (Node): Une liste chaînée.
    Returns:
        list: La liste convertie en objet `list`.
    """
    if N is None:
        return []
    return [N.valeur] + Node_to_list(N.suivant)

def print_Node(L: Node) -> None:
    """Afficher une liste chaînée"""
    res = "("
    for elt in Node_to_list(L):
        res += str(elt) + ','
    res = res[:-1]  # on retire la dernière virgule
    res += ")"  # on ferme la parenthèse
    print(res)

print_Node(None)
print_Node(L)


###########################
# une version plus courte #
###########################
def print_Node(L: Node):
    print('(' + ','.join(map(str, Node_to_list(L))) + ')')

print_Node(None)
print_Node(L)


###########################################
# version qui supporte les listes nichées #
###########################################
def print_Node(N: Node) -> str:
    def aux(N: Node) -> str:
        if N is None:
            return ''
        valeur = f'({aux(N.valeur)})' if isinstance(N.valeur, Node) else str(N.valeur)
        if N.suivant is None:
            return valeur
        return valeur + "," + aux(N.suivant)

    if N is None:
        print('()')
    elif N.suivant is None:
        print(f'({N.valeur})')
    else:
        print('(' + aux(N) + ')')

print_Node(init_nested([1, 2, 1, [3, 4, 5], 6, [73, 74, 75, [76, 77, 78]]]))




# 3. une fonction append(L, elem) qui ajoute l’élément elem à la fin de la liste


def append(L: Node, elem):
    if L is None:
        L = Node(elem)
    while L.suivant is not None:
        L = L.suivant
    L.suivant = Node(elem)

L = init([1, 2, 3])
print_Node(L)
append(L, 4)
print_Node(L)



def append_rec(L: Node, elem):
    if L is None:
        L = Node(elem)
    if L.suivant is None:
        L.suicant = Node(elem)
    append_rec(L.suicant, elem)

print_Node(L)
append(L, 5)
print_Node(L)






# 4. une fonction get(L, index) qui retourne l’élément d’indice index de la liste s’il existe et None sinon

def get(L: Node, index: int) -> Node:
    if L is None:
        return None
    if index == 0:
        return L.valeur
    return get(L.suivant, index - 1)

L = init([3, 1, 4, 1, 5, 9])
print(get(L, 0))
print(get(L, 4))
print(get(L, 100))
print(get(None, 2))



def get_iter(L: Node, index: int):
    if L is None:
        return None
    p = L
    while p is not None:
        if index == 0:
            return p.valeur
        p = p.suivant
        index -= 1
    return None

L = init([3, 1, 4, 1, 5, 9])
print(get_iter(L, 0))
print(get_iter(L, 4))
print(get_iter(L, 100))
print(get_iter(None, 2))




# 5. une fonction `set(L, index, value)` qui modifie la valeur de l’élément
# d’indice `index` dans la liste `L`

# NOTE: `set` est un mot clef de python, pour l'objet ensemble. Il n'est pas réservé (il es possible de le re-définir), mais il est conseillé de ne pas le faire.

def set_rec(L: Node, index: int, valeur) -> Node:
    """Créer une nouvelle liste chaînée dont la valeur à l'indice `index` est
    remplacée par `valeur`.
    La fonction retourne la nouvelle version de la liste (la modification n'est
    pas faîte en place).
    Args:
        L (Note): La liste chaînée à modifier.
        index (int): L'index à modifier dans la liste `L`. 0 désigne le premier
                     élément (indexation à 0).
        valeur: La nouvelle valeur à mettre à l'index `index`.
    Returns:
        Node: La liste `L` dans laquelle on a remplacé l'élément à l'indice
              `index` par `valeur`.
    Raises:
        IndexError: Si `index` est négatif, ou bien si il est en dehors de la
                    liste (trop grand).
    """
    if L is None:
        raise IndexError(f"Indice en dehors de la liste : {index}")
    if index == 0:
        L.valeur = valeur
    elif index < 0:
        raise ValueError(f"Les indices négatifs ne sont pas acceptés : {index}")
    else:
        set_rec(L.suivant, index - 1, valeur)

L = init([42, 1, 73, 1, 5, 9])
print_Node(L)
set_rec(L, 0, 3)  # 42 -> 3
set_rec(L, 2, 4)  # 73 -> 4
print_Node(L)



################################################################################
# liste des éléments plus grands qu'un élément donné

# 1. écrire la fonction `nbPlusGrands(L, seuil)` qui prend en argument une
# liste d’entiers ainsi qu’un seuil et qui retourne le nombre d’éléments
# contenus dans la liste qui sont strictement supérieurs au seuil passé en
# argument.

def nb_plus_grands(L: Node, seuil) -> int:
    """Calcule le nombre d'éléménts de `L` qui sont supérieurs à seuil.
    Cela suppose que tous les éléments de `L` soient comparables avec `seuil`.
    """
    if L is None: return 0
    if L.valeur > seuil:
        return 1 + nb_plus_grands(L.suivant, seuil)
    return nb_plus_grands(L.suivant, seuil)

phi = init([1, 6, 1, 8, 0, 3, 3, 9, 8, 8, 7])
# éléments > 6 :     ^           ^  ^  ^  ^
print(nb_plus_grands(phi, 6))


# 2.écrire ensuite la fonction `listePlusGrands(L, seuil)` qui retourne la liste des éléments de `L` plus grands que le seuil.
def listePlusGrands(L: Node, seuil) -> Node:
    if L is None: return None
    if L.valeur > seuil:
        return Node(L.valeur,
                    listePlusGrands(L.suivant, seuil))
    return listePlusGrands(L.suivant, seuil)

print_Node(listePlusGrands(phi, 6))


################################################################################
# Liste des carrés

# 1. écrire une fonction `carre(L)` qui prend en argument une liste de nombres et retourne la liste contenant le carré des nombres de la liste initiale. Cette solution devra modifier directement les valeurs de la liste initiale.

def carre(L: Node):
    p = L
    while p is not None:
        # comme le += ajout, le **= met à la puissance
        # donc `x **= 2` est comme `x = x ** 2`
        p.valeur **= 2
        p = p.suivant


L = init([1, 2, 3, 10, 99])
carre(L)
print_Node(L)

def carre_rec(L: Node):
    if L is None: return
    L.valeur **= 2
    carre_rec(L.suivant)

L = init([1, 2, 3, 10, 99])
carre_rec(L)
print_Node(L)


# 2. écrire une fonction `carre_fin(L)` qui construit une nouvelle liste résultat à partir de la liste initiale. Proposer une solution efficace.



def carre_fin_rec(L: Node) -> Node:
    if L is None: return None
    return Node(L.valeur ** 2,
                carre_fin_rec(L.suivant))

L = init([1, 2, 3, 5, 8, 13, 21])
print_Node(carre_fin_rec(L))
print_Node(L)  # L n'est pas modifiée


# NOTE: Version itérative non efficace :
# cette version n'est pas efficace, car il faut ajouter les valeurs à la fin de
# la liste result (avec un append). Comme append est en O(n), et comme on le
# répète pour tous les éléments de la liste, cette algorithme est en O(n^2) (où
# n est le nombre d'éléments de `L`).

# calcul plus formel de la complexité
# On sait que append est en O(x) où $x$ est la longueur de la liste que l'on
# doit allonger. Dans carre_fin_iter, on appelle append d'abord avec une liste
# vide ($x=0$), puis un singleton ($x=1$), puis avec $x=2$ etc...
# Si $n$ est la longueur de `L`, le nombre d'opérations à faire est
# $1+2+3+...+n$, soit $(n(n+1))/2$ opérations.
# $(n(n+1))/2 = (n^2 + n)/2$ et $(n^2+n)/2 = O(n^2)$. Donc, la complexité de cette fonction est $O(n^2)$.

def carre_fin_iter(L: Node) -> Node:
    result = None
    while p is not None:
        append(result, p.valeur ** 2)
        p = p.suivant
    return result

L = init([1, 2, 3, 5, 8, 13, 21])
print_Node(carre_fin_rec(L))
print_Node(L)  # L n'est pas modifiée



################################################################################
# INSERTION D’UN ÉLÉMENT EN MILIEU DE LISTE

# 1. écrire une fonction itérative `insertion(liste, index, elem)` qui prend en
# argument une liste, une valeur `elem` ainsi qu’un indice et qui insère
# l’élément à l’indice désiré. On considèrera que le premier élément est à
# l’indice 0
def insertion(liste: Node, index: int, elem):
    if liste is None:
        liste = Node(elem)

L = init([1, 2, 3, 5, 8, 13, 21])
print_node







