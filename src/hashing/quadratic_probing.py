#!/usr/bin/env python3
from .hash_table import HashTable

class QuadraticProbing(HashTable):
    """
        Basic Hash Table example with open addressing using Quadratic Probing 
    """
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.lim_charge = self._lim_charge_func()
    
    def _lim_charge_func(self):
        return self.size_table // 2 + 1
    
    def _colision_resolution(self, key, data=None):
        i = 1
        # Tenta no máximo self.size_table vezes
        while i < self.size_table:
            new_key = self.hash_function(key + i*i)
            
            if self.values[new_key] is None or self.values[new_key] == data:
                return new_key
            
            i += 1
        # Se saiu do loop, não achou espaço
        return None
