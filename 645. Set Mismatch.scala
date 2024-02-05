object Solution {
  def findErrorNums(nums: Array[Int]): Array[Int] = {
    val n = nums.length
    val total = nums.sum
    var numSet: Set[Int] = Set.empty
    for (num <- nums) {
      if (!numSet.contains(num)) {
        numSet += num // Add num to the set
      } else {
        return Array(num, num + n * (1 + n) / 2 - total) 
      }
    }
    Array.empty[Int]
  }
}