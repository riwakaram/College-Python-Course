s1 = {1, 2, 3}
s2 = {'Hello', 1.0, (1, 2, 3)}
print(s1)
print(s2)
print()

s1.add(3)
s2.add(3)
print(s1)
print(s2)
print()

print(s1 & s2)
print(s1 | s2)
print(s2 - s1)
print()

s2.remove(1.0)
print(s2)
