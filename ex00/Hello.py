ft_list = ["Hello", "tata!"]
ft_tuple = ("Hello", "toto!")
ft_set = {"Hello", "tutu!"}
ft_dict = {"Hello": "titi!"}

# TODO: modify the string of each data object to display the following:
# 1. "Hello World"
# 2. "Hello «country of your campus»"
# 3. "Hello «city of your campus»"
# 4. "Hello «name of your campus»"

# your code here
# Accessing list is by index
ft_list[1] = "World!"
# Accessing tuple is by index (readonly) as tuples are immutable
# To modify a tuple, you need to create a new tuple
ft_tuple = ("Hello", "Armenia!")
# set is mutable but elements are unique.
# Accessing set by index is not supported
# While you can make a new set, sets support `discard()` and `add()` methods
# sets will not keep the order of elements!!!
ft_set.discard("tutu!")
ft_set.add("Yerevan!")
# dict is mutable. Accessing dict is by key
ft_dict["Hello"] = "42Yerevan!"

print(ft_list)
print(ft_tuple)
print(ft_set)
print(ft_dict)
