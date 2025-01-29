#!/usr/bin/env python3
from .hash_table import HashTable

class QuadraticProbing(HashTable):
    """
    Basic Hash Table example with open addressing using Quadratic Probing.
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

    def _find_index(self, key):
        """
        Retorna o índice onde a 'key' está armazenada, ou None se não estiver.
        """
        base_index = self.hash_function(key)
        size = self.size_table
        i = 0
        while i < size:
            index = (base_index + i*i) % size
            # Se achar um slot vazio, então a chave não está na tabela
            if self.values[index] is None:
                return None
            # Se achamos a chave
            if self.values[index] == key:
                return index
            i += 1
        return None

    def __getitem__(self, key):
        index = self._find_index(key)
        if index is None:
            raise KeyError(f"Key '{key}' not found")
        return self.values[index]

    def __delitem__(self, key):
        index = self._find_index(key)
        if index is None:
            raise KeyError(f"Key '{key}' not found for deletion")
        self.values[index] = None
        # qualquer limpeza ou marcação de 'deleted' se necessário

    def __contains__(self, key):
        try:
            _ = self[key]
            return True
        except KeyError:
            return False
