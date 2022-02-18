# Chapter04 - Introspection
# introspection is an ability to determine the type of an object at runtime
# Everything in python is an object. Every object in Python may have attributes
# and methods.

# dir()
# type()
# isinstance()
# help
# Docstrings
# def power2and3(x):
#     """Returns the tuple (x**2, x**3)"""
#     return x**2, x**3
#
# power2and3(2)


# Chapter05 - Input and Output
# print specifiers in Python (%f, %e, %g, %d, %s, %r)
# files

# my_file = open("temp.txt", "w")
# my_file.write("This is my first text file created in Python")
# my_file.close()

my_file = open("temp.txt", "r")
text = my_file.read()
my_file.close()
print(text)

# Chapter06 - Control Flow
# if
# for
