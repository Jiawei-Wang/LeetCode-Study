# 思考：key value pair，每个key只有一个value，每个value只有一个key，则算成功
class Solution:
  def wordPattern(self, pattern: str, s: str) -> bool:
    words = s.split(" ")
    length = len(pattern)
    if length != len(words):
      return False
    dic = dict()
    available = set(words)
    for i in range(length):
      char = pattern[i]
      word = words[i]
      # 每次步进到一个新的元素组合，有四种可能情况：
      if char not in dic and word in available: # 全新组合，放进dic中
        dic[char] = word
        available.remove(word)
      elif char in dic and word in available: # 旧key配新value，肯定不符合条件
        return False
      elif char not in dic and word not in available: # 新key配旧value，肯定不符合条件
        return False
      elif dic[char] != word: # 旧key配旧value，此时依旧分两种：1. 在dic中发现不匹配则False，2. 在dic中发现匹配则跳过此轮
        return False

    return True


# 2024
class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        array = s.split()
        return map(pattern.find, pattern) == map(array.index, array)

        """
        string.find gets the smallest index for a char in a string
        for example: pattern = "example"
        list(map(pattern.find, pattern)) = [0, 1, 2, 3, 4, 5, 0]
        
        array.index does the same thing
        for example: array = ["e", "x", "a", "m", "p", "l", "e"]
        results = list(map(array.index, array)) = [0, 1, 2, 3, 4, 5, 0]
        """