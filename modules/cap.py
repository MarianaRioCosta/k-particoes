#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
adicionar: colocar um novo par (tempo evento) a lista ordenada de eventos da cap com pesquisa binaria
se possível optimizar esta função
view
proximo- da o primeiro evento
apagarprimeiro - apaga o primeiro (tempo,evento)
'''

class cap:
    def __init__(self):
        
        self._start=0
        self._list=[]
       
    def proximo(self):
        return self._list[0]
    
    def apaga(self):
        self._list = self._list[1:]
        return self._list

    def view(self):
        return self._list
    
    def __str__(self):
        return "%s" % [f"evento {ev.gettipo()} em {ev.gettime()} seg" for ev in self._list]

    def adicionar(self,evento):
        if self._list == []:
            self._list.append(evento)
            
        else:
            tempo=evento.gettime()
            left=0
            right=len(self._list)
            
            while right > left:
                meio = (left+right)//2
                time=self._list[meio].gettime()
                
                if tempo > time:
                    left = meio + 1
                else:
                    right = meio
                    
          
            self._list.insert(left, evento)