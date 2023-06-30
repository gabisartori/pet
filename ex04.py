# This one is about printing pretty little stairs
# The output should be a certain number of lines
# And each of them must have one more symbol than the previous

output = []
temp = []
for i in range(5):
    temp.append('*')
    output.append(temp)

# The output should look like this
# ['*']
# ['*', '*']
# ['*', '*', '*']
# ['*', '*', '*', '*']
# ['*', '*', '*', '*', '*']

# But it looks like this
# ['*', '*', '*', '*', '*']
# ['*', '*', '*', '*', '*']
# ['*', '*', '*', '*', '*']
# ['*', '*', '*', '*', '*']
# ['*', '*', '*', '*', '*']
for line in output:
    print(line)
