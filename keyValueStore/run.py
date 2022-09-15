"""
Question: design a key value DS, to support 3 methods
there will be a global version to keep track of all inputs
1. put key value: put key value pair into DS
2. get key: get the latest value of the key
3. get key version: return the value with version <= given version
"""
from keyValueStore import KVStore
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


# get instruction and write to output
test = KVStore()
output = []
for instruction in buffer: 
    move = instruction.split( )
    operation = move[0]
    key = move[1]

    # find out which method to call
    if len(move) == 2: # get key
        output.append(test.get(key))
    elif operation == 'PUT': # put key value
        output.append(test.put(key, int(move[2])))
    else: # get key version
        output.append(test.getVer(key, int(move[2])))   

# stdout
for item in output:
    sys.stdout.write(str(item)+'\n')