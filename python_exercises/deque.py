# Import the deque class from the collections module
# A deque (pronounced "deck") is a double-ended queue that supports 
# adding and removing elements from both ends with O(1) performance.
from collections import deque

# Initialize an empty deque object
d = deque()

# Request an integer input from the user, to determine the number of operations
X = int(input())

# Loop through the range of the number provided by the user
for i in range(X):
    
    # Request a string input from the user for each iteration. This string input is expected to be a command
    command = str(input())
    
    # Check if a space exists in the command, this indicates the command has an argument
    if " " in command:
        # Split the command into method and arg by the space delimiter
        method,arg = command.split()
        
        # getattr function gets the method name from the deque object 'd' and applies it with the argument 'arg'
        # This line effectively performs operations like d.append(arg) or d.appendleft(arg) based on user's input
        getattr(d,method)(arg)
    
    # If there is no space in the command, it means the command does not have an argument
    else:
        method = command
        
        # Similar to the previous getattr, but this one is for methods without arguments like d.pop() or d.popleft()
        getattr(d,method)()

# After all operations are complete, print the contents of the deque 'd'
# The ' '.join(list(d)) converts the deque elements into a space-separated string before printing.
print(' '.join(list(d)))
