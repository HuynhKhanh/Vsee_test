# sorted() method sorts the given sequence as well as set and dictionary(which is not a sequence)
# either in ascending order
# or in descending order(does unicode comparison for string char by char)
# and always returns the a sorted list. This method doesn’t effect the original sequence.

# Syntax: sorted(iteraable, key, reverse=False)affect
# Parameters:
# Iterable: sequence (list, tuple, string) or collection (dictionary, set, frozenset)
# or any other iterator that needs to be sorted.
# Key(optional): A function that would serve as a key or a basis of sort comparison.
# Reverse(optional): If set True, then the iterable would be sorted in reverse (descending) order,
# by default it is set as False.
# Return Type: Returns a sorted list.


def sorted_basic():
    L = [1, 2, 3, 4, 5]
    print("Sorted List:", sorted(L))

    print("\nReverse sorted list:", sorted(L, reverse=True))


def sorted_different_data_type():
    # List
    x = ['q', 'w', 'r', 'e', 't', 'y']
    print(sorted(x))

    #tuple
    x = ('q', 'w', 'e', 'r', 't', 'y')
    print(sorted(x))

    # String-sorted based on ASCII translations
    x = "python"
    print(sorted(x))

    # Dictionary
    x = {'q': 1, 'w': 2, 'e': 3, 'r': 4, 't': 5, 'y': 6}
    print(sorted(x))

    # Python program to demonstrate
    # sorted()

    # List
    x = ['q', 'w', 'r', 'e', 't', 'y']
    print(sorted(x))

    # Tuple
    x = ('q', 'w', 'e', 'r', 't', 'y')
    print(sorted(x))

    # String-sorted based on ASCII translations
    x = "python"
    print(sorted(x))

    # Dictionary
    x = {'q': 1, 'w': 2, 'e': 3, 'r': 4, 't': 5, 'y': 6}
    print(sorted(x))

    # Set
    x = {'q', 'w', 'e', 'r', 't', 'y'}
    print(sorted(x))


def swap():
    x = 5
    y = 10
    x,y = y,x
    print( x,y)


def swap_arr(a, b, c):
    return a if a <= b and a <= c else (b if b <= a and b <= c else c)


if __name__ == '__main__':
    sorted_basic()
    print("-------")
    sorted_different_data_type()
    swap()
    print(swap_arr(1, 4, 5))
