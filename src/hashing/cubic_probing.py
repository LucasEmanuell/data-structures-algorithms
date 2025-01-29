#!/usr/bin/env python3
from .hash_table import HashTable

class CubicProbing(HashTable):
    """
        Hash Table implementation using Cubic Probing for collision resolution.
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.lim_charge = self._lim_charge_func()

    def _lim_charge_func(self):
        return self.size_table // 2 + 1  # Pode ajustar conforme necessário

    def _colision_resolution(self, key, data=None):
        """
            Resolve colisões usando Cubic Probing.
            new_key = (hash + i^3) % size_table
        """
        i = 1
        # Tenta no máximo self.size_table vezes para evitar loops infinitos
        while i < self.size_table:
            # Calcula o novo índice usando Cubic Probing
            new_key = self.hash_function(key + i**3)

            if self.values[new_key] is None or self.values[new_key] == data:
                return new_key

            i += 1

        # Se não encontrou um slot vazio após todas as tentativas, retorna None para rehash
        return None
