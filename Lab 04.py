# Implementing collision resolution techniques

# Linear Probing
# Quardatical Probing


# Linear Probing

# used in hash tables when two keys hash to the same index.

# How It Works

# 1. Hash the key using a hash function.

# 2. If the slot is empty, insert the key-value pair there.

# 3. If the slot is occupied, move sequentially through the table ((index+1) % capacity) until an empty slot is found
# 4. For searching, if the key is not at the hashed index, continue probing linearly until you either find it or hit an empty slot.
# 5. For deletion, you typically mark a slot as deleted (a special placeholder) rather than making it fully empty, to avoid breaking the probe sequence.


# Functions for Linear Probing Hash Table

def create_hash_table(capacity=10):
    """Creates a hash table with the given capacity."""
    return [None] * capacity, 0, capacity # table, size, capacity

def _hash(key, capacity):
    """Simple hash function"""
    return hash(key) % capacity

def insert(hash_table, key, value):
    """Insert or update key-value pair"""
    table, size, capacity = hash_table

    if size == capacity:
        raise Exception("Hash table is full")

    index = _hash(key, capacity)

    while table[index] is not None and table[index][0] != key:
        index = (index + 1) % capacity

    # New key or update existing key
    if table[index] is None:
        size += 1
    table[index] = (key, value)
    # Create a new tuple with updated size
    hash_table = (table, size, capacity)
    return hash_table # Return the updated hash_table

def search(hash_table, key):
    """Search for a key and return its value"""
    table, size, capacity = hash_table
    index = _hash(key, capacity)
    start_index = index  # remember where we started

    while table[index] is not None:
        if table[index][0] == key:
            return table[index][1]
        index = (index + 1) % capacity
        if index == start_index:  # we've looped around
            break
    return None  # not found

def delete(hash_table, key):
    """Delete a key by marking its slot as deleted"""
    table, size, capacity = hash_table
    index = _hash(key, capacity)
    start_index = index

    while table[index] is not None:
        if table[index][0] == key:
            table[index] = ("<deleted>", None)
            size -= 1
            # Create a new tuple with updated size
            hash_table = (table, size, capacity)
            return hash_table # Return the updated hash_table
        index = (index + 1) % capacity
        if index == start_index:
            break
    return hash_table # Return the original hash_table if key not found


ht = create_hash_table(5)
ht = insert(ht, "apple", 100)
ht = insert(ht, "banana", 200)
ht = insert(ht, "grape", 300)
ht = insert(ht, "orange", 400)

print("Searching for grape:", search(ht, "grape"))
print("Searching for mango:", search(ht, "mango"))

ht = delete(ht, "banana")
print("After deleting banana:")

def display(hash_table):
    table, size, capacity = hash_table
    for i, item in enumerate(table):
        print(f"Slot {i}: {item}")

display(ht)



# Quadratic probing

# Another collision resolution technique for hash tables. It works like linear probing but instead of checking the next slot one-by-one

# Helps to spread out collisions and avoid clustering, which can occur with linear probing


# How it Works

# Compute the initial index using hash(key) % capacity.

# If the index is empty, insert the element.

# If the index is full, try

# (index + 1^2) % capacity,

# (index + 2^2) % capacity,

# (index + 3^2) % capacity, ...
# until an empty slot is found.

# Searching and deletion follow the same probing sequence

# Functions for Quadratic Probing Hash Table

def create_quadratic_hash_table(capacity=10):
    """Creates a hash table with the given capacity."""
    return [None] * capacity, 0, capacity # table, size, capacity

def _quadratic_hash(key, capacity):
    """Simple hash function"""
    return hash(key) % capacity

def quadratic_insert(hash_table, key, value):
    """Insert or update key-value pair"""
    table, size, capacity = hash_table

    if size == capacity:
        raise Exception("Hash table is full")

    index = _quadratic_hash(key, capacity)
    i = 0

    # probe until an empty slot or matching key is found
    while table[(index + i * i) % capacity] is not None and \
          table[(index + i * i) % capacity][0] != key:
        i += 1

    final_index = (index + i * i) % capacity
    if table[final_index] is None:
        size += 1
    table[final_index] = (key, value)
    # Create a new tuple with updated size
    hash_table = (table, size, capacity)
    return hash_table # Return the updated hash_table

def quadratic_search(hash_table, key):
    """Search for a key and return its value"""
    table, size, capacity = hash_table
    index = _quadratic_hash(key, capacity)
    i = 0

    while table[(index + i * i) % capacity] is not None:
        current_index = (index + i * i) % capacity
        if table[current_index][0] == key:
            return table[current_index][1]
        i += 1
        if i == capacity:  # full loop
            break
    return None  # not found

def quadratic_delete(hash_table, key):
    """Delete a key by marking its slot as deleted"""
    table, size, capacity = hash_table
    index = _quadratic_hash(key, capacity)
    i = 0

    while table[(index + i * i) % capacity] is not None:
        current_index = (index + i * i) % capacity
        if table[current_index][0] == key:
            table[current_index] = ("<deleted>", None)
            size -= 1
            # Create a new tuple with updated size
            hash_table = (table, size, capacity)
            return hash_table # Return the updated hash_table
        i += 1
        if i == capacity:
            break
    return hash_table # Return the original hash_table if key not found

def quadratic_display(hash_table):
    """Display the table contents"""
    table, size, capacity = hash_table
    for i, entry in enumerate(table):
        print(f"Index {i}: {entry}")


ht_qp = create_quadratic_hash_table(7)
ht_qp = quadratic_insert(ht_qp, "apple", 10)
ht_qp = quadratic_insert(ht_qp, "banana", 20)
ht_qp = quadratic_insert(ht_qp, "grape", 30)
ht_qp = quadratic_insert(ht_qp, "orange", 40)

print("Searching for grape:", quadratic_search(ht_qp, "grape"))  # 30
print("Searching for mango:", quadratic_search(ht_qp, "mango"))  # None

ht_qp = quadratic_delete(ht_qp, "banana")
print("After deleting banana:")
quadratic_display(ht_qp)


