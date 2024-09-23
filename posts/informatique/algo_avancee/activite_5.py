from typing import Self

# 1.

class AB:
    def __init__(self, value, left: Self =None, right: Self =None):
        self.value = value
        self.left = left
        self.right = right

    def __str__(self) -> str:
        return self._to_str()

    def _to_str(self, indent: str = '', before: str =' ') -> str:
        val = str(self.value)
        width = len(val) + 1
        val_repr = indent + before + val
        res = ""
        match (self.left, self.right):
            case (None, None):
                res += val_repr + '\n'
            case (None, right):
                res += val_repr + "╮\n"
                res += right._to_str(indent + ' '*width, before='╰')
            case (left, None):
                res += left._to_str(indent + ' '*width, before="╭")
                res += val_repr + "╯\n"
            case (left, right):
                res += left._to_str(indent + ' '*width, before="╭")
                res += val_repr + "┤\n"
                res += right._to_str(indent + ' '*width, before="╰")
        return res

# 2.

def ab_vide(ab: AB) -> bool:
    return AB is None


# 3.

def est_feuille(ab: AB) -> bool:
    return (AB.left is None) and (AB.right is None)

# QUESTIONS DE COURS

# 1.

def nb_noeuds(ab: AB) -> int:
    if est_vide(ab): return 0
    return max(nb_noeuds(ab.left), nb_noeuds(ab.right))

A = AB(12, AB(137, AB(3, AB(28),
                         AB(37)),
                   AB('x', AB(67, AB("coucou")),
                           AB(73))),
           AB(3, AB(5),
                 AB(6)))

print(A)


# 2.

