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



def zip_iter(L1: Node, L2: Node) -> Node:
    p = L1
    q = L2
    res = None
    last = None
    while p is not None and q is not None:
        if res is None:
            res = Node(Node(p.valeur, Node(q.valeur)))
            last = res
        else:
            last.suivant = Node(Node(p.valeur, Node(q.valeur)))
            last = last.suivant
        p = p.suivant
        q = q.suivant
    return res

L1 = Node(3, Node(1, Node(4, Node(1, Node(5, Node(9, Node(2)))))))
L2 = Node(1, Node(6, Node(1, Node(8, Node(0, Node(3, Node(3)))))))
print(Liste(zip_iter(L1, L2)))
print(Liste(L1), Liste(L2))


def zip_rec(L1: Node, L2: Node) -> Node:
    if L1 is None or L2 is None:
        return None
    return Node(Node(L1.valeur, Node(L2.valeur)),
                zip_rec(L1.suivant, L2.suivant))


L1 = Node(3, Node(1, Node(4, Node(1, Node(5, Node(9, Node(2)))))))
L2 = Node(1, Node(6, Node(1, Node(8, Node(0, Node(3, Node(3)))))))
L3 = Node(1, Node(2, Node(3)))
print(Liste(zip_rec(L1, L2)))
print(Liste(zip_rec(L1, L3)))


################################################################################
# LISTE CROISSANTE

# On considère qu'un liste vide ou avec un seul élément sont croissantes

def croissante_iter(L: Node) -> bool:
    if L is None:
        return True
    p = L
    while p.suivant is not None:
        if p.valeur > p.suivant.valeur:
            return False
        p = p.suivant
    return True

L = Node(1, Node(6, Node(6, Node(42, Node(73)))))
print(croissante_iter(L))  # True
L = Node(1, Node(6, Node(0, Node(42))))
print(croissante_iter(L))  # False



def remove_all(L: Node, elem) -> Node:
    if L is None: return None
    if L.valeur == elem:
        return remove_all(L.suivant, elem)
    return Node(L.valeur, remove_all(L.suivant, elem))

L = Node(1, Node(1, Node(1, Node(8, Node(1, Node(3, Node(3)))))))
print(Liste(remove_all(L, 1)))



def remove_all_iter(L: Node, elem) -> Node:
    if L is None: return None
    if L.suivant is None:
        return None if L.valeur == elem else Node(L.valeur)
    res = Node(L.valeur)
    res_tl = res
    while L is not None:
        if L.valeur != elem:
            res_tl.suivant = Node(L.valeur)
            res_tl = res_tl.suivant
        L = L.suivant
    return res

L = Node(1, Node(1, Node(1, Node(8, Node(1, Node(3, Node(3)))))))
print(Liste(remove_all_iter(L, 1)))



################################################################################
# interclassement

def copy(L: Node) -> Node:
    """Créer une copie d'une liste chaînée."""
    if L is None: return None
    return Node(L.valeur, copy(L.suivant))

def copy_iter(L: Node) -> Node:
    """Créer une copie d'une liste chaînée."""
    if L is None: return None
    res = Node(L.valeur)
    p = res
    q = L.suivant
    while q is not None:
        p.suivant = Node(q.valeur)
        p = p.suivant
        q = q.suivant
    return res


def interclassement(L1: Node, L2: Node) -> Node:
    if L1 is None: return copy(L2)
    if L2 is None: return copy(L1)
    p = L1
    q = L2
    # init 1ère valeur
    res = None
    if p.valeur < q.valeur:
        res = Node(p.valeur)
        p = p.suivant
    else:
        res = Node(q.valeur)
        q = q.suivant
    w = res
    while p is not None and q is not None:
        if p.valeur < q.valeur:
            w.suivant = Node(p.valeur)
            w = w.suivant
            p = p.suivant
        else:
            w.suivant = Node(q.valeur)
            w = w.suivant
            q = q.suivant
    if p is None:
        w.suivant = copy(q)
    elif q is None:
        w.suivant = copy(p)
    return res

L1 = Node(1, Node(6, Node(42, Node(73, Node(1237)))))
L2 = Node(0, Node(12, Node(37, Node(67, Node(68)))))
print(Liste(interclassement(L1, L2)))


