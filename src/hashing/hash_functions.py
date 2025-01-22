def universal_hash(key, size_table, base=31):
    if isinstance(key, int):
        return key % size_table
    elif isinstance(key, str):
        h = 0
        for char in key:
            h = (base * h + ord(char)) % size_table
        return h
    else:
        raise TypeError(f"Tipo de chave não suportado: {type(key)}")