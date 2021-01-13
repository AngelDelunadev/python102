string = "backwards"
backward_string = ""
x = len(string)
while x != 0 :
    backward_string = backward_string + string[x-1]
    x = x -1
print(backward_string)

