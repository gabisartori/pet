# This function returns the sum of values in a certain interval of a list
# The idea is that the interval is described in a human-like way
# So 1 means the first element, 2 means the second and so on
def total_sum(list_of_values, start, end):
    # Checking if you put in proper values
    if end > len(list) or start < 1:
        print("This interval does not make sense!")
        return

    # Actual function
    total = 0
    for i in range(start, end):
        total += list_of_values[i]
    return total


# But as it is, the function is not including all of the items in the total sum
example_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(total_sum(example_list, 1, 9))  # expected output: 45
