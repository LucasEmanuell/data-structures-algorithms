#!/usr/bin/env python3
from .hash_table import HashTable
from collections import deque
from terminaltables import AsciiTable
from .number_theory.prime_numbers import next_prime  # Certifique-se de importar corretamente


class HashTableWithLinkedList(HashTable):
    """
    Hash Table implementation using Separate Chaining (Linked Lists).
    """

    def __init__(self, size_table, charge_factor=None, lim_charge=None, rehashing=False):
        super().__init__(size_table, charge_factor, lim_charge, rehashing)
        # Inicializa cada bucket como uma deque para representar a lista ligada
        self.values = [deque() for _ in range(self.size_table)]
        self.num_elements = 0  # Contador para número total de elementos

    def _set_value(self, key, data):
        # Adiciona o dado à frente da deque correspondente ao bucket
        self.values[key].appendleft(data)
        # Mapeia o dado para o bucket
        self._keys[data] = key
        self.num_elements += 1
        print('{0} inserido no bucket {1}'.format(data, key))
        # Verifica o fator de carga após a inserção
        if self.with_rehashing and self.load_factor() > self.lim_charge:
            print("Fator de carga excedido! Realizando rehashing...")
            self.rehashing()

    def load_factor(self):
        """
        Calcula o fator de carga atual.
        """
        return self.num_elements / self.size_table

    def insert_data(self, data):
        key = self.hash_function(data)

        # Verifica se o dado já existe no bucket
        if data in self.values[key]:
            print(f"'{data}' já existe no bucket {key}")
            return key, data
        else:
            self._set_value(key, data)
            return key, data

    def delete_value(self, value):
        key = self.hash_function(value)
        if value in self.values[key]:
            self.values[key].remove(value)
            del self._keys[value]
            self.num_elements -= 1
            print('Value "{}" has been removed from bucket {}!'.format(value, key))
            print(self)
            return value
        else:
            print('Value "{}" not found in bucket {}.'.format(value, key))
            return None

    def _mount_table(self):
        table = [
            ["Bucket", "Linked_List_Values"]
        ]
        for key, linked_list in enumerate(self.values):
            line = [key]
            if linked_list:
                line.append(" -> ".join(str(item) for item in linked_list))
            else:
                line.append("None")
            table.append(line)
        return AsciiTable(table).table

    def rehashing(self):
        """
        Realiza o rehashing da tabela.
        """
        # Coleta todos os elementos existentes
        survivor_values = []
        for bucket in self.values:
            survivor_values.extend(bucket)

        # Calcula o novo tamanho da tabela
        new_size = next_prime(self.size_table * 2)
        print("Rehashing: aumentando o tamanho da tabela de {} para {}.".format(self.size_table, new_size))

        # Reinicializa a tabela
        self.size_table = new_size
        self.values = [deque() for _ in range(self.size_table)]
        self._keys.clear()
        self.num_elements = 0  # Reset do contador

        # Reinserção dos elementos
        for value in survivor_values:
            self.insert_data(value)

    def balanced_factor(self):
        # Calcula o fator de balanceamento baseado no comprimento máximo das listas ligadas
        if self.size_table == 0:
            return 1.0
        if not any(self.values):
            return 1.0  # Tabela vazia está perfeitamente balanceada
        balanced_factor_table = max([len(cell) for cell in self.values if len(cell) > 0], default=0)
        list_values = [balanced_factor_table - len(cell) for cell in self.values if len(cell) > 0]
        return 1 - (sum(list_values) / (self.size_table * balanced_factor_table))
        # return sum([self.charge_factor - len(slot) for slot in self.values if slot is not None])\
        #        / self.size_table * self.charge_factor
