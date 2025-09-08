# Creating the Dictionary

# Creating Dictionary
my_dict = {
    "name": "Venkata",
    "profession": "Data Analyst",
    "experience_years": 2,
    "skills": ["Python", "SQL", "Power BI", "Excel"],
    "Place":"Guntur"
}

# Printing the dictionary
print(my_dict)

# From List of Tuples

my_dict= dict({
    "name": "Venkata",
    "profession": "Data Analyst",
    "experience_years": 2,
    "skills": ["Python", "SQL", "Power BI", "Excel"],
    "Place":"Guntur"
})

print(my_dict)

# Inserting New Pair

my_dict["Nation"]="Indain"
my_dict["Numbers"]=(232,33,4323,43,2)


print(my_dict)

# Updating the Dictionary

my_dict["experience_years"]=3
my_dict["skills"].append("ADS")
# Corrected line: Assign a tuple to a new key
my_dict["NewNumbers"] = (34, 323, 434)
# Appending to the skills list again as it was in the original code
my_dict["skills"].append(323)


print("\nUpdateddictionary:")
print(my_dict)

# Lookup values by key

# Accessing the value associated with the "name" key
print("Name:", my_dict["name"])

# Accessing the value associated with the "skills" key
print("Skills:", my_dict["skills"])

# You can also use the .get() method, which is safer as it returns None if the key doesn't exist
print("Profession (using .get()):", my_dict.get("profession"))

# Trying to access a non-existent key using .get() will return None
print("Age (using .get()):", my_dict.get("age"))

# Trying to access a non-existent key using square brackets will raise a KeyError
try:
    print("Age (using []):", my_dict["age"])
except KeyError:
    print("Error: 'age' key not found in the dictionary.")
    
del my_dict["Place"]
print(my_dict)

my_dict.clear()
print(my_dict)

my_dict = {
    "name": "Venkata Narayana Potla",
    "profession": "Data Analyst",
    "experience_years": 3
}

# Check key membership
print("name" in my_dict)       # ✅ True
print("location" in my_dict)   # ❌ False

# Using .values()
print("Data Analyst" in my_dict.values())  # ✅ True
print("India" in my_dict.values())         # ❌ False

my_dict = {
    "name": "Venkata Narayana Potla",
    "profession": "Data Analyst",
    "experience_years": 3
}

for key in my_dict:
    print(key)

my_dict = {
    "name": "Venkata Narayana Potla",
    "profession": "Data Analyst",
    "experience_years": 3
}

for key in my_dict:
    print(key)
for key, value in my_dict.items():
    print(f"{key} → {value}")

# Problem: Word Frequency Counter

def word_frequency_counter(text):
    word_freq = {}
    words = text.split()

    for word in words:
      if word in word_freq:
        word_freq[word] +=1
      else:
          word_freq = 1
      return word_freq

Text= "Data is Every where,find and use well"
result=word_frequency_counter(Text)

print("word_frequency_counter:")
print(result)




