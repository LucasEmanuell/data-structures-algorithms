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
    hma = test_insert_hma(size_table, charge_factor, values_to_insert, rehashing=rehashing)
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

# -----------------------------------------------------------
# NOVA FUNÇÃO: test_insert_rehashing_steps
# -----------------------------------------------------------
def test_insert_rehashing_steps(size_table, values, steps_to_print=None):
    """
    Insere os valores de 'values' passo a passo em QuadraticProbing,
    com tabela inicial de tamanho 'size_table' (THo=11, por exemplo),
    e imprime a tabela nos passos definidos em 'steps_to_print'.

    :param size_table: tamanho inicial da tabela de hash (ex: 11)
    :param values: lista de valores a inserir
    :param steps_to_print: lista de passos em que se deseja imprimir a tabela
                           (ex: [9, 16])
    """
    if steps_to_print is None:
        steps_to_print = []

    print(f"=== Hashing Fechada com Quadratic Probing ===")
    print(f"TH0 = {size_table}, com rehashing ativado.")
    qp = QuadraticProbing(size_table=size_table, rehashing=True)

    # Inserção passo a passo
    for i, val in enumerate(values, start=1):
        print(f"\n>>> Passo {i}: inserindo '{val}'")
        qp.insert_data(val)  # insere 1 a 1
        # Se este passo está na lista de "steps_to_print", imprimimos a tabela
        if i in steps_to_print:
            print(f"\n--- Tabela após o {i}º passo ---")
            print(qp)

    # Ao final, imprimir a tabela completa (opcional)
    print("\n=== Tabela Final ===")
    print(qp)


# ---------------------------------------------------------------------
# CHAMADA DE TESTE para exibir passos 9 e 16
# ---------------------------------------------------------------------

if __name__ == "__main__":
    # Conjunto S
    S = [32, 77, 441, 22, 62, 131, 16, 81, 91, 31,
         19, 21, 22, 88, 11, 876, 69, 16, 36, 12, 19]

    # Precisamos exibir o 9º e 16º passo
    steps = [9, 16]

    # Tamanho inicial da tabela = 11 (THo = 11)
    test_insert_rehashing_steps(size_table=11, values=S, steps_to_print=steps)
