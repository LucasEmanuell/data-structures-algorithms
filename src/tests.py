from avl_tree.avl_weiss import AVL as avl_tree
from hashing.middle_open_hash import HMA
from hashing.double_hash_r import DoubleHashR
from hashing.double_hash_th import DoubleHashTH
from hashing.hash_table import HashTable
from hashing.hash_table_with_linked_list import HashTableWithLinkedList
from hashing.number_theory.prime_numbers import next_prime
from hashing.quadratic_probing import QuadraticProbing
from hashing.cubic_probing import CubicProbing


def test_insert_avl(display, values):
    tree = avl_tree(display=display)
    root = tree.createFromList(values)
    tree.display_tree(root)
    tree.nodes

def test_insert_hma(size_table, charge_factor, values, rehashing=True):
    hma = HMA(size_table=size_table, charge_factor=charge_factor, rehashing=rehashing)
    hma.bulk_insert(values)
    print(hma)
    return hma

def test_insert_double_hash_r(size_table, values):
    dh = DoubleHashR(size_table)
    dh.bulk_insert(values)
    print(dh)

def test_insert_hash_linked_list(size_table, charge_factor, values):
    hl = HashTableWithLinkedList(charge_factor=charge_factor, size_table=size_table)
    hl.bulk_insert(values)
    return hl

def test_insert_hash_table(size_table, values):
    ht = HashTable(size_table=size_table)
    ht.bulk_insert(values)
    return ht

def test_nex_lt_prime(value):
    _next = next_prime(value)
    return _next

def test_double_hash_th(size_table, values):
    dh = DoubleHashTH(size_table=size_table)
    dh.bulk_insert(values)
    return dh

def test_insert_delete_hma(size_table, charge_factor, values_to_insert, values_to_delete, rehashing=True):
    hma = test_insert_hma(size_table, charge_factor,  values_to_insert, rehashing=rehashing)
    print(hma)
    for value in values_to_delete:
        if hma.delete_value(value) is not None:
            print('element {0} deleted'.format(value))
            print(hma)
        else:
            print('element {0} not found'.format(value))

def test_balanced_factor_hma(size_table, charge_factor, values):
    hma = test_insert_hma(size_table, charge_factor, values, rehashing=False)
    print(hma.balanced_factor())

def test_balanced_factor_linked_list_hash(size_table, charge_factor, values):
    hash_linked_list = test_insert_hash_linked_list(size_table, charge_factor, values)
    print(hash_linked_list.balanced_factor())

def test_insert_rehashing(size_table, values):
    rehash = QuadraticProbing(size_table=size_table, rehashing=True)
    rehash.bulk_insert(values)
    print(rehash)

def test_insert_rehashing_cubic(size_table, values):
    rehash = CubicProbing(size_table=size_table, rehashing=True)
    rehash.bulk_insert(values)
    print(rehash)
def test_insert_delete_hash_linked_list(size_table, charge_factor, values_to_insert, values_to_delete):
    hl = HashTableWithLinkedList(size_table=size_table, charge_factor=charge_factor)
    print("Inserindo valores:")
    for value in values_to_insert:
        hl.insert_data(value)
    print("\nTabela de Hash após inserções:")
    print(hl)
    
    print("\nDeletando valores:")
    for value in values_to_delete:
        hl.delete_value(value)
    
    print("\nTabela de Hash após deleções:")
    print(hl)
#test_insert_delete_hma(7,3,[32, 77, 441, 22, 62, 131, 16, 81, 91, 31, 19, 21, 22, 88, 11, 876, 69, 16, 36, 12, 19],[19, 81, 101, 441, 11, 22, 14])
# print(test_balanced_factor_linked_list_hash(5, 3, [22, 43, 16,16, 44, 77, 62]))   
#test_balanced_factor_hma(7, 2, [0,1,85,6,36,46,89,112,44])
# print(test_double_hash_th(29, [22, 43, 36, 16, 44, 77, 62, 32, 71, 31, 41, 27, 29, 19, 7, 14, 91, 81, 1]))
#test_insert_double_hash_r(11, [31, 11, 14, 92, 33, 11, 65, 87, 49, 7, 19, 32, 71, 12, 73,23])
# test_insert_hma(5,2, ['A31', 'hB2', 'wA5', 'Hv3', '12y', '0o1', '4Ab', 'S84', 'd32', '34a', 'C4W', '6b2', 'C128', 'Zz5', 'WgC', '12s', '51K', '3GH', 'A9W', 'Vt1', '1x3', 'a89', '2D1', '35', '8Yx'], True)
#test_insert_delete_hma(5,2, ['A31', 'hB2', 'wA5', 'Hv3', '12y', '0o1', '4Ab', 'S84', 'd32', '34a', 'C4W', '6b2', 'C128', 'Zz5', 'WgC', '12s', '51K', '3GH', 'A9W', 'Vt1', '1x3', 'a89', '2D1', '35', '8Yx'], ['Hv3', 'S84', '6b2', 'Zz5', '12y'], True)
# A31, hB2, wA5, Hv3, 12y, 0o1, 4Ab, S84, d32, 34a, C4W, 6b2, C128, Zz5, WgC, 12s, 51K, 3GH, A9W, Vt1, 1x3, a89, 2D1, 35, 8Yx
# ['A31', 'hB2', 'wA5', 'Hv3', '12y', '0o1', '4Ab', 'S84', 'd32', '34a', 'C4W', '6b2', 'C128', 'Zz5', 'WgC', '12s', '51K', '3GH', 'A9W', 'Vt1', '1x3', 'a89', '2D1', '35', '8Yx']
#test_insert_rehashing(size_table=5, values=['A31', 'hB2', 'wA5', 'Hv3', '12y', '0o1', '4Ab', 'S84', 'd32', '34a', 'C4W', '6b2', 'C128', 'Zz5', 'WgC', '12s', '51K', '3GH', 'A9W', 'Vt1', '1x3', 'a89', '2D1', '35', '8Yx'])
#test_insert_rehashing_cubic(5,['A31', 'hB2', 'wA5', 'Hv3', '12y', '0o1', '4Ab', 'S84', 'd32', '34a', 'C4W', '6b2', 'C128', 'Zz5', 'WgC', '12s', '51K', '3GH', 'A9W', 'Vt1', '1x3', 'a89', '2D1', '35', '8Yx'])
#test_insert_hash_linked_list(size_table=7,charge_factor=3,values_to_insert=[32, 77, 441, 22, 62, 131, 16, 81, 91, 31, 19, 21, 22, 88, 11, 876, 69, 16, 36, 12, 19],values_to_delete=[19, 81, 101, 441, 11, 22, 14])
test_insert_delete_hash_linked_list(
    size_table=7,
    charge_factor=3,
    values_to_insert=[32, 77, 441, 22, 62, 131, 16, 81, 91, 31, 19, 21, 22, 88, 11, 876, 69, 16, 36, 12, 19],
    values_to_delete=[19, 81, 101, 441, 11, 22, 14]
)
