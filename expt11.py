#conversion of list to tuple tuple to list to dictionary from dictionary etc.
#expt 11
#create basic tuple list
print("LIST TO TUPLE")
l = [1, 2, 3, 4]
t = tuple(l)
print("List:", l)
print("Converted to Tuple:", t)
print("TUPLE TO LIST")
#converting tuple list
newlist = list(t)
print("Tuple:", t)
print("Converted to List:", newlist)
print("LIST OF TUPLES TO DICTIONARY")
# Each tuple must be (key, value)
tuple_list = [('a', 1), ('b', 2), ('c', 3)]
dicttuples = dict(tuple_list)#type onversion
print("List of Tuples:", tuple_list)
print("Converted to Dictionary:", dicttuples)
#2 lists to dict with inbuilt methods
#we can also traverse and manually add key values
#but for this program we use inbuilt methods
print("TWO LISTS TO DICTIONARY" )
keys = ['name', 'age', 'city']
values = ['Alice', 25, 'New York']
dictlists = dict(zip(keys, values))
print("Keys:", keys)
print("Values:", values)
print("Zipped to Dictionary:", dictlists)

print("DICTIONARY TO LISTS ")
my_dict = {'x': 10, 'y': 20, 'z': 30}
keys_list = list(my_dict.keys())
values_list = list(my_dict.values())
items_list = list(my_dict.items())
print("Dictionary:", my_dict)
print("Keys List:", keys_list)
print("Values List:", values_list)
print("Items List (tuples):", items_list)

print("DICTIONARY TO TUPLE ")
keys_tuple = tuple(my_dict.keys())
values_tuple = tuple(my_dict.values())
items_tuple = tuple(my_dict.items())
print("Keys Tuple:", keys_tuple)
print("Values Tuple:", values_tuple)
print("Items Tuple:", items_tuple)
