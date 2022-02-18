#lists
#Tuples - a tuple is an immutable (cannot be modified) sequence of objects
#Slicing
#Dictionaries
# a dictionary has key-value pairs

# dic = {}
# dic["Joe"] = "room 101"
# dic["Elias"] = "room 302"
# dic["Hanan"] = "room 205"
#
# for key in dic.keys():
#     print(key + " lives in " + dic[key])

# people = ['Joe', 'Elias', "Hanan"]
# rooms = ['room 101', 'room 302', 'room 205']
# dic = {}
# for i in range(len(people)):
#     dic[people[i]] = rooms[i]
#
# print(dic)

# Passing arguments to functions


def double_value_v1(l):
    print('inside double_value_v1: l = %s' % l)
    for i in range(len(l)):
        l[i] = 2 * l[i]
    print('inside double_value_v1, after change: l = %s' % l)


def double_value_v2(l):
    print('inside double_value_v2: l = %s' % l)
    l = l[:]
    for i in range(len(l)):
        l[i] = 2 * l[i]
    print('inside double_value_v2, after change: l = %s' % l)


my_list = [3, -5, 10, 23]
print(my_list)
double_value_v1(my_list)
print(my_list)

my_list = [3, -5, 10, 23]
print(my_list)
double_value_v2(my_list)
print(my_list)
