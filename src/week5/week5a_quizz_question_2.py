my_list = [1,2]
my_list = my_list + [10, 20]
print my_list
my_list.extend([10, 20])
print my_list
my_list.reverse()
print my_list
another_list = [99,98]
another_list.extend(my_list)
print another_list
print my_list
my_list.append(10)
print my_list