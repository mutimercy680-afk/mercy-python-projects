fruits=["apple","banana","mango"]
print(fruits)


colors=["red","blue","green"]
print(colors[1])

user= {"name":"mercy","age":17}
print(user["name"])


user={"name":"mercy","age":17}
for key in user.keys():
  print(key)
  for value in user.values():
    print(value)

    student = {"name": "John", "age":20, "grade": "a"}

 # Adding elements
fruits.add("orange")
print("After adding orange:", fruits)

# Removing elements
fruits.remove("banana")
print("After removing banana:", fruits)

a = frozenset([1,2,3])
b = frozenset([1,2,])