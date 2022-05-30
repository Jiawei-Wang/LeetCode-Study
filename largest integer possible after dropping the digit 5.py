# Given an integer, return the largest integer possible after dropping the digit 5 from the integer
class solution:
  def findLargest(self, target):
    cur = float('-inf')
    for i in target:
      new = int(str(i).replace('5', ''))
      cur = max(cur, new)
    return cur


ans = solution()
target = [115, 511, 152]
print(ans.findLargest(target))