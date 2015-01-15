from pysb import *

Model()

Monomer('a', ['a1'])

Parameter('k', 1e-5)
Parameter('l', 1e-8)

Rule('p',  a(a1=None) + a(a1=None) <> a(a1=1) % a(a1=1), k, l)

Parameter('ao',100)
Initial(a(a1=None),ao)

Observable('tp', a(a1=1)%a(a1=1))
Observable('ta', a(a1=None))