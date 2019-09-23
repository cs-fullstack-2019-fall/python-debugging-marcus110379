# ### Problem 5:
# Create the list: squad = ["One", "Two", "Three", "Four", "Five"]. Print the list in reverse without using a list method.

squad = ["One", "Two", "Three", "Four", "Five"]
for index of range(len(squad -1), -1, -1):  #You need to change "of" to "in" for range
    print(squad(index))  #you need to use bracket [] instead of parenthesis () around index
    