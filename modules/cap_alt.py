#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
lista ordenada ao contrário
"""


class cap():
    def __init__(self):
        self._start=0
        self._list = []
        
    def proximo(self):
        return self._list[-1]

    
    def apaga(self):
        self._list.pop()


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
                if tempo < time:
                    left = meio + 1
                else:
                    right = meio
                    
          
            self._list.insert(right, evento)
            
            
            