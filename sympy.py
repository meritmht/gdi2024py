# AUFGABE 4.3

from sympy.logic.boolalg import And, Or, Not, Implies, Equivalent
from sympy.logic.boolalg import to_cnf
from sympy.abc import A, B, C

f = ( ((A & ~B) >> C) & ( C >> (A | B) ) & ( ~( A & C) ))
f

