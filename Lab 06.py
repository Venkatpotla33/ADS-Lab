# Quadratic probing with Hashing And Double Hashing

# Quadratic Probing

# general formula (h'(k) + c1*i + c2*i^2) % m.

class HashTable:
    """
    A simple implementation of a Hash Table using Quadratic Probing for collision resolution.
    """

    def __init__(self, size, c1=0, c2=1):
        """
        Initializes the hash table.
        Args:
            size (int): The size of the hash table. It's recommended to use a prime number
                        for better distribution.
            c1 (int): The constant for the linear term in the quadratic probe.
            c2 (int): The constant for the quadratic term in the probe. Must be non-zero.
        """
        self.size = size
        # Initialize the table with None, indicating empty slots
        self.table = [None] * self.size
        if c2 == 0:
            raise ValueError("c2 cannot be zero for Quadratic Probing, as it would degrade to linear probing.")
        self.c1 = c1
        self.c2 = c2


    def _hash_function(self, key):
        """
        A simple modular hash function.
        Args:
            key (int): The key to be hashed.
        Returns:
            int: The calculated hash index.
        """
        return key % self.size

    def insert(self, key):
        """
        Inserts a key into the hash table using a general quadratic probing formula.
        The formula used is: (initial_hash + c1*i + c2*i^2) % table_size
        Args:
            key (int): The key to be inserted.
        """
        initial_hash = self._hash_function(key)

        # Case 1: The initial slot is empty
        if self.table[initial_hash] is None:
            self.table[initial_hash] = key
            print(f"Inserted {key} at index {initial_hash}")
            return

        # Case 2: The initial slot is occupied (collision)
        print(f"Collision for key {key} at index {initial_hash}. Starting quadratic probing.")
        i = 1
        while True:
            # Calculate next index using the general quadratic probing formula
            next_index = (initial_hash + self.c1 * i + self.c2 * i * i) % self.size

            if self.table[next_index] is None:
                self.table[next_index] = key
                print(f"  -> Inserted {key} at index {next_index} after {i} probe(s).")
                return

            # If we loop back to the start, the table might be full or in a cycle
            if next_index == initial_hash:
                print(f"Could not insert key {key}. Hash table may be full or stuck in a cycle.")
                return

            i += 1
            # To prevent an infinite loop if the table is poorly sized or full
            if i >= self.size:
                 print(f"Could not insert key {key}. Probed {i} times without success. Table is likely full.")
                 return


    def search(self, key):
        """
        Searches for a key in the hash table.
        Args:
            key (int): The key to search for.
        Returns:
            int: The index of the key if found, otherwise None.
        """
        initial_hash = self._hash_function(key)

        i = 0
        while i < self.size:
            # The index to check is (initial_hash + c1*i + c2*i^2) % size
            # i starts at 0 for the initial check of the home slot
            probe_index = (initial_hash + self.c1 * i + self.c2 * i * i) % self.size

            # If we find an empty slot along the probe path, the key cannot be in the table
            if self.table[probe_index] is None:
                print(f"Key {key} not found (empty slot at index {probe_index}).")
                return None

            # If we find the key, return its index
            if self.table[probe_index] == key:
                print(f"Key {key} found at index {probe_index}.")
                return probe_index

            i += 1

        # If we complete the loop without finding the key
        print(f"Key {key} not found after checking all possible probe locations.")
        return None

    def display(self):
        """
        Displays the contents of the hash table.
        """
        print("\n--- Hash Table ---")
        for i, value in enumerate(self.table):
            print(f"Index {i}: {value if value is not None else 'Empty'}")
        print("--------------------\n")


if __name__ == "__main__":
    keys_to_insert = [18, 48, 78, 28, 58]

    # --- Example 1: Simple Quadratic Probing (h(k) + i^2) ---
    print("--- Example 1: Probing with (h(k) + i^2) ---")
    # Uses default c1=0, c2=1
    ht_simple = HashTable(10)
    print(f"Inserting keys: {keys_to_insert}\n")
    for key in keys_to_insert:
        ht_simple.insert(key)
    ht_simple.display()

    # --- Example 2: Custom Quadratic Probing (h(k) + i + i^2) ---
    print("\n--- Example 2: Probing with (h(k) + i + i^2) ---")
    # Using the general quadratic form with c1=1, c2=1
    ht_custom = HashTable(10, c1=1, c2=1)
    print(f"Inserting keys: {keys_to_insert}\n")
    for key in keys_to_insert:
        ht_custom.insert(key)
    ht_custom.display()

    # --- Search Demonstration on custom table ---
    print("--- Searching in custom table ---")
    # Search for a key that exists and required probing
    ht_custom.search(28)

    # Search for a key that does not exist
    ht_custom.search(99)
    
    
    
