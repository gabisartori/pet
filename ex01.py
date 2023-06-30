import math

# This function uses the math module to calculate the sin of a given angle
def sin(angle):
    return math.sin(angle)

# But when tested upon a few entry values, it gives off weird results
# Why is that and how can you fix the function so that, with the same inputs,
# It returns the expected values.

print(f"{sin(30):.3f}", "Expected 0.500")
print(f"{sin(180):.3f}", "Expected 0.000")
print(f"{sin(0):.3f}", "Expected 0.000")  # That one works ¯\_(ツ)_/¯
print(f"{sin(60):.3f}", "Expected 0.866")
