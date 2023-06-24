import math
co = float(input('Comprimento do Cateto Oposto: '))
ca = float(input('Comprimento do Cateto Adjacen: '))
'''hi = (co ** 2 + ca ** 2) ** (1/2)
print ('A hipotenusa vai medir {}.'.format(hi))'''
hi = math.hypot(co, ca)
print ('A hipotenusa vai medir {:.2f}.'.format(hi))
