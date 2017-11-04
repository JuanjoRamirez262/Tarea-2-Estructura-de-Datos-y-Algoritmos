# -*- coding: utf-8 -*-
"""
Created on Sat Nov 04 14:57:18 2017

@author: juanjo
"""

t,b,f,c = raw_input().strip().split(' ')
t,b,f,c = [int(t),int(b),int(f),int(c)]

n = t+1 #numero de nodos

nodos=[set([]) for _ in xrange(n+1)]

nodos[0].add(n) #agregamos en la primera posicion el numero de nodos

#Todas las condiciones fueron calculadas para que no exceda en la capacidad del algoritmo y evitar caidas.

if t < 0 or b < 0 or f < 0 or c < 0:
    print 'Alguno de los datos es negativo, por lo que no se puede hacer un grafo con tales caracteristicas.'
elif b > (((n-1)*(n-2)/2) + 1):
    print 'Los backwards edge solicitados exceden el maximo de la capacidad de este algoritmo.'
elif c > n-2:
    print 'Los cross edge solicitados exceden el maximo de la capacidad de este algoritmo.'
elif f > ((n-2)*(n-1)/2 -(n-2)):
    print 'Los forward edge solicitados exceden el maximo de la capacidad de este algoritmo.'
else:
    #agregar los tree
    #Se crea una rama extensa de largo n-1, y el que falta se crea en otra rama
    tlargo = len(nodos) #Largo lista nodos (numero de nodos y nodos por separado)
    i=1
    while i<=tlargo:
        if i<(len(nodos)-2):
            nodos[i].add(i+1)
        else:
            nodos[1].add(len(nodos)-1)
        i+=1
    
    #agregar los forward
    #Creamos forwards partiendo de la primera rama, y los vamos conectando hasta completar los forwards requeridos
    pos = 1
    while f != 0:
        m = pos + 2
        while m <= n:
            nodos[pos].add(m)
            m += 1
            f -= 1
        pos += 1
    
    
    #agregar los backwards
    #Se parte de la rama mas lejana, y nos vamos devolviendo hasta llegar al principio, y luego nos adelantamos un nodo
    #y repetimos el proceso
    contadorback = 0
    restador = 1
    n2 = n
    while b !=0 :
            if contadorback == 0:
                nodos[n2].add(1)
                contadorback = 1
                b -= 1
                n2 -= 1
            else:
                while (n2 -restador > 0 and b!=0):
                    nodos[n2].add(n2-restador)
                    restador +=1 
                    b -= 1
                n2 -= 1
            restador = 1
    
    #agregar los cross
    #Del nodo que dejamos airlado, conectamos a la otra rama cosa de poder crear cross edge
    posicion = 2
    while c != 0:
        nodos[n].add(posicion)
        posicion += 1
        c -= 1
        
    #imprimimos lo anteriormente calculado
    for j in xrange(1,n+1):
      print len(nodos[j]),
      for num in nodos[j]:
        print num,
      print  
