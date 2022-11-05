#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
LISTA MAGICA:
    - é uma lista que tem um elemento para cada bloco: -1, se o bloco não for perfeito e o tempo em que o bloco foi criado, se ele for perfeito
    - como ao mutar um individuo temos que manter os tempos de algumas coisas, ao crirar um individuo novo vamos passar uma lista magica como argumento
    -depois associamos ao individuo essa lista e fazemos update
    
    - se a lista que passarmos estiver vazia, é porque o individuo está mesmo a ser criado de raiz e geramos uma lista
    
    - caso seja uma mutação, vamos dar replace de um individuo por outro na população, e passamos a lista do antigo
    - assim quando mutarmos um individuo, a lista vai ser atualizada
    
    
    -ao fazer get lista magica, vamos devolver a lista com -1 se não for perfeito, e o tempo em que cada bloco foi criado, para a morte calculamos a diferenca entre esse tempo e o agora
"""


"""
getnif
getparticao
create_listamagica
update_listamagica
get_listamagica
coef = coeficiente de inadaptação
"""

class indv:
    
    def __init__(self, k, w, part, tempo, listamagica,nif):
        
        self._start=0
        
        self._particao = part
        
        self._nif = nif
        
        self._listamagica = listamagica
        self._listamagica = self.update_listamagica(w, k, tempo)
        
    
    def getnif(self):
        return self._nif
    
    def getparticao(self):
        return self._particao

    def __str__(self):
        return "%s" % self._particao
    
    def create_listamagica(self,w,k, tempo):
            
        listamagica = []
        
        perf = sum(w)//k
        
        lista_somas = self._particao.soma_blocos(w, k)
        
        for x in lista_somas:
            if x == perf:
                listamagica.append(tempo)
            else:
                listamagica.append(-1)
        
        return listamagica
  

    def update_listamagica(self, w, k, tempo):
        if self._listamagica == []:
            return self.create_listamagica(w, k, tempo)
        
        else:
            lista_somas = self._particao.soma_blocos(w, k)
                
            perf = sum(w)//k
            return [tempo if (lista_somas[x] == perf and self._listamagica[x] == -1) else self._listamagica[x] for x in range(k)]

    def getlista_magica(self):
        return self._listamagica