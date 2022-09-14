"""
Question: design a data structure that can store all words in a dictionary and also their ranks,
such that when a prefix is given, the first 5 words that contain the prefix are returned with regards to the rank

input file: 
first line: number of words in dictinary
second line: number of prefixes 
the rest: individual words + previxes

thinking process:
1. a Trie to hold the dictionary
2. DFS to find closest 5 words for each prefix input
"""
from autocomplete import Autocomplete
test = Autocomplete()

# get the input and build the Trie first
f = open("input.txt")

dicSize = int(f.readline())
inputSize = int(f.readline())

for i in range(dicSize):
    word = str(f.readline())[:-1] # get rid of \n at the end of each line
    rank = i + 1 # rank of a word in dic is its index + 1
    test.insert(word, rank)

# search in Trie
output = []
for i in range(inputSize):
    prefix = str(f.readline())[:-1] # get rid of \n at the end of each line
    output.append(test.search(prefix))

print(output)