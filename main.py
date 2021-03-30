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

num_a = 1
num_b = 1

print("num_a == num_b", num_a == num_b)
print("num_a is num_b", num_a is num_b)

print(a, b, c)
a.append(4)
b.append(9)
c.append(5)
print(a, b, c)

print("a is list type?", isinstance(a, list))
print("a is list-like type?", isinstance(a, (list, tuple)), type(a))

t = ()
print("t is list-like type?", isinstance(t, (list, tuple)), type(t))
