# sort() function is very similar to sorted() but unlike sorted it returns nothing
# and makes changes to the original sequence.
# Moreover, sort() is a method of list class and can only be used with lists.

# Syntax: List_name.sort(key, reverse=False)
# Parameters:
# key: A function that serves as a key for the sort comparison.
# reverse: If true, the list is sorted in descending order.
# Return type: None

def sort_basic():
    # List of Integers
    numbers = [1, 3, 4, 2]
    numbers.sort()
    print(numbers)

    # List of Floating point numbers
    decimal_number = [2.01, 2.00, 3.67, 3.28, 1.68]
    decimal_number.sort()
    print(decimal_number)

    # List of strings
    words = ["Geeks", "For", "Geeks"]
    words.sort()
    print(words)


def sort_using_revert_order():
    # List of Integers
    numbers = [1, 3, 4, 2]
    numbers.sort(reverse=True)
    print(numbers)

    # List of Floating point numbers
    decimal_number = [2.01, 2.00, 3.67, 3.28, 1.68]
    decimal_number.sort(reverse=True)
    print(decimal_number)


def sort_second(val):
    return val[1]


def sort_using_key_parameter():
    list1 = [(1, 5), (2, 4), (3, 1)]
    # list1 = sort_second(list1)
    list1.sort(key=sort_second)
    print(list1)

    list1.sort(key=sort_second, reverse=True)
    print(list1)


if __name__ == '__main__':
    print("Sorting basic:\n ---------")
    sort_basic()
    print("Sorting in reverse order:\n ---------")
    sort_using_revert_order()
    print("Using key parameter:\n --------- ")
    sort_using_key_parameter()
