# Turn the following English description into code:
# Create a list with two numbers, 0 and 1, respectively.
# For 40 times, add to the end of the list the sum of the last two numbers.

def sum_of_list():
    my_list = [0, 1]
    for i in range(0, 40):
        elemente = my_list[0:2]
        elemente = my_list[len(my_list)-2: len(my_list)]
        print elemente
        my_list.append(sum(elemente))
    return my_list

print sum_of_list()

