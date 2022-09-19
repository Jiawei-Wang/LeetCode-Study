"""
1. how are we going to come up with a word -> follow up 
2. what kind of DS to store the word -> hashmap
3. how are we going to give feedback -> stdin/stdout
"""
import sys
import random

class hangMan:
    def __init__(self, input):
        self.out = dict() # key = char, value = [indexes for the char in the input]
        self.string = input
        self.chance = 5
        self.curr = ''

    # constract the data structure
    def makeWord(self):
        temp = self.string
        for word in temp.split(): # hello, world
            self.curr += '_' * len(word) + ' '
        self.curr = self.curr[:-1]
        
        for index in range(len(self.string)): # a dict without space but with all other chars
            if self.string[index] != ' ':
                if self.string[index] not in self.out:
                    self.out[self.string[index]] = [index]
                else:
                    self.out[self.string[index]].append(index)
    
    # guess the word by taking one input at one time
    def guessWord(self, char):
        # input validation
        if not char:
            return 'try again'
        if not char.isalpha():
            return 'invalid input, try again'
        if len(char) != 1:
            return 'try again'

        if char in self.out:
            ind = self.out[char] 
            for index in ind:
                self.curr = self.curr[0:index] + self.string[index] + self.curr[index+1:]
        else:
            self.chance -= 1
            if not self.chance:
                return 'you lose'
        
        if self.curr == self.string:
            return "you win"

        return [self.curr, self.chance]


first = random.choice(open("input.txt").readlines()) # random(num=3) ?
second = random.choice(open("input.txt").readlines())
third = random.choice(open("input.txt").readlines())
input = str(first + " "+ second+""+ third)
print(input)
test = hangMan(input)
test.makeWord()

buffer = []
run = True
while run:
    line = sys.stdin.readline().rstrip('\n') 
    line = str(line)
    if line == 'quit':
        run = False
    else:
        buffer.append(line)
        print(test.guessWord(line))











