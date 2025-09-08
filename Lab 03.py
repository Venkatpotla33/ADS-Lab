# Implementing Dictionary With Array and Hash Table

# Create a Basic Dictionary


s_details = {
    "name": "Venkata",
    "age": 26,
    "course": "Data Science",
    "grade": "A"
}

# Accessing dictionary values
print("Name:", s_details["name"])
print("Age:", s_details["age"])
print("Course:", s_details["course"])



# Adding and Updating Elemets

s_details["college"]="gitam"
s_details["grade"]="B"
print(s_details)


# delete and remove the elemets

del s_details["grade"]
print(s_details)


age=s_details.pop("age")
print(age)
print(s_details)




# Implemting the Dictionary Array without Hashing

# Dictionary Array without Hashing and Dictionary as a Tuples


dictionary = []

def insert(dictionary, key, value):
    for i, (k, v) in enumerate(dictionary):
        if k == key:   # key exists, update it
            dictionary[i] = (key, value)
            return
    dictionary.append((key, value))  # key not found, add new pair

# Function to get a value by key
def get(dictionary, key):
    for k, v in dictionary:
        if k == key:
            return v
    return None  # if key not found

# Function to delete a key-value pair
def delete(dictionary, key):
    for i, (k, v) in enumerate(dictionary):
        if k == key:
            dictionary.pop(i)
            return True
    return False  # key not found

# Function to display dictionary contents
def display(dictionary):
    for k, v in dictionary:
        print(f"{k} : {v}")



# Insert elements
insert(dictionary, "name", "Venkata")
insert(dictionary, "age", 23)
insert(dictionary, "course", "Data Science")

print("Dictionary after insertions:")
display(dictionary)

# Update an existing key
insert(dictionary, "age", 24)
print("\nDictionary after updating age:")
display(dictionary)

# Retrieve a value
print("\nGet 'course':", get(dictionary, "course"))

# Delete a key
delete(dictionary, "name")
print("\nDictionary after deleting 'name':")
display(dictionary)


# Dictionary Array without Hashing and Dictionary as a Tuples


dictionary = []

def insert(dictionary, key, value):
    for i, (k, v) in enumerate(dictionary):
        if k == key:   # key exists, update it
            dictionary[i] = (key, value)
            return
    dictionary.append((key, value))  # key not found, add new pair

# Function to get a value by key
def get(dictionary, key):
    for k, v in dictionary:
        if k == key:
            return v
    return None  # if key not found

# Function to delete a key-value pair
def delete(dictionary, key):
    for i, (k, v) in enumerate(dictionary):
        if k == key:
            dictionary.pop(i)
            return True
    return False  # key not found

# Function to display dictionary contents
def display(dictionary):
    for k, v in dictionary:
        print(f"{k} : {v}")



# Insert elements
insert(dictionary, "name", "Venkata")
insert(dictionary, "age", 23)
insert(dictionary, "course", "Data Science")

print("Dictionary after insertions:")
display(dictionary)

# Update an existing key
insert(dictionary, "age", 24)
print("\nDictionary after updating age:")
display(dictionary)

# Retrieve a value
print("\nGet 'course':", get(dictionary, "course"))

# Delete a key
delete(dictionary, "name")
print("\nDictionary after deleting 'name':")
display(dictionary)


# Dictionary with Hash Table

class HashTable:
    def __init__(self, capacity=20):
        self.capacity = capacity
        self.table = [[] for _ in range(self.capacity)]

    def _hash(self, key):
        return hash(key) % self.capacity

    def insert(self, key, value):
        index = self._hash(key)
        for i, (k, v) in enumerate(self.table[index]):
            if k == key:
                self.table[index][i] = (key, value)  # Update value if key exists
                return
        self.table[index].append((key, value))  # Add new key-value pair

    def get(self, key):
        index = self._hash(key)
        for k, v in self.table[index]:
            if k == key:
                return v
        return None  # Key not found

    def delete(self, key):
        index = self._hash(key)
        for i, (k, v) in enumerate(self.table[index]):
            if k == key:
                del self.table[index][i]
                return True  # Deletion successful
        return False  # Key not found

    def display(self):
        for i in range(self.capacity):
            print(f"Bucket {i}: {self.table[i]}")

# Example usage
ht = HashTable(5)
ht.insert("name", "Venkat")
ht.insert("age", 26)
ht.insert("course", "Data Science")
ht.insert("college", "gitam")
ht.insert("grade", "A")

print("Hash Table after insertions:")
ht.display()

print("\nGet 'course':", ht.get("course"))
print("Get 'city':", ht.get("city")) # Key not found

ht.insert("age", 27) # Update age
print("\nHash Table after updating age:")
ht.display()

ht.delete("college")
print("\nHash Table after deleting 'college':")
ht.display()


class HashTable:
    def __init__(self, capacity=10):
        self.capacity = capacity
        self.table = [[] for _ in range(self.capacity)]

    def _hash(self, key):
        return hash(key) % self.capacity

    def insert(self, key, value):
        """Inserts a key-value pair into the hash table or updates the value if the key exists."""
        index = self._hash(key)
        for i, (k, v) in enumerate(self.table[index]):
            if k == key:
                self.table[index][i] = (key, value)  # Update value if key exists
                print(f"Updated key '{key}' with value '{value}'")
                return
        self.table[index].append((key, value))  # Add new key-value pair
        print(f"Inserted key '{key}' with value '{value}'")

    def get(self, key):
        """Retrieves the value associated with the given key. Returns None if the key is not found."""
        index = self._hash(key)
        for k, v in self.table[index]:
            if k == key:
                print(f"Found value '{v}' for key '{key}'")
                return v
        print(f"Key '{key}' not found")
        return None  # Key not found

    def delete(self, key):
        """Deletes the key-value pair associated with the given key. Returns True if successful, False otherwise."""
        index = self._hash(key)
        for i, (k, v) in enumerate(self.table[index]):
            if k == key:
                del self.table[index][i]
                print(f"Deleted key '{key}'")
                return True  # Deletion successful
        print(f"Key '{key}' not found for deletion")
        return False  # Key not found

    def display(self):
        """Displays the contents of the hash table."""
        print("\nHash Table Contents:")
        for i in range(self.capacity):
            print(f"Bucket {i}: {self.table[i]}")

# Example usage:
ht = HashTable(5)

ht.insert("name", "Venkata")
ht.insert("age", 26)
ht.insert("course", "Data Science")
ht.insert("college", "gitam")
ht.insert("grade", "A")

ht.display()

ht.get("course")
ht.get("city") # Key not found

ht.insert("age", 27) # Update age
ht.display()

ht.delete("college")
ht.display()
ht.delete("city") # Key not found for deletion

