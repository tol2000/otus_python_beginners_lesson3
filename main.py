"""
Compare `is` and `==`
"""

a = [1, 2, 3]
b = [1, 2, 3]
c = a


print("id of a:", id(a))
print("id of b:", id(b))
print("id of c:", id(c))


print("a == b:", a == b)
print("a is b:", a is b)

print("a == c:", a == c)
print("a is c:", a is c)

print(a, b, c)
a.append(4)
# TODO: modify other lists
