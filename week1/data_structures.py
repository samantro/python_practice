# Demonstration of basic list operations in Python
lst = [1,2,3,4,5]
print("Original list:", lst)

lst.append(6)
print("After appending 6:", lst)

lst.remove(3)
print("After removing 3:", lst)

print("List length:", len(lst))
print("Secontd element: {0}\nLast element: {1}".format(lst[1], lst[-1]))

# Demonstration of basic tuple operations in Python

tpl = (10, 20, 30)
print("Original tuple:", tpl)

tpl += (40,)  # Adding an element to a tuple
print("After adding 40:", tpl)
print("First tuple:", tpl[0])

# Demonstration of basic set operations in Python

st = {1, 2, 3, 3, 3, 4}
print("Original set (duplicates removed):", st)

st.add(5)
print("After adding 5:", st)

st.remove(2)
print("After removing 2:", st)

# Demonstration of basic dictionary operations in Python

profile = {
  "mame": "Alice",
  "age": 30,
  "city": "New York",
  "skills": ["Python", "Data Analysis", "Machine Learning"]
}

profile["skills"].append("Deep Learning")
profile["age"] = 26

for key, value in profile.items():
    print(key)

for key, value in profile.items():
    print(value)