# Double Hashing

class HashTable:
    """
    An implementation of a Hash Table using Double Hashing for collision resolution.
    """

    def __init__(self, size):
        """
        Initializes the hash table.
        Args:
            size (int): The size of the hash table. For double hashing, it is crucial
                        that this size is a prime number to ensure the probe sequence
                        can visit all slots.
        """
        self.size = size
        self.table = [None] * self.size
        # A prime number smaller than the table size, used for the second hash function.
        self.prime_for_h2 = self._get_smaller_prime(size)
        if self.prime_for_h2 is None:
            raise ValueError("Table size is too small to find a secondary prime.")

    def _is_prime(self, n):
        """Checks if a number is prime."""
        if n <= 1:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    def _get_smaller_prime(self, n):
        """Finds a prime number smaller than n."""
        for i in range(n - 1, 1, -1):
            if self._is_prime(i):
                return i
        return None

    def _hash_function_1(self, key):
        """
        Primary hash function. Determines the initial probe index.
        Args:
            key (int): The key to be hashed.
        Returns:
            int: The calculated initial hash index.
        """
        return key % self.size

    def _hash_function_2(self, key):
        """
        Secondary hash function. Determines the step size for probing.
        This function must NOT return 0.
        The formula used here is: R - (key % R), where R is a prime smaller than table size.
        Args:
            key (int): The key to be hashed.
        Returns:
            int: The step size for probing, which is always greater than 0.
        """
        return self.prime_for_h2 - (key % self.prime_for_h2)

    def insert(self, key):
        """
        Inserts a key into the hash table using double hashing.
        The formula is: (h1(k) + i * h2(k)) % size
        Args:
            key (int): The key to be inserted.
        """
        initial_hash = self._hash_function_1(key)

        # Case 1: The initial slot is empty
        if self.table[initial_hash] is None:
            self.table[initial_hash] = key
            print(f"Inserted {key} at index {initial_hash}")
            return

        # Case 2: The initial slot is occupied (collision)
        print(f"Collision for key {key} at index {initial_hash}.")
        step_size = self._hash_function_2(key)
        print(f"  -> Calculated step size for {key}: {step_size}")

        i = 1
        while True:
            next_index = (initial_hash + i * step_size) % self.size

            if self.table[next_index] is None:
                self.table[next_index] = key
                print(f"  -> Inserted {key} at index {next_index} after {i} probe(s).")
                return

            # If we loop back, the table is full.
            if next_index == initial_hash:
                print(f"Could not insert key {key}. Hash table is full.")
                return

            i += 1
            if i >= self.size:
                print(f"Could not insert key {key}. Table is full.")
                return

    def search(self, key):
        """
        Searches for a key in the hash table.
        Args:
            key (int): The key to search for.
        Returns:
            int: The index of the key if found, otherwise None.
        """
        initial_hash = self._hash_function_1(key)

        i = 0
        while i < self.size:
            probe_index = (initial_hash + i * self._hash_function_2(key)) % self.size if i > 0 else initial_hash

            if self.table[probe_index] is None:
                print(f"Key {key} not found (empty slot at index {probe_index}).")
                return None

            if self.table[probe_index] == key:
                print(f"Key {key} found at index {probe_index}.")
                return probe_index

            i += 1

        print(f"Key {key} not found after a full table scan.")
        return None

    def display(self):
        """Displays the contents of the hash table."""
        print("\n--- Hash Table ---")
        for i, value in enumerate(self.table):
            print(f"Index {i}: {value if value is not None else 'Empty'}")
        print("--------------------\n")


if __name__ == "__main__":
    # For Double Hashing, the table size should be a prime number.
    table_size = 11
    ht = HashTable(table_size)
    print(f"Created a Hash Table of size {table_size}.")
    print(f"The prime for the second hash function is {ht.prime_for_h2}.\n")

    # Keys designed to cause collisions
    keys_to_insert = [19, 27, 33, 44, 55, 66]
    print(f"Inserting keys: {keys_to_insert}\n")

    for key in keys_to_insert:
        ht.insert(key)

    ht.display()

    # --- Search Demonstration ---
    print("--- Searching for keys ---")
    ht.search(44)  # Exists, required probing
    ht.search(19)  # Exists, at initial slot
    ht.search(100) # Does not exist