#!/usr/bin/env python3
<<<<<<< HEAD
<<<<<<< HEAD
from number_theory.prime_numbers import next_prime
=======
from .number_theory.prime_numbers import next_prime
>>>>>>> hma
=======
from .number_theory.prime_numbers import next_prime
>>>>>>> hma
from terminaltables import AsciiTable

class HashTable:
    """
        Basic Hash Table example with open addressing and linear probing.
        This class works as father of other hash table variations
    """

<<<<<<< HEAD
<<<<<<< HEAD
    def __init__(self, size_table, charge_factor=None, lim_charge=None):
=======
    def __init__(self, size_table, charge_factor=None, lim_charge=None, rehashing=False):
>>>>>>> hma
=======
    def __init__(self, size_table, charge_factor=None, lim_charge=None, rehashing=False):
>>>>>>> hma
        """

        :param size_table: recommended a prime number
        :param charge_factor: define the charge per slot
        :param lim_charge: define when rehashing must be done
        """
        self.size_table = size_table
        self.values = [None] * self.size_table #the hash table start with empty slots
        self.lim_charge = 0.75 if lim_charge is None else lim_charge
        self.charge_factor = 1 if charge_factor is None else charge_factor
        self.__aux_list = []
<<<<<<< HEAD
<<<<<<< HEAD
        self._keys = {} # the result of hash_function operation
=======
=======
>>>>>>> hma
        self._keys = {}
        self.with_rehashing = rehashing
        # the result of hash_function operation
        [self._initialize_keys(index) for index in range(self.size_table)]

    def _initialize_keys(self, index):
        self._keys[index] = None
<<<<<<< HEAD
>>>>>>> hma
=======
>>>>>>> hma

    def keys(self):
        return self._keys

    def __str__(self):
        return self._mount_table()

    def balanced_factor(self):
        return sum([1 for slot in self.values
                    if slot is not None]) / (self.size_table * self.charge_factor)

    def hash_function(self, key):
        """
<<<<<<< HEAD
<<<<<<< HEAD

=======
>>>>>>> hma
=======
>>>>>>> hma
        :param key: value of slot
        :return: a key that represent the position of key-value in array
        """
        return key % self.size_table

<<<<<<< HEAD
<<<<<<< HEAD
    def mount_table(self):
=======
    def _mount_table(self):
>>>>>>> hma
=======
    def _mount_table(self):
>>>>>>> hma
        table = [
            [index for index in range(len(self.values))],
            [value for value in self.values]
        ]
        return AsciiTable(table).table
<<<<<<< HEAD
<<<<<<< HEAD

    def _step_by_step(self, step_ord):

        print("step {0}".format(step_ord))
        # print([i for i in range(len(self.values))])
        # print(self.values)
        print(self.mount_table())
=======
=======
>>>>>>> hma

    def _str_hash_function(self, data, key):
        return "{0} mod {1} = {2}".format(data, self.size_table, key)

    def _step_by_step(self, step_ord, data_insert_tuple):
        pass
<<<<<<< HEAD
>>>>>>> hma
=======
>>>>>>> hma

    def bulk_insert(self, values):
        i = 1
        self.__aux_list = values
        [self.insert_data(value) for value in values]

    def _set_value(self, key, data):
        self.values[key] = data
        self._keys[key] = data
        print('{0} insert in bucket {1}'.format(data, key))
        # print(self)

    def _colision_presentation(self, **kwargs):
        return 'colision: {data} mod {size_table} = {new_key}'.format(**kwargs)

    def _insert_presentation(self, **kwargs):
        return '{data} mod {size_table} = {key}'.format(**kwargs)

    def _colision_resolution(self, key, data=None):
        new_key = self.hash_function(key + 1)

        while self.values[new_key] is not None \
                and self.values[new_key] != key:

            if self.values.count(None) > 0 and self.values[new_key] is not None \
                    and self.values[new_key] != key:
                print(self._colision_presentation(data=data, size_table=self.size_table, new_key=new_key))
                new_key = self.hash_function(new_key + 1)
            else:
                new_key = None
                break

        return new_key

    def delete_value(self, value):
        try:
            index = self.values.index(value)
            self.values[index] = None
            return index
        except ValueError:
            return None

    def rehashing(self):
        survivor_values = [value for value in self.values if value is not None]
        self.size_table = next_prime(self.size_table, factor=2)
        self._keys.clear()
        self.values = [None] * self.size_table #hell's pointers D: don't DRY ;/
        print("rehashing new size table value => {0}".format(self.size_table))
        map(self.insert_data, survivor_values)

    def _insert_presentation(self, key, data, **kwargs):
        return 'insert {0} in bucket {1}'.format(data, key)

    def insert_data(self, data):
        key = self.hash_function(data)

        if self.values[key] is None:
            self._set_value(key, data)
            return key, data

        elif self.values[key] == data:
            pass

        else:
            new_key = self._colision_resolution(key, data)
            if new_key is not None:
                self._set_value(new_key, data)
            elif new_key is None and self.with_rehashing is True:
                self.rehashing()
                self.insert_data(data)
            else:
                print("\n*-*-*-*- Element {0} couldn't be inserted ! -*-*-*-*\n".format(data))

        



