# This is a very complicated function, it sums two numbers and return the result
def sum(a, b):
    return a + b

# Since it's such a complex code, we wish to make sure it's working properly.
# To do that, we'll use a few pre-calculated values to make sure it's doing the adition correctly.
# Then we compare with the expected result and test if it's doing alright.

def test_sum(a, b, expected_result):
    return sum(a, b) == expected_result


# Test cases
print(test_sum(1, 2, 3))  # 1 + 2 = 3; True
print(test_sum(2, 2, 2))  # 2 + 2 = 2; False
print(test_sum(1, 1, 1))  # 1 + 1 = 1; False
print(test_sum(1, 2, 4))  # 1 + 2 = 4; False
print(test_sum(0.1, 0.1, 0.2))  # 0.1 + 0.1 = 0.2; True
print(test_sum(0.1, 0.1, 0.3))  # 0.1 + 0.1 = 0.3; False
print(test_sum(0.1, 0.2, 0.3))  # 0.1 + 0.2 = 0.3; True
print(test_sum(0.2, 0.2, 0.4))  # 0.2 + 0.2 = 0.4; True

# As you can see, it is spotting mistakes in the examples
# Such as 2 + 2 = 2.
# But it is not working properly on the 0.1 + 0.2 case, which should be correctly 0.3
