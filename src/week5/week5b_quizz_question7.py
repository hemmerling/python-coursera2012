def square_list(numbers):
        result = []
        for n in numbers:
                result.append(n**2)
        return result

def is_even(number):
    """Returns whether the number is even."""
    return number % 2 == 0

#print square_list ([4,5,-2])
#print is_even(5)

l = [1, 2, 3, 4, 5, 6, 7]
print [is_even(number) for number in l]
print [number for number in l if is_even(number)]
print [n for n in l if is_even(n)]
#print [if is_even(number): number for number in l] 
