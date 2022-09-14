# in run.py, the input is given as a file
# if the interviewer wants to use command line for input
# the following should work

import sys

# read from command line one line at a time
# type 'quit' to finish the input
buffer = []
run = True
while run:
    line = sys.stdin.readline().rstrip('\n') 
    if line == 'quit':
        run = False
    else:
        buffer.append(line)
print(buffer)