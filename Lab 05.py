# Linked List

# Implement Linked List And Build Levels of Linked List in Implementing a Skip List

import random

class SkipNode:

    def __init__(self, value, level):
        self.value = value
        self.forwards = [None] * (level + 1)

class SkipList:

    def __init__(self, max_level=6, p=0.5):
        self.max_level = max_level
        self.p = p
        self.header = SkipNode(-1, self.max_level)
        self.level = 0

    def random_level(self):

        lvl = 0
        while random.random() < self.p and lvl < self.max_level:
            lvl += 1
        return lvl


# Inserting
    def insert(self, value):

        update = [None] * (self.max_level + 1)
        current = self.header

        # Corrected loop to iterate from highest level down to 0
        for i in range(self.level, -1, -1):
            while current.forwards[i] and current.forwards[i].value < value:
                current = current.forwards[i]
            update[i] = current

        current = current.forwards[0]

        if current is None or current.value != value:
            rnd_level = self.random_level()

            # If new random level is greater than current skip list level,
            # update the header's forward pointers for the new levels.
            if rnd_level > self.level:
                for i in range(self.level + 1, rnd_level + 1):
                    update[i] = self.header
                self.level = rnd_level

            new_node = SkipNode(value, rnd_level)

            for i in range(rnd_level + 1):
                new_node.forwards[i] = update[i].forwards[i]
                update[i].forwards[i] = new_node

# Searching
    def search(self, value):
        """Searches for a value in the skip list."""
        current = self.header

        # Corrected loop to iterate from highest level down to 0
        for i in range(self.level, -1, -1):
            while current.forwards[i] and current.forwards[i].value < value:
                current = current.forwards[i]


        current = current.forwards[0]
        if current and current.value == value:
            return True
        return False

# Display

    def print_list(self):
        """Prints the skip list level by level, showing the linked list at each level."""
        print("\nSkip List Levels (representing linked lists at each level):")

        for i in range(self.level, -1, -1):

            current = self.header.forwards[i]
            print(f"Level {i}: ", end="")

            while current:
                print(current.value, end=" -> ")
                current = current.forwards[i]
            print("None")
            
            
skip_list = SkipList(max_level=6, p=0.5)


values_to_insert = [3, 6, 7, 9, 12, 19, 17, 26, 21, 25]
print("Inserting values:", values_to_insert)
for value in values_to_insert:
    skip_list.insert(value)


skip_list.print_list()


values_to_search = [19, 5, 26, 10]
print("\nSearching for values:")
for value in values_to_search:
    if skip_list.search(value):
        print(f"{value} found in the skip list.")
    else:
        print(f"{value} not found in the skip list.")
        



skip_list = SkipList(max_level=6, p=0.5)


values_to_insert = [3, 6, 7, 9, 12, 19, 17, 26, 21, 25]
print("Inserting values:", values_to_insert)
for value in values_to_insert:
    skip_list.insert(value)


skip_list.print_list()


values_to_search = [19, 5, 26, 10]
print("\nSearching for values:")
for value in values_to_search:
    if skip_list.search(value):
        print(f"{value} found in the skip list.")
    else:
        print(f"{value} not found in the skip list.")
        
        
        

skip_list = SkipList(max_level=6, p=0.5)


values_to_insert = [3, 6, 7, 9, 12, 19, 17, 26, 21, 25]
print("Inserting values:", values_to_insert)
for value in values_to_insert:
    skip_list.insert(value)


skip_list.print_list()


values_to_search = [19, 5, 26, 10]
print("\nSearching for values:")
for value in values_to_search:
    if skip_list.search(value):
        print(f"{value} found in the skip list.")
    else:
        print(f"{value} not found in the skip list.